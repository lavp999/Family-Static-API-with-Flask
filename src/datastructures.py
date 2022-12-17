
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list 
"""
from random import randint
from flask import jsonify

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{"id": self._generateId(),
                        "first_name": "John",
                        "last_name": self.last_name,
                        "age": 33,
                        "lucky_members": [7, 13, 22]},
                        {"id": self._generateId(),
                        "first_name": "Jane",
                        "last_name": self.last_name,
                        "age": 35,
                        "lucky_members": [10, 14, 3]},
                        {"id": self._generateId(),
                        "first_name": "Jimmy",
                        "last_name": self.last_name,
                        "age": 5,
                        "lucky_members": [1]}
                        ]
 
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if member["age"] > 0:
            miembro = { "id": self._generateId(),
                        "first_name": member["first_name"],
                        "last_name": self.last_name,
                        "age": member["age"],
                        "lucky_members": member[1,2]}

            self._members.append(miembro)
            return {"miembro": miembro, "msg":"Creación con éxito"}
        else:
            return {"miembro": {},"msg":"error en la creación"}

    def delete_member(self, id):
        pos = -1
        aux = 0

        for e in self._members:
            print(e["id"])
            if e["id"] == id:
                pos = aux
                miembro = e
            aux += 1

        if pos != -1:
            self._members.pop(pos)
            return {"miembro": miembro, "msg":"Miembro " + miembro["first_name"]+ " Eliminado"}
        else:
            return {"miembro": {},"msg":"No existe el miembro: "+ str(id)}


    def get_member(self, id):
        members = self.get_all_members()

        for e in members:
            if e["id"] == id:  # e['first_name'] == "Luis": 
                return e

        return {}

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
