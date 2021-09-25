import logging
import json
from copy import deepcopy

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def infect2(x,y,maze,ans,count):
    count+=1
    c2,c3,c4 = count, count, count
    m2 = deepcopy(maze)
    # move up
    if (maze[x-1][y] == 1):
        # print("moving up")
        maze[x-1][y] = 3
        if (ans[x-2][y-1] == -2):
            ans[x-2][y-1] = count
        else:
            ans[x-2][y-1] = min(count,ans[x-2][y-1])
        infect2(x-1,y,maze,ans,count)
    # move down
    if (m2[x+1][y] == 1):
        # print("moving down")
        m2[x+1][y] = 3
        if (ans[x][y-1] == -2):
            ans[x][y-1] = c2
        else:
            ans[x][y-1] = min(count,ans[x][y-1])
        infect2(x+1,y,m2,ans,c2)
    
    # move left 
    if (m2[x][y-1] == 1):
        # print("moving left")
        m2[x][y-1] = 3
        if (ans[x-1][y-2] == -2):
            ans[x-1][y-2] = c3
        else:
            ans[x-1][y-2] = min(count,ans[x-1][y-2])
        infect2(x,y-1,m2,ans,c3)

    # move right
    if (m2[x][y+1] == 1):
        # print("moving right")
        m2[x][y+1] = 3
        if (ans[x-1][y] == -2):
            ans[x-1][y] = c4
        else:
            ans[x-1][y] = min(count,ans[x-1][y])
        infect2(x,y+1,m2,ans,c4)
    return maze

@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = []
    for r in data:
        room = r['room']
        if (room > 7):
            current = {
                "room": room,
                "p1": -1,
                "p2": -1,
                "p3": -1,
                "p4": -1
            }
            break
        grid = r['grid']
        interested = r["interestedIndividuals"]
        infected = []
        ans = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        grid_len = len(grid[0])
        for i in range(len(grid)):
            for j in range(grid_len):
                # ans[i][j] = 0
                if (grid[i][j] == 1):
                    ans[i][j] = -2
                elif (grid[i][j] == 3):
                    infected.append([i+1,j+1])
            grid[i].insert(0,-1)
            grid[i].append(-1)

        # add boundary
        temp = [-1 for _ in range(len(grid[0]))]
        grid.insert(0,temp)
        grid.append(temp)
        for i in infected:
            infect2(i[0],i[1],grid,ans,0)
            # if (len(infected) == 1):
            #     infect(i[0],i[2],infected[0][0],infected[0][1],grid)

            # print(i)
        # solve()
        # print(grid)
        
        p1 = {}
        for i in interested:
            # p1[i] = ans[i[0],i[1]]
            p = i.split(',')
            p1[i] = ans[int(p[0])][int(p[1])]

        p2 = -1
        b = False
        for i in ans:
            for j in i:
                if (j == -2):
                    b = True
                    break
            if (max(i) > p2):
                p2 = max(i)
        if (b):
            p2 = -1

        current = {
            "room": room,
            "p1": p1,
            "p2": p2,
            "p3": -1,
            "p4": -1
        }
        result.append(current)
    logging.info("My result :{}".format(result))
    return json.dumps(result)



