import random
import json


class FridayLunch():

    def reShuffle(self):
        # Here, we are trying to load the data.
        try:
            with open('a.json') as f:
                data = json.load(f)

            members = data['members']
            random.shuffle(members)

            # if there are no members, it will prompt a message.
            if len(members) == 0:
                print("There are no members in the group to arrage.")
                return
            # if there are less than 3 members, it will prompt a message
            if len(members) < 3:
                print("The total members we have are less than 3. They are grouped into 1. Please add more members to create groups of 3 to 5")
                return members
            else:
                # Here we are identifying the number of groups in the multiples of 3.
                # then we add the members from our json into those groups
                # for eg if we have 7 members, first create 2 groups and add 3 into each of those groups.

                num_groups = len(members) // 3

                list_of_groups = []
                for i in range(num_groups):
                    group = []
                    for j in range(3):
                        m = members.pop(0)
                        group.append(m)
                    list_of_groups.append(group)

                # This is to handle the remaining members.
                # So eariler out of 7 we added 6 members into 2 groups. And one member is remaining.
                # Now, we are taking that 1 member and adding it into the group. Thus it will take care of all the remaining numbers.
                # Thus each group will not be less than 3

                for i in range(len(members)):
                    list_of_groups[i].append(members[i])

                return list_of_groups
        except:
            return "There are no members at all. Please add some members."


'''
This will reshuffle the already existing members. If there are members, it will prompt a message. The command is as follow.
python ShuffleGroups.py
'''
f = FridayLunch()
print(f.reShuffle())
