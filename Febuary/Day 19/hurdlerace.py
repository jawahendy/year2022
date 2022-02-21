def hurdleRace(k, height):
    maxi = max(height)
    if(maxi>k):
        return maxi-k
    return 0