def isValid(s):
    # Write your code here
    cntr = Counter(s)
    res = 'NO'
    print("cnt = {} len = {}".format(cntr, len(set(cntr.values()))))

    if len(set(cntr.values())) == 1:
        res = 'YES'
    elif len(set(cntr.values())) == 2:
        bigger = max(cntr.values())
        lesser = min(cntr.values())
        bigger_let = [let for let, c in cntr.items() if c == bigger]
        lesser_let = [let for let, c in cntr.items() if c == lesser]

        if len(lesser_let) == 1 and lesser == 1:
            res = 'YES'
        elif len(bigger_let) == 1 or len(lesser_let) == 1:
            if abs(bigger-lesser) == 1:
                res = 'YES'
            else:
                res = 'NO'
        else:
            res = 'NO'
    else:
        res = 'NO'

    return res