def queensAttack(n, k, r_q, c_q, obstacles):
    tot_tiles = 0

    direction = [[1,1],[1,0],[0,1],[-1,-1],[-1,0],[0,-1],[-1,1],[1,-1]]
    blocked = 0

    obs = {}


    if(obstacles): 
        for ob in obstacles:
            obs[ob[0],ob[1]] = 1

    for move in direction:
        i, j = r_q, c_q
        i += move[0]
        j += move[1]
        while(i<=n and j<=n and i>0 and j>0):
            
            if((i,j) in obs):
                break
            else:
                tot_tiles += 1
            i += move[0]
            j += move[1]

    return tot_tiles