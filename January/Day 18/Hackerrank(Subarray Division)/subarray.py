from functools import reduce

def add(a, b): # function to add elements in our subarray
  return a + b

def birthday(s, d, m):
  counter = 0
  for i in range(len(s)): # loop through array S
    temp_list = s[i:i+m] # create subarray of length M
    if reduce(add, temp_list) == d: # if elements in subarray add up to D
      counter += 1
  return counter