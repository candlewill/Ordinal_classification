import csv

import numpy as np


def load_vader(filename):
    with open(filename, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        texts, ratings = [], []
        for line in reader:
            texts.append(line[2])
            ratings.append(float(line[1]))
    return texts, ratings


def data_vader():
    texts, ratings = load_vader("./resources/tweets.txt")
    ratings = np.array(ratings) / 1.5
    print(np.min(ratings), np.max(ratings))
    return texts, ratings.tolist()


def additional():
    texts, ratings = data_vader()
    return texts, ratings


if __name__ == "__main__":
    texts, ratings = additional()
    print(type(ratings), ratings)
    for i in texts:
        print(i)
