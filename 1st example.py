#Use Pool.apply() to get the row wise common items in list_a and list_b.
#list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
#list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing as mp

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]


def get_commons(list_1, list_2):
    return list(set(list_1).intersection(list_2))


pool = mp.Pool(mp.cpu_count())
results = [pool.apply(get_commons, args=(l1, l2)) for (l1, l2) in
           zip(list_a, list_b)]
pool.close()
print results[:10]
