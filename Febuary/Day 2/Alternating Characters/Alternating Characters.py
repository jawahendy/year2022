def alternatingCharacters(s):
    # Write your code here
    dele = 0

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dele += 1

    return dele