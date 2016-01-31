import csv

from load_data import load_pickle

(test, submit_predict) = load_pickle("./tmp/submit.p")
ids, topics, texts = test

ratings = []
for score in submit_predict:
    if score > 0.75:
        s = 2
    elif score

for t in texts:
    print(t)

with open("./tmp/submit.csv", 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for i in range(len(ids)):
        w.writerow([ids[i], topics[i], submit_predict[i]])
