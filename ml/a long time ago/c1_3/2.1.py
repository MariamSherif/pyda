import re

from numpy import zeros
from scipy.spatial.distance import cosine
from collections import Counter


with open('sentences.txt', 'r') as infile:
    data = map(
        lambda row: filter(
            lambda item: item, re.split('[^a-z]', row.lower())
        ), infile
    )


indexs = list(set(reduce(lambda a, b: a + b, data)))
matrix = zeros((len(data), len(indexs)))


for i in range(len(data)):
    cnt = Counter(data[i])
    for j, word in enumerate(indexs):
        matrix[i, j] = cnt.get(word, 0)

result = sorted(list(enumerate(cosine(matrix[0], matrix[i]) for i in range(len(data)))), key=lambda item: item[1])

with open('task1.txt', 'w') as answ:
    answ.write('%d %d' % tuple(item[0] for item in result[1:3]))
