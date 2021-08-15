#Use Pool.map() to run the following python scripts in parallel.
#Script names: ‘1.py’, ‘2.py’, ‘3.py’


#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import multiprocessing as mp

processes = ('1.py', '2.py', '3.py')


def run_python(process):
    os.system('python {}'.format(process))


pool = mp.Pool(processes=3)
pool.map(run_python, processes)
