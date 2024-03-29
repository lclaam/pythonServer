import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def decoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    values = data.get("possible_values")
    num = data.get("num_slots")
#     answer = [values[0],values[0],values[1],values[1],values[1]]
#     answer = [values[2],values[2],values[3],values[3],values[3]]
    answer = [values[4],values[4],values[5],values[5],values[5]]

#     answer = [values[4] for _ in range(num)]
#     answer = ['t','o','z','v','j']
    # for _ in data["possible_values"]:
    # answer = [ data["possible_values"][0] for _ in range(data["num_slots"])]

    result = {
        "answer": answer
    }
    
    logging.info("My result :{}".format(result))
    return json.dumps(result)
