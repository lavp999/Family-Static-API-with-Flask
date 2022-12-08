"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure 
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def getMembers():
    jackson_family.add_member({"first_name": "Luis", "last_name": "otra familia", "age": 55, "lucky_members": [1,2]})
    jackson_family.add_member({"first_name": "Luis2", "last_name": "otra familia", "age": 5, "lucky_members": [3,2]})
           
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }

    return jsonify(response_body), 200


@app.route('/members/<int:id>', methods=['GET'])
def getMember(id):
    jackson_family.add_member({"first_name": "Luis", "last_name": "otra familia", "age": 55, "lucky_members": [1,2]})
    jackson_family.add_member({"first_name": "Luis2", "last_name": "otra familia", "age": 5, "lucky_members": [3,2]})

    miembro = jackson_family.get_member(id)
    if miembro:
        return jsonify(miembro) , 200

    return {"msg":"No se ha encontrado al miembro "+str(id)}, 404 


@app.route('/member', methods=['POST'])
def postMember():
    data = request.json
    res = jackson_family.add_member(data)

    if res["miembro"]:
        return jsonify(res["miembro"]) , 200

    return jsonify({"msg":"NO se ha agregado con éxito al miembro "+str(data["first_name"])+" - "+res["msg"]}), 404 



@app.route('/member/<int:id>', methods=['DELETE'])
def deleteMember(id):
    res = jackson_family.delete_member(id)
    if res["miembro"]:
        return jsonify(res["miembro"]) , 200

    return jsonify({"msg":res["msg"]}), 404 




# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)