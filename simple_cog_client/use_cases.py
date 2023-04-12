import logging
from typing import List

import requests

from .processors import processors


def build_input_json(inputs: List[str]):
    """Input values as al list of key=value strings,
    e.g. ["image=foo.png", "text=bar"]
    The inputs keys must be a valid processor name.
    """
    input_json = {}
    for pair in inputs:
        name, value = pair.split('=')
        if name in processors:
            logging.info("Processing input %s" % name)
            value = processors[name].encode(value)
            input_json[name] = value
    return input_json

def send_request(url, input_json):
    payload = {
        "input": input_json,
        "id": "0",
        "created_at": "2020-01-01T00:00:00.000Z",
    }
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        logging.error(err)
        raise Exception("Error in request")
    else:
        logging.info("Successful request")
    output = dict(**response.json()["output"])
    for name, value in output.items():
        if name in processors:
            logging.info("Processing output %s" % name)
            output[name] = processors[name].decode(value)
    return output