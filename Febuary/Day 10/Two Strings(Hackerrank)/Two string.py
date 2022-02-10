def twoStrings(s1, s2):
    # Write your code here
    word1 = set(s1)
    word2 = set(s2)
    if set.intersection(word1,word2):
        return "YES"
    return "NO"