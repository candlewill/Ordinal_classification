import numpy as np
from load_data import load_SemEval

def SemEval_statistics(topics, scores, texts):
    # data type: list
    size = len(texts)
    print("size: %s" % len(texts))
    nb_unavailable_text = 0
    unavailable_mark = "Not Available"

    for i in texts:
        if i == unavailable_mark:
            nb_unavailable_text += 1
    print("Number of Unavailable Texts: %s, number of available text: %s (%s)" % (
    nb_unavailable_text, size - nb_unavailable_text, (size - nb_unavailable_text) / size))
    nb_topics = len(set(topics))
    print("number of topics: %s" % nb_topics)
    print("Topics: %s" % str(sorted(set(topics))))

    score_set = [-2, -1, 0, 1, 2]
    for score in score_set:
        print("number of texts in score=%s: %s" % (score, scores.count(float(score))))

    texts_len = []
    for text in texts:
        if text != unavailable_mark:
            texts_len.append(len(text.split()))
    texts_len = np.array(texts_len)
    max_Length = np.max(texts_len)
    min_Length = np.min(texts_len)
    average_Length = np.mean(texts_len)
    print("Max Length: %s, Min Length: %s, Average Length: %s" % (max_Length, min_Length, average_Length))


def common_topics():
    Train = ['@microsoft', 'ac/dc', 'amazon', 'amazon prime', 'amazon prime day', 'angela merkel', 'apple', 'apple watch', 'arsenal', 'barca', 'batman', 'bbc', 'bentley', 'bernie sanders', 'beyonce', 'bob marley', 'bobby jindal', 'chelsea', 'chris brown', 'conor mcgregor', 'david beckham', 'david cameron', 'digi', 'disneyland', 'donald trump', 'erdogan', 'eric church', 'federer', 'fleetwood mac', 'galaxy note', 'game of thrones', 'google', 'google+', 'grateful dead', 'hannibal', 'harper', 'harry potter', 'hillary', 'ibm', 'ihop', 'ios', 'ipad', 'iphone', 'ipod', 'jay-z', 'jeb bush', 'joe biden', 'jurassic park', 'jurassic world', 'justin', 'juventus', 'kerry', 'kurt cobain', 'labor day', 'lexus', 'madonna', 'magic mike xxl', 'mariah carey', 'messi', 'metlife']
    Dev = ['michael jackson', 'michelle obama', 'minecraft', 'monsanto', 'netflix', 'nike', 'nintendo', 'nokia', 'obama', 'oracle', 'planned parenthood', 'pope', 'pride parade', 'ric flair', 'rick perry', 'sarah palin', 'scotus', 'seinfeld', 'serena', 'snoop dogg']
    Devtest = ['sony', 'star wars', 'sting', 't-mobile', 'taylor swift', 'ted 2', 'teen wolf', 'tgif', 'tiger woods', 'tom cruise', 'tory', 'trump', 'tsipras', 'ukip', 'valentine', "valentine 's day", 'venice beach', 'windows 10', 'xbox', 'zlatan']

    print("Common terms between train and dev set, nb: %s, terms: %s"%(len(set(Train) & set(Dev)), sorted(set(Train) & set(Dev))))
    print("Common terms between train and devtest set, nb: %s, terms: %s"%(len(set(Train) & set(Devtest)), sorted(set(Train) & set(Devtest))))
    print("Common terms between dev and devtest set, nb: %s, terms: %s"%(len(set(Devtest) & set(Dev)), sorted(set(Devtest) & set(Dev))))

def testdata_statistics():
    filename = "./resources/TEST data/SemEval2016_Task4_test_datasets/SemEval2016-task4-test.subtask-BCDE.txt"
    topics, scores, texts = load_SemEval(filename)
    SemEval_statistics(topics, scores, texts)


if __name__ == "__main__":
    testdata_statistics()
    exit()
    filenames = ["dev_gold.tsv", "devtest_gold.tsv", "devtest_input.tsv","train_gold.tsv"]
    file_dir = "./resources/full_tweets/"

    for filename in filenames:
        print("------------------------- Filename: %s -------------------------" % filename)
        filename = file_dir + filename
        if "devtest_input.tsv" in filename:
            topics, scores, texts = load_SemEval(filename, "input")
        else:
            topics, scores, texts = load_SemEval(filename)
        SemEval_statistics(topics, scores, texts)

    common_topics()