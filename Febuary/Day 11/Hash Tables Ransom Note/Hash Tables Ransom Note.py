def checkMagazine(magazine, note):
    # Write your code here
    d1 = {}
    for word in magazine:
        d1[word] = d1.get(word,0) + 1
    for word in note:
        if d1.get(word,0) == 0:
            print('No')
            return
        else:
            d1[word] -= 1
    print('Yes')