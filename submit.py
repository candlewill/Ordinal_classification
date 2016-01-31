import csv
import time
from load_data import load_pickle

(test, submit_predict) = load_pickle("./tmp/submit.p")
ids, topics, texts = test

ratings = []
for score in submit_predict:
    if score > 0.875:
        s = 2
    elif score > 0.625:
        s = 1
    elif score > 0.375:
        s = 0
    elif score > 0.125:
        s = -1
    else:
        s = -2
    ratings.append(s)

for t in texts:
    print(t)

timestr = time.strftime("%Y%m%d-%H%M%S")
print("File saved to: " % timestr)

with open("./tmp/submit" + str(timestr) + ".csv", 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t')
    for i in range(len(ids)):
        w.writerow([ids[i], topics[i], ratings[i]])