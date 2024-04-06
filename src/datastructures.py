
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        # example list of members
        self._members = [
            {
                "first_name": "John",
                "last_name": self.last_name,
                 "age": 33,
                  "lucky_numbers": [7,7,7],
                  "id": self._generateId()  
                      }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        member['last_name'] = self.last_name
        member['id'] = self._generateId
        self._members.append(member)

    def delete_member(self, id):
       for i, member in enumerate(self.members):
         if member['id'] == id:
            del self._members[i]
            break
    def update_member(self, id, new_member_data):
        for i, member in enumerate(self._members):
            if member['id'] == id:
                self._members[i] = new_member_data
                self._members[i]['id'] = id 
                break



    def get_member(self, id):
        for member in self._members:
            if member['id'] == id:
                return member
            return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
