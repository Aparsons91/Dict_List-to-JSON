# Author: Nathan Sipe
# GitHub username: sipenp
# Date: 
# Description:
import time

# Import:
import zmq
import json
from pathlib import Path
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5560")

# Functions:
def main():
    list_dict = {
        'letters': [
        {'a': 1},
        {'b': 2},
        {'c': 3}
        ],
        'numbers': [
            {'1': 'a'},
            {'2': 'b'},
            {'3': 'c'}
            ] }

    socket.send_pyobj(list_dict)
    response = socket.recv()
    print(f'Received reply {response}')
    socket.send_string("Test_JSON.json")
    filepath = socket.recv()
    print(f'Received reply: {filepath}')
    time.sleep(1)
    with open('Test_JSON.json', 'r') as json_file:
        data = json.load(json_file)

    print(data)
    print(json.dumps(data, indent=4))
    socket.send_pyobj('exit')




# Main:

if __name__ == '__main__':
    main()
