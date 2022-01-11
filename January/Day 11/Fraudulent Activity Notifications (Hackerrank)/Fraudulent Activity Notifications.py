def activityNotifications(expenditure, d):
    # Write your code here
    total = 0
    for i in range(d, len(expenditure)):
        days = expenditure[i-d:i]
        arr = sorted(days)
        if d%2 != 0:
            median = arr[(d+1)//2 - 1]
        else:
            median = (arr[(d)//2 - 1] + arr[(d+1)//2])/2
        if expenditure[i] >= 2 * median:
            total +=1
    return total
