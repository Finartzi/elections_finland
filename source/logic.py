"""
    Logic
"""
import pathlib
import pprint as p
import file_handling as handle
import cls as c

def get_datafiles():
    return [f for f in pathlib.Path("JSON-data").glob("*.json")]

def nominators():
    values = handle.getJSON("JSON-data/kv2025_nominators.json")
    print("Alueita: " + str(values["election"]["country-data"]["area-data"]["@number-of-polling-districts"]))
    """
        for item in values["election"]["country-data"].keys():
            print(item)
    """

    parties = len(values["election"]["country-data"]["nominator"])
    print("Puolueita: " + str(parties))
    print("---")

    for x in range(parties):
        party = c.Nominators(values["election"]["country-data"]["nominator"][x]["@name"],
                             values["election"]["country-data"]["nominator"][x]["@abbreviation"],
                             values["election"]["country-data"]["nominator"][x]["@advance-votes"],
                             values["election"]["country-data"]["nominator"][x]["@advance-votes-percent"],
                             values["election"]["country-data"]["nominator"][x]["@election-day-votes"],
                             values["election"]["country-data"]["nominator"][x]["@election-day-votes-percent"],
                             values["election"]["country-data"]["nominator"][x]["@total-votes"],
                             values["election"]["country-data"]["nominator"][x]["@total-votes-percent"],
                             values["election"]["country-data"]["nominator"][x]["@seats"])

        p.pprint(["Puolue: " + party.name, "Lyhenne: " + party.abbreviation,
                  "Ennakkoäänet: " + party.advance_votes, "Ennakko %: " + party.advance_votes_percent,
                 "Vaalipäivän äänet: " + party.election_day_votes, "Vaalipäivän %: " + party.advance_votes_percent,
                 "Äänet yhteensä: " + party.total_votes, "Äänet %: " + party.total_votes_percent,
                 "Paikkoja: " + party.seats])
        print("---")


def run():
    print("")
    nominators()