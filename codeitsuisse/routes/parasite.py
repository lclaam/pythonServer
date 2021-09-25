import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

def infect2(x,y,maze,ans,count):
    count+=1
    # move up
    if (maze[x-1][y] == 1):
        # print("moving up")
        maze[x-1][y] = 3
        if (ans[x-2][y-1] == -1):
            ans[x-2][y-1] = count
        else:
            ans[x-2][y-1] = min(count,ans[x-2][y-1])
        infect2(x-1,y,maze,ans,count)
    # move down
    if (maze[x+1][y] == 1):
        # print("moving down")
        maze[x+1][y] = 3
        if (ans[x][y-1] == -1):
            ans[x][y-1] = count
        else:
            ans[x][y-1] = min(count,ans[x][y-1])
        infect2(x+1,y,maze,ans,count)

    # move left 
    if (maze[x][y-1] == 1):
        # print("moving down")
        maze[x][y-1] = 3
        if (ans[x-1][y-2] == -1):
            ans[x-1][y-2] = count
        else:
            ans[x-1][y-2] = min(count,ans[x-1][y-2])
        infect2(x,y-1,maze,ans,count)

    # move right
    if (maze[x][y+1] == 1):
        # print("moving down")
        maze[x][y+1] = 3
        if (ans[x-1][y] == -1):
            ans[x-1][y] = count
        else:
            ans[x-1][y] = min(count,ans[x-1][y])
        infect2(x,y+1,maze,ans,count)
    return 0

@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input")
    result = []
    for r in data:
        room = r['room']
        grid = r['grid']
        interested = r["interestedIndividuals"]
        infected = []
        ans = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        grid_len = len(grid[0])
        for i in range(len(grid)):
            for j in range(grid_len):
                # ans[i][j] = 0
                if (grid[i][j] == 3):
                    infected.append([i+1,j+1])
                    ans[i][j] = 0
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
            p1[i] = ans[int(i[0])][int(i[2])]
            # print(ans[int(i[0])][int(i[2])])
        # for i in ans:
        #     print(i)
        # for i in grid:
        #     print(i)

        current = {
            "room": room,
            "p1": p1,
            "p2": -1,
            "p3": -1,
            "p4": -1
        }
        result.append(current)
#     result = "Hello"
    logging.info("My result :{}".format(result))
    return json.dumps(result)



