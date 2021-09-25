import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

# def infect2(x,y,maze,ans,count):
#     count+=1
#     # move up
#     if (maze[x-1][y] == 1):
#         # print("moving up")
#         maze[x-1][y] = 3
#         if (ans[x-2][y-1] == -1):
#             ans[x-2][y-1] = count
#         else:
#             ans[x-2][y-1] = min(count,ans[x-2][y-1])
#         infect2(x-1,y,maze,ans,count)
#     # move down
#     if (maze[x+1][y] == 1):
#         # print("moving down")
#         maze[x+1][y] = 3
#         if (ans[x][y-1] == -1):
#             ans[x][y-1] = count
#         else:
#             ans[x][y-1] = min(count,ans[x][y-1])
#         infect2(x+1,y,maze,ans,count)

#     # move left 
#     if (maze[x][y-1] == 1):
#         # print("moving down")
#         maze[x][y-1] = 3
#         if (ans[x-1][y-2] == -1):
#             ans[x-1][y-2] = count
#         else:
#             ans[x-1][y-2] = min(count,ans[x-1][y-2])
#         infect2(x,y-1,maze,ans,count)

#     # move right
#     if (maze[x][y+1] == 1):
#         # print("moving down")
#         maze[x][y+1] = 3
#         if (ans[x-1][y] == -1):
#             ans[x-1][y] = count
#         else:
#             ans[x-1][y] = min(count,ans[x-1][y])
#         infect2(x,y+1,maze,ans,count)
#     return 0


@app.route('/parasite', methods=['POST'])
def parasite():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    inputValue = data.get("input")
    result = inputValue
    logging.info("My result :{}".format(result))
    return json.dumps(result)



