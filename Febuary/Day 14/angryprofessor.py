def angryProfessor(k, a):
    s = 0 
    for i in a:
        if i<1:
            s+=1
    return "YES" if s<k else "NO"