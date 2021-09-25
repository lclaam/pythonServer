import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/decoder', methods=['POST'])
def decoder():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
#     values = data.get("possible_values")
#     num = data.get("num_slots")
#     answer = [values[0] for _ in range(num)]
#     result = {
#         "answer": answer
#     }
    inputValue = data.get("input")
    result = inputValue
    logging.info("My result :{}".format(result))
    return json.dumps(result)
