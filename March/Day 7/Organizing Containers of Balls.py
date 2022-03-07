def organizingContainers(container):
    caps = []
    for i in range(len(container)):
        caps.append( sum(container[i]) )
    #print(caps)

    typenums = []
    for i in range(len(container)):
        n = 0
        for j in range(len(container)):
            n += container[j][i]
        typenums.append(n)
    
    if sorted(caps) == sorted(typenums):
        return 'Possible'
    else:
        return 'Impossible'
