parties = []

class PoliticalParty:

    def save_party(self, party):
        parties.append(party)
        return ({
            "id":party['id'],
            "name":party['name']
        })


    def get_all_parties(self,):
        return(parties)