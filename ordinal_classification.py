from string import punctuation
from load_data import load_SemEval
import re
from collections import defaultdict
import numpy as np
import os
from load_data import load_pickle, load_embeddings
from save_data import dump_picle

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

        if i % 500 == 0:      # display maping method in every 500 words
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

def build_keras_input(texts, scores):
    filename_data, filename_w = './tmp/indexed_data.p', './tmp/Weight.p'

    if os.path.isfile(filename_data) and os.path.isfile(filename_w):
        data = load_pickle(filename_data)
        W = load_pickle(filename_w)
        print('Use existing data. Load OK.')
        return (data, W)

    print("Construct new data.")
    # load data from pickle

    vocab = get_vocab(texts)

    # using word2vec vectors
    # word_vecs = load_embeddings('google_news', '/home/hs/Data/Word_Embeddings/google_news.bin')
    word_vecs = load_embeddings('D:/Word_Embeddings/glove.840B.300d.txt.w2v')

    word_vecs = add_unknown_words(word_vecs, vocab)
    W, word_idx_map = build_embedding_matrix(word_vecs, vocab)

    idx_data = make_idx_data(texts, word_idx_map)

    data = (idx_data, scores)

    dump_picle(data, filename_data)
    dump_picle(W, filename_w)
    return (data, W)

topics, scores, texts = load_SemEval("./resources/full_tweets/train_gold.tsv")
for i in texts:
    print(clean_str(i))
