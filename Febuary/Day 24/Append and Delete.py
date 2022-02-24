def appendAndDelete(s, t, k):
    # Write your code here
    start = 0
    ind = 0
    to_del = 0
    to_app = 0
    
    while ind < len(s) and ind < len(t) and s[ind] == t[ind]:
        ind += 1
    start = ind
    
    if start < len(s):
        to_del = len(s[start:])
        if to_del == len(s) and k - to_del >= len(t):
            return 'Yes'
    if start < len(t):
        to_app = len(t[start:])
    k -= to_del + to_app
    if k == 0 or (k > 0 and k % 2 == 0) or k >= 2*len(t):
        return 'Yes'
    else:
        return 'No'
