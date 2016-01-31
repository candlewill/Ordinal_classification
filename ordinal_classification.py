from string import punctuation
import re
from collections import defaultdict
import os

import numpy as np

from load_data import load_SemEval
from load_data import load_pickle, load_embeddings
from save_data import dump_picle
from load_data import load_SemEval_test


def clean_str(sentence):
    """
    Tokenization/string cleaning for dataset
    Every dataset is lower
    """
    for p in list(punctuation):
        sentence = sentence.replace(p, '')
    sent = sentence.lower()
    sent = re.sub(r"http.*$", "https", sent)  # replace httpfjeiwaefwfioew like with http

    return re.sub(r" +", " ", sent).strip()


# return the vocabulary dictionary, format: word-frequency
def get_vocab(corpus):
    vocab = defaultdict(int)
    for sent in corpus:
        for word in clean_str(sent).split():
            vocab[word] += 1
    print('Vocabulary Size is: %s. ' % len(vocab))
    return vocab


def add_unknown_words(word_vecs, vocab, min_df=3, k=300):
    """
    For words that occur in at least min_df documents, create a separate word vector.
    0.25 is chosen so the unknown vectors have (approximately) same variance as pre-trained ones
    """
    count = 0
    for word in vocab:
        if word not in word_vecs and vocab[word] >= min_df:
            word_vecs[word] = np.random.uniform(-0.25, 0.25, k)
            count += 1
    print("Adding unknown words with randomly generated vectors. Number of unknown words: %s." % count)
    return word_vecs


# word_vecs is the model of word2vec
def build_embedding_matrix(word_vecs, vocab, k=300):
    """
    Get word matrix. W[i] is the vector for word indexed by i
    """
    union = (set(word_vecs.keys()) & set(vocab.keys()))
    vocab_size = len(union)
    print('The number of words occuring in corpus and word2vec simutaneously: %s.' % vocab_size)
    word_idx_map = dict()
    W = np.zeros(shape=(vocab_size + 1, k))
    W[0] = np.zeros(k, dtype=np.float32)
    for i, word in enumerate(union, start=1):

        if i % 500 == 0:  # display maping method in every 500 words
            print("Word: %s ------------>> Index: %s." % (word, str(i)))

        W[i] = word_vecs[word]
        word_idx_map[word] = i  # dict
    return W, word_idx_map


def sent2ind(sent, word_idx_map):
    """
    Transforms sentence into a list of indices.
    """
    x = []
    words = sent.split()
    for word in words:
        if word in word_idx_map:
            x.append(word_idx_map[word])
        else:  # use value 0 to indicate the missing words
            x.append(0)
    return x


def make_idx_data(sentences, word_idx_map):
    """
    Transforms sentences (corpus, a list of sentence) into a 2-d matrix.
    """
    idx_data = []
    for sent in sentences:
        idx_sent = sent2ind(clean_str(sent), word_idx_map)
        idx_data.append(idx_sent)
    # idx_data = np.array(idx_data, dtype=np.int)
    return idx_data


def build_keras_input(texts, scores, test, new=True):
    # texts, scores are dict type, key: train, dev, devtest.
    keys = ["train", "dev", "devtest"]
    train, train_scores = texts[keys[0]], scores[keys[0]]
    dev, dev_scores = texts[keys[1]], scores[keys[1]]
    devtest, devtest_scores = texts[keys[2]], scores[keys[2]]

    filename_data, filename_w = './tmp/indexed_data.p', './tmp/Weight.p'

    test_filename = './tmp/test_data.p'

    if os.path.isfile(filename_data) and os.path.isfile(filename_w) and new == False:
        data = load_pickle(filename_data)
        W = load_pickle(filename_w)

        test_data = load_pickle(test_filename)

        print('Use existing data. Load OK.')
        return (data, W, test_data)

    print("Construct new data.")
    # load data from pickle

    vocab = get_vocab(train)

    # using word2vec vectors
    # word_vecs = load_embeddings('google_news', '/home/hs/Data/Word_Embeddings/google_news.bin')
    # word_vecs = load_embeddings('D:/Word_Embeddings/glove.840B.300d.txt.w2v')
    word_vecs = load_embeddings('/home/hs/Data/Word_Embeddings/glove.840B.300d.txt.w2v')

    word_vecs = add_unknown_words(word_vecs, vocab)
    W, word_idx_map = build_embedding_matrix(word_vecs, vocab)

    idx_data_train = make_idx_data(train, word_idx_map)
    idx_data_dev = make_idx_data(dev, word_idx_map)
    idx_data_devtest = make_idx_data(devtest, word_idx_map)

    idx_data_test = make_idx_data(test[2], word_idx_map)

    data = (idx_data_train, idx_data_dev, idx_data_devtest, train_scores, dev_scores, devtest_scores)

    test_data = (test[0], test[1], idx_data_test)

    dump_picle(data, filename_data)
    dump_picle(W, filename_w)
    dump_picle(test_data, test_filename)
    print("Saved: data and W are saved into: %s, and %s." % (filename_data, filename_w))

    return (data, W, test_data)


def remove_unavailable(texts, scores):
    unavailable_mark = "Not Available"
    unavailable_idx = []
    for i, t in enumerate(texts):
        if t == unavailable_mark:
            unavailable_idx.append(i)
    print("Number of unavailable texts: %s." % len(unavailable_idx))
    # Delete unavailable terms
    for i in list(reversed(unavailable_idx)):
        texts.pop(i)
        scores.pop(i)
    return (texts, scores)


def build_ordinal_regression_input():
    _, scores_train, texts_train = load_SemEval("./resources/full_tweets/train_gold.tsv")
    _, scores_dev, texts_dev = load_SemEval("./resources/full_tweets/dev_gold.tsv")
    _, scores_devtest, texts_devtest = load_SemEval("./resources/full_tweets/devtest_gold.tsv")

    _, scores_old, texts_old = load_SemEval("./resources/full_tweets/old_data.tsv")

    ids, topics, texts = load_SemEval_test(
        './resources/TEST data/SemEval2016_Task4_test_datasets/SemEval2016-task4-test.subtask-BCDE.txt')

    test = [ids, topics, texts]

    scores_train = scores_train + [i - 3 for i in scores_old]  # from [1, 5] to [-2, 2]
    texts_train = texts_train + texts_old

    keys = ["train", "dev", "devtest"]
    texts, scores = dict(), dict()

    texts[keys[0]], scores[keys[0]] = remove_unavailable(texts_train, scores_train)
    texts[keys[1]], scores[keys[1]] = remove_unavailable(texts_dev, scores_dev)
    texts[keys[2]], scores[keys[2]] = remove_unavailable(texts_devtest, scores_devtest)

    data, W, _ = build_keras_input(texts, scores, test, new=True)
    exit()
    '''
    vocabulary_size, dims = W.shape
    print("Vocabulary_size, dims = %s, %s."%W.shape)

    X_train, X_valid, X_test, Y_train, Y_dev, Y_test = data
    print(len(X_train), ' train sequences')
    print(len(X_valid), ' valid sequences')
    print(len(X_test), ' test sequences')

    print("Pad sequences (samples x time)")
    X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
    X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
    X_valid = sequence.pad_sequences(X_valid, maxlen=maxlen)
    print('X_train shape:', X_train.shape)
    print('X_valid shape:', X_valid.shape)
    print('X_test shape:', X_test.shape)

    # Convert the sentiment scores from [-2, 2] to [0, 1]
    Y_train = (np.array(Y_train)+2)/2
    Y_dev = (np.array(Y_dev)+2)/2
    Y_test = (np.array(Y_test)+2)/2

    batch_size = 8

    model = cnn(W)

    model.compile(loss='mse', optimizer='adagrad')  # loss function: mse
    print("Train...")
    early_stopping = EarlyStopping(monitor='val_loss', patience=5)
    result = model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=10, validation_data=(X_valid, Y_dev),
              callbacks=[early_stopping])

    score = model.evaluate(X_test, Y_test, batch_size=batch_size)
    print('Test score:', score)

    # experiment evaluated by multiple metrics
    predict = model.predict(X_test, batch_size=batch_size).reshape((1, len(X_test)))[0]
    print('Y_test: %s' %str(Y_test))
    print('Predict value: %s' % str(predict))

    from metrics import continuous_metrics
    continuous_metrics(Y_test, predict, 'prediction result:')

    # visualization
    from visualize import draw_linear_regression

    X = range(50, 100)  # or range(len(y_test))
    draw_linear_regression(X, np.array(Y_test)[X], np.array(predict)[X], 'Sentence Number', "Sentiment scores",
                           'Comparison of predicted and true scores')

    from visualize import draw_hist

    # plot_keras(result, x_labels='Epoch', y_labels='Loss')
    draw_hist(np.array(Y_test) - np.array(predict), title='Histogram of sentiment scores prediction: ')

    '''
if __name__ == "__main__":
    build_ordinal_regression_input()
