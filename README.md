# Dict_List-to-JSON
To use this program, run the python file. It will continue to run until told to exit
Send a list of dictionaries as demonstrated in the pseudocode below.
Then await a response and send a followup filename.
The program will create a JSON file with that filename in the same directory where it is located.
It will then return the filepath to the new file.

list_of_dicts = [dict1, dict2,..dict(n)]

socket.send_pyobj(list_of_dicts)
response = socket.recv() #receives string response confirming initial object received

socket.send_string("Desired_filename.json")
filepath_to_json = socket.recv()

To end service:
socket.send_pyobj("exit")
