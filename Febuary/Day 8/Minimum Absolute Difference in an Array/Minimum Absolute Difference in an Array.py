def minimumAbsoluteDifference(arr):
    # Write your code here
    arr.sort()
    min_dif = abs(arr[0] - arr[1])
    for i in range(len(arr)-1):
        dif = abs(arr[i] - arr[i+1])
        if dif < min_dif:
            min_dif = dif
    return min_dif