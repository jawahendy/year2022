import math
import os
import random
import re
import sys
import bisect as bs

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bs.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def median(a_sorted, days):
    half = len(a_sorted)//2
    
    if days % 2:
        median = a_sorted[half]
    else:
        median = (a_sorted[half-1] + a_sorted[half])/2
        
    return float(median)

def activityNotifications(log, days):
    # Write your code here

    heap = sorted(log[:days])
    res = 0
    med = 0
    to_del = 0
    
    for ind in range(days, len(log)):
        med = median(heap, days)
        #print("heap: {}".format(heap))
        #print("log[{}] = {} med = {}".format(ind, log[ind], med))
            
        if float(log[ind]) >= 2*med:
            res += 1
        
        #del heap[heap.index(log[to_del])]
        del heap[index(heap, log[to_del])]
        bs.insort(heap, log[ind])
        to_del += 1
            
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
