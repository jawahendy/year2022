def minimumDistances(a):
    # Write your code here
    res = -1
    memo = [-1] * (10**5 + 3)
    
    for ind, el in enumerate(a):
        if memo[el] >= 0:
            res = min(res if res >= 0 else 10**5 + 2, ind - memo[el])
        memo[el] = ind
        
    return res
