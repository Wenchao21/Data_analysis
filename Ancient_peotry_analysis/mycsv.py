import csv

import redis

import jieba.posseg

pool = redis.ConnectionPool(host="127.0.0.1", port=6379)

r = redis.Redis(connection_pool=pool, db=2)


decade = []
title = []
author_name = []
with open('result.csv') as f:
    reader = csv.reader(f)
    for wordCount in reader:
        decade.append(wordCount[0])
        title.append(wordCount[2])
        author_name.append(wordCount[3])


New_title = set(decade)
New_title.remove('author_decade')

list22 = list(New_title)
num = len(New_title)
print("All: %s, total: %s" % (list22, num))

countSong = 0

for i in range(0, len(New_title)-1):
    for j in range(0, len(decade)-1):
        if str(decade[j]) == str(list22[i]):
            countSong = countSong + 1

print(countSong)
seg_list = jieba.cut(str(wordCount[0]), cut_all=False)
print("/".join(seg_list))
string1 = string1 + str("/".join(seg_list))

# 词频分析

tags = jieba.analyse.extract_tags(string1, topK=100)
print(tags)
print(','.join(seg_list))


words = jieba.posseg.cut(string1)


for i in words:
    print(i.word)
    print(i.flag)
