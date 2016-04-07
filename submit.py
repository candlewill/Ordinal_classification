import csv
import time

from load_data import load_pickle

(test, submit_predict) = load_pickle("./tmp/submit_cnn_valid.p")
ids, topics, texts = test
print(len(submit_predict))
exit()
ratings = []
cut_offs = [0.2, 0.4, 0.6, 0.8]
# cut_offs = [0.125, 0.375, 0.625, 0.875]

for score in submit_predict:
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
    ratings.append(s)

for t in texts:
    print(t)

timestr = time.strftime("%Y%m%d-%H%M%S")
path = "./tmp/submit" + str(timestr) + ".csv"

print(len(ids), len(topics), len(texts))
# exit()
with open(path, 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for i in range(len(ids)):
        w.writerow([ids[i], topics[i], ratings[i]])

print("File saved to: " + path)
