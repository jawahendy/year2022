def jumpingOnClouds(c, k):
    cur = k % n
    energy = 100 - 1 - c[cur]*2
    
    while cur != 0:
        cur = (cur + k) % n
        energy -= 1 + c[cur]*2
        
    return energy