def beautifulTriplets(d, arr):
    # Write your code here
    res = 0
    
    for el in arr:
        if el + d in arr and el + 2*d in arr:
            res += 1
            
    return res