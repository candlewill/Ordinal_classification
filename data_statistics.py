import numpy as np


def SemEval_statistics(topics, scores, texts):
    # data type: list
    size = len(texts)
    print("size: %s" % len(texts))
    nb_unavailable_text = 0
    for i in texts:
        if i == "Not Available":
            nb_unavailable_text += 1
    print("Number of Unavailable Texts: %s, number of available text: %s (%s)" % (
    nb_unavailable_text, size - nb_unavailable_text, (size - nb_unavailable_text) / size))
    nb_topics = len(set(topics))
    print("number of topics: %s" % nb_topics)

    score_set = [-2, -1, 0, 1, 2]
    for score in score_set:
        print("number of texts in score=%s: %s" % (score, scores.count(float(score))))

    texts_len = []
    for text in texts:
        texts_len.append(len(text.split()))
    texts_len = np.array(texts_len)
    max_Length = np.max(texts_len)
    min_Length = np.min(texts_len)
    average_Length = np.mean(texts_len)
    print("Max Length: %s, Min Length: %s, Average Length: %s" % (max_Length, min_Length, average_Length))


if __name__ == "__main__":
    filenames = ["dev_gold.tsv", "", "",""]