def circularArrayRotation(a, k, queries):
    # Write your code here
    n=len(a)
    
    ans=[]
    for q in queries:
        ans.append(a[(n-k+q)%n])
        
    return ans