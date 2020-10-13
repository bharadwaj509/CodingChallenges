import json
import sys

class InitiateList():
    def __init__(self, members):
        # created a dictionary here and added the members we read from command line to the dictionary
        data = {}
        data['members']  = members

        # dumping into json
        with open('a.json', 'w')  as w:
            json.dump(data, w)            
        print("List is initiated with members", " ".join(members))


'''
here the code is taking the arguments from the command prompt and initiating the json file
everytime we call this file, it will re-set the json file. So calling it once would suffice
python InitiateList.py a b c
The above command would create the data in json file.
{"members": ["a", "b", "c"]}
'''
initiate = InitiateList(sys.argv[1:])
