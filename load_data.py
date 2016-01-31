import csv
import pickle
import gensim
import codecs


def load_SemEval(filename, type='gold'):
    # type values: "gold", "input"
    if type == 'gold':
        topic_col, score_col, text_col = 1, 2, 3
    elif type == 'input':
        topic_col, text_col = 1, 2
    else:
        raise Exception('Wrong parameter value for type.')

    topics, scores, texts = [], [], []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        for line in reader:
            topics.append(str(line[topic_col]))
            texts.append(str(line[text_col]))

            if type == 'gold':
                scores.append(float(line[score_col]))

    return topics, scores, texts


def load_pickle(filename):
    out = pickle.load(open(filename, "rb"))
    return out


def load_embeddings(filename, binary=False):
    model = gensim.models.Word2Vec.load_word2vec_format(filename, binary=binary)
    w2v = dict()
    for key in model.vocab.keys():
        w2v[key] = model[key]
    return w2v


# convert the GloVe format word vectors to word2vec format in order to use gensim's loading method
def vector_convert(filename, postfix='.w2v'):
    with open(filename, 'r', encoding='utf-8') as input_f:
        reader = input_f.readlines()
        l = len(reader)
        print("The vocabulary size is： %s." % l)
        dim = len(reader[0].replace("\n", "").split()[1:])
        print("The dimension of word vectors is： %s" % dim)
        with open(filename + postfix, 'w', encoding='utf-8') as output_f:
            header = str(l) + " " + str(dim) + "\n"
            output_f.write(header)
            for line in reader:
                output_f.write(line)
    print("Converting finished!")


# vector_convert("/home/hs/Data/Word_Embeddings/glove.840B.300d.txt")
# exit()

if __name__ == '__main__':
    topics, scores, texts = load_SemEval("./resources/full_tweets/train_gold.tsv")
    i = 1898
    print(texts[i - 1], topics[i - 1], scores[i - 1])
    print(len(texts))
