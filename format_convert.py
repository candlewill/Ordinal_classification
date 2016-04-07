def devtest_gold(filename, gold_filename):
    topics, ratings = [], []
    with open(filename, 'r') as f:
        for line in f:
            a = line.split('\t')
            if a[3] != 'Not Available\n':
                topics.append(a[1])
                ratings.append(a[2])
    with open(gold_filename, 'w') as of:
        for i, topic, rating in zip(range(len(topics)), topics, ratings):
            of.write(str(i + 1) + '\t' + topic + '\t' + rating + '\n')


devtest_gold('./resources/full_tweets/devtest_gold.tsv', './resources/devtest_gold_FILE.tsv')
