def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    res = 0

    while s > 0:
        res += 1
        s -= p
        p = max(p - d, m)

    if s != 0:
        res -= 1

    return res
