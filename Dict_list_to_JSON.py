# Microservice A -Anthony Parsons. Outline in Readme.md
import zmq
import json
from pathlib import Path

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5560")
print('Starting Service...')
while True:
    #  Wait for next request from client
    message = socket.recv_pyobj()
    if message == "exit":
        print('Exiting Service...')
        break
    socket.send_string("Received list of dictionaries")
    print('Received list of dictionaries')
    filename = socket.recv_string()
    print(f'Received file name {filename}...')
    current_dir = Path.cwd()
    current_dir.joinpath(filename)
    with open(filename, "w") as json_file:
        json.dump(message, json_file, indent=4)
    socket.send_string(f"File Location {current_dir}")
    
    
socket.close()