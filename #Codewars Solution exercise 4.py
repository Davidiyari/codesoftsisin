#Codewars Solution exercise 4
from collections import Counter

def duplicate_or_unique(arr):
    c = Counter(arr)
    n = len(c)
    length = len(arr)
    if length == n + 1:
        for k, v in c.items():
            if v == 2:
                return k
    if length == 2 * n - 1:
        for k, v in c.items():
            if v == 1:
                return k