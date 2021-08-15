#Normalize each row of 2d array (list) to vary between 0 and 1.
#list_a = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25, 26]]

#!/usr/bin/python
# -*- coding: utf-8 -*-
import multiprocessing as mp

list_a = [[2, 3, 4, 5], [6, 9, 10, 12], [11, 12, 13, 14], [21, 24, 25,
          26]]


def normalize(mylist):
    mini = min(mylist)
    maxi = max(mylist)
    return [(i - mini) / (maxi - mini) for i in mylist]


pool = mp.Pool(mp.cpu_count())
results = [pool.apply(normalize, args=(l1, )) for l1 in list_a]
pool.close()
print results[:10]
