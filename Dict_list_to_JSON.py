
import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv_pyobj()
    if message == "exit":
        break
    socket.send_string("Received list of dictionaries")
    filename = socket.recv_string()
    socket.send_string(f"Received filename {filename}")
    print(f"Received request: {message}")
    with open(filename, "w") as json_file:
        json.dump(message, json_file, indent=4)
    
socket.close()