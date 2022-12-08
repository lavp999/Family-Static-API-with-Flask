
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

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        miembro = { "id": self._generateId(),
                    "first_name": member.first_name,
                    "last_name": self.last_name,
                    "age": member.age,
                    "lucky_members": member.lucky_members
                  }
        # member['id'] = self._generateId()
        self._members.append(miembro)

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


member = [
            {"name": "luis",
             "age": 25,
             "cargo": "Jefe 1",
             "members": [{"nombre": "Juan",
                          "age": 24,
                          "cargo": "subjefe",
                          "members": [{"nombre": "pedro",
                                      "age": 23,
                                        "cargo": "empleado",
                                        "members": []} 
                                     ]  
                         }]
            },
            {"nombre": "Juan1",
             "age": 24,
             "cargo": "subjefe",
             "members": [{"nombre": "pedro1",
                          "age": 23,
                          "cargo": "empleado",
                          "members": []}
                        ]
            }
         ]

family = FamilyStructure("mi familia")
family.add_member(member)
family.add_member({"name": "luis1","age": 25,"cargo": "Jefe 1","members": []})
family.add_member({"name": "luis2","age": 25,"cargo": "Jefe 1","members": []})
print (family.last_name)
print(family._members)
