import csv


def load_SemEval(filename, type='gold'):
    # type values: "gold", "input"
    if type == 'gold':
        topic_col, score_col, text_col = 1, 2, 3
    elif type == 'input':
        topic_col, text_col = 1, 2
    else:
        raise Exception('Wrong parameter value for type.')

    topics, scores, texts = [], [], []
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for line in reader:
            topics.append(str(line[topic_col]))
            texts.append(str(line[text_col]))

            if type == 'gold':
                scores.append(float(line[score_col]))

    return topics, scores, texts

if __name__ == '__main__':
    topics, scores, texts = load_SemEval("./resources/full_tweets/train_gold.tsv", "input")
    print(topics[:100])
