def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b:
        return -1
    possibleBuys = [i+j for i in keyboards for j in drives if i+j<=b]
    
    return max(possibleBuys)