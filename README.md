# Apartment List Coding Test

## InitiateList.py

The code will take the arguments from the command prompt and will initiate the json file.<br>
Everytime we call this file, it will re-set the json file. So calling it once would suffice.<br>
command : <i>python InitiateList.py a b c</i><br>
The above command would create the data in json file.<br>
<i>{"members": ["a", "b", "c"]}</i><br>

## AddMember.py

This class is to add new members to JSON. This will append the list to the exisiting list.<br>
The command is as follows:<br>
<i>python AddMember.py e f g</i><br>
If you did not initiate the list already, and attempt to add new members, it will initiate the list.<br>

## ShuffleGroups.py

This will reshuffle the already existing members. If there are members, it will prompt a message. The command is as follow.<br>
<i>python ShuffleGroups.py</i><br>

