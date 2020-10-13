import json
import sys

class AddMember():
    def addMembers(self, new_members_list):
        try:
            # Here we are trying to open the json and appending the data to the already existing list.
            # if there is no list at all, it will raise and exception and the list will be initiated
            with open('a.json') as f:
                data = json.load(f)

            for member in new_members_list:
                data['members'].append(member)

            with open('a.json', 'w')  as w:
                json.dump(data, w)

            print("Added the new members", " ".join(new_members_list))
        except:
            from InitiateList import InitiateList

addMember = AddMember()
addMember.addMembers(sys.argv[1:])

'''
This class is to add new members to JSON. This will append the list to the exisiting list.
The command is as follows:
python AddMember.py e f g
If you did not initiate the list already, and attempt to add new members, it will initiate the list.

'''
