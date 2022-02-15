def saveThePrisoner(n, m, s):
    # Write your code here
    ans = (s+m-1)%n
    if ans==0:
        return n
    return ans