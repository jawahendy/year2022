def viralAdvertising(n):
    # Write your code here
    PeopleAdvertised=5
    
    totPeopleLiked = 0
    for day in range(n):
        PeopleLiked = PeopleAdvertised//2
        totPeopleLiked += PeopleLiked
        PeopleAdvertised = PeopleLiked*3
        
        
    return totPeopleLiked