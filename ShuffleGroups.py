import random
import json


class FridayLunch():

    def groupMembers(self, members, n):
        # Here we are identifying the number of groups in multiples of 3,4,5.
        # then we add the members from our json into those groups
        # for eg if we have 7 members, first create 2 groups and add 3 into each of those groups.
        num_groups = len(members) // n
        list_of_groups = []
        for i in range(num_groups):
            group = []
            for j in range(n):
                m = members.pop(0)
                group.append(m)
            list_of_groups.append(group)

        # This is to handle the remaining members.
        # So eariler out of 7 we added 6 members into 2 groups. And one member is remaining.
        # Now, we are taking that 1 member and adding it into the group. Thus it will take care of all the remaining numbers.
        # Thus each group will not be less than 3
        if len(members) >=3 and len(members)<=5:
            list_of_groups.append(members)

        return list_of_groups

    def reShuffle(self):
        # Here, we are trying to load the data.
        try:
            with open('a.json') as f:
                data = json.load(f)

            members = data['members']
            random.shuffle(members)

            # if there are no members, it will prompt a message.
            if len(members) == 0:
                return "There are no members in the group to arrage."

            # if there are less than 3 members, it will prompt a message
            if len(members) < 3:
                print("The total members we have are less than 3. They are grouped into 1. Please add more members to create groups of 3 to 5")
                return members
            else:
                ### The following will take care of random choices between a group or 5, 4 or 3 basing on the number of members
                if len(members) % 5 in [0,3] and len(members) % 4 == 0:
                    rand = random.randint(0,100)                    
                    if rand%2 == 0: return self.groupMembers(members, 5)
                    else: return self.groupMembers(members, 4)


                if len(members) % 5 in [0,4] and len(members) % 3 == 0:
                    rand = random.randint(0,100)
                    if rand%2 == 0: return self.groupMembers(members, 5)
                    else: return self.groupMembers(members, 3)

                if len(members) % 5 in [0,3,4]: return self.groupMembers(members, 5)

                if len(members) % 4 in [0,3]: return self.groupMembers(members, 4)

                if len(members) % 3 == 0: return self.groupMembers(members, 3)

        except:
            return "There are no members at all. Please add some members."


'''
This will reshuffle the already existing members. If there are members, it will prompt a message. The command is as follow.
python ShuffleGroups.py
'''
f = FridayLunch()
print(f.reShuffle())
