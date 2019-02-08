from flask import make_response, jsonify, request, Blueprint
from app.v1.models.parties import PoliticalParty, parties

api = Blueprint('parties', __name__,  url_prefix='/api/v1/')

@api.route('/parties', methods=["POST"])
def create_party():
    data = request.get_json(force=True)
    if len(parties) == 0:
        _id = 1
    else:
        _id = parties[-1]['id'] + 1
    if data.get('name','') == '' or data.get('hqAddress','')=='' or data.get('logoUrl','')=='':
        return make_response(jsonify({
            "status":400,
            "error": 'party name or hqadress or logo cannot be empty'
        }), 400)
    
    new_party = {
        "id":_id,
        "name": data['name'],
        "hqAddress": data['hqAddress'],
        "logoUrl": data['logoUrl']
    }

    res = PoliticalParty().save_party(new_party)


    return make_response(jsonify({
        "status":201,
        "data": [res]
    }), 201)

@api.route("/parties", methods=['GET'])
def get_all_parties():

    parties = PoliticalParty().get_all_parties()
  
    return make_response(jsonify({
        "status":200,
        "data": parties
    }), 200)


@api.route('/parties/<int:party_id>', methods=['GET'])
def get_single_party(party_id):
    party=PoliticalParty.get_by_id(party_id)
    if party == None:
        return make_response(jsonify({
        "status":404,
        "error": 'party not found'
        }), 404)
    else:
        return make_response(jsonify({
            "status":200,
            "party":party
        }), 200)
