def cutTheSticks(arr):
    # Write your code here
    out = []
    while arr:
        out.append(len(arr))
        arr_min = min(arr)
        arr = list(map(lambda x: x - arr_min, arr))
        arr = list(filter(lambda x: x > 0, arr))
        
        
    return out