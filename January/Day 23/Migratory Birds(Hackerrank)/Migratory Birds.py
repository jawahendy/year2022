def migratoryBirds(arr):
    # Write your code here
    count = [0] * 6
    for i in arr:
        count[i] += 1
    return count.index(max(count))