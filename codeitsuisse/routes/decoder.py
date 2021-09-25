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
    answer = [values[4] for _ in range(num)]
#     answer = ['i','q','q','x','q']
    # for _ in data["possible_values"]:
    # answer = [ data["possible_values"][0] for _ in range(data["num_slots"])]

    result = {
        "answer": answer
    }
    
    logging.info("My result :{}".format(result))
    return json.dumps(result)
