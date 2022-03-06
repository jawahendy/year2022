def taumBday(b, w, bc, wc, z):
    res = 0
    
    if bc <= wc:
        res += bc*b
        if bc + z <= wc:
            res += (bc + z)*w
        else:
            res += wc*w
    else:
        res += wc*w
        if wc + z <= bc:
            res += (wc + z)*b
        else:
            res += bc*b
        
    return res