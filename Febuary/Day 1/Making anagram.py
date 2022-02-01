from collections import Counter


def makeAnagram(a, b):
    # Write your code here
    count_a = Counter(a)
    count_b = Counter(b)

    difference_a = count_a - count_b
    difference_b = count_b - count_a

    return sum(difference_a.values()) + sum(difference_b.values())