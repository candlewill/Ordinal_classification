from load_data import load_pickle


def build_devtest_submit(gold, predict):
    out = []
    with open(gold) as gf:
        for line in gf:
            out.append(line)
    cut_offs = [0.2, 0.4, 0.6, 0.8]

    with open('./resources/predict_cnn_lstm.txt', 'w') as o:
        for i, line in enumerate(out):
            score = predict[i]
            if score > cut_offs[3]:
                s = 2
            elif score > cut_offs[2]:
                s = 1
            elif score > cut_offs[1]:
                s = 0
            elif score > cut_offs[0]:
                s = -1
            else:
                s = -2
            print(line[:-1], i, predict[i], s)
            o.write('\t'.join(line.split('\t')[0:2])+'\t'+str(s)+'\n')


(_, predict) = load_pickle("./tmp/submit_cnn_lstm.p")
gold = './resources/devtest_gold_FILE.tsv'
build_devtest_submit(gold, predict)