"""
    Logic
"""
import pathlib
import pprint as p
import file_handling as handle
import cls as c

def get_datafiles():
    #return os.listdir("JSON-data")
    return [f for f in pathlib.Path("JSON-data").glob("*.json")]

def nominators():
    values = handle.getJSON("JSON-data/kv2025_nominators.json")
    p.pprint(values["@identity-code"])
    p.pprint(values["@election-type"])
    #p.pprint(values["election"]["country-data"]["nominator"][1])
    party = c.Nominators(values["election"]["country-data"]["nominator"][0]["@name"],
                         values["election"]["country-data"]["nominator"][0]["@abbreviation"],
                         values["election"]["country-data"]["nominator"][0]["@advance-votes"],
                         values["election"]["country-data"]["nominator"][0]["@advance-votes-percent"],
                         values["election"]["country-data"]["nominator"][0]["@election-day-votes"],
                         values["election"]["country-data"]["nominator"][0]["@election-day-votes-percent"],
                         values["election"]["country-data"]["nominator"][0]["@total-votes"],
                         values["election"]["country-data"]["nominator"][0]["@total-votes-percent"],
                         values["election"]["country-data"]["nominator"][0]["@seats"])

    p.pprint(["Puolue: " + party.name, "Lyhenne: " + party.abbreviation,
              "Ennakkoäänet: " + party.advance_votes, "Ennakko %: " + party.advance_votes_percent,
             "Vaalipäivän äänet: " + party.election_day_votes, "Vaalipäivän %: " + party.advance_votes_percent,
             "Äänet yhteensä: " + party.total_votes, "Äänet %: " + party.total_votes_percent,
             "Paikkoja: " + party.seats])


def run():
    print("")
    nominators()