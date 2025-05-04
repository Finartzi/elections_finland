"""
    Logic
"""
import pathlib
import pprint as p
import file_handling as handle
import cls as c

list_data_files = ["JSON-data/kv2025_nominators.json", "JSON-data/av2025_nominators.json",
                   "JSON-data/kv2025_results.json", "JSON-data/av2025_results.json",
                   "JSON-data/kv2025_candidates.json", "JSON-data/av2025_candidates.json"]


def get_datafiles():
    return [f for f in pathlib.Path("JSON-data").glob("*.json")]


def nominators(data_file):
    def old_country_data(data, party, data_selection):
        values = data
        try:
            old = c.ElectionCompare(
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@election-event-name-abbreviation"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@advance-votes"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@advance-votes-percent"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@election-day-votes"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@election-day-votes-percent"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@total-votes"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@total-votes-percent"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@number-of-votes-total-change"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@votes-total-percent-change"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection]["@seats"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@seat-change"])
        except KeyError:
            old = c.ElectionCompare(
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@election-event-name-abbreviation"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@advance-votes"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@advance-votes-percent"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@election-day-votes"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@election-day-votes-percent"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@total-votes"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@total-votes-percent"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@number-of-votes-total-change"],
                values["election"]["country-data"]["nominator"][party]["comparison-election"][data_selection][
                    "@votes-total-percent-change"])

        value = [old.election_event_name_abbreviation,
                 old.advance_votes,
                 old.advance_votes_percent,
                 old.election_day_votes,
                 old.election_day_votes_percent,
                 old.total_votes,
                 old.total_votes_percent,
                 old.number_of_votes_total_change,
                 old.votes_total_percent_change,
                 old.seats,
                 old.seat_change]
        return value

    values = handle.getJSON(data_file)
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
        old_1 = old_country_data(values, x, 0)
        old_2 = old_country_data(values, x, 1)

        p.pprint(["Puolue: " + party.name, "Lyhenne: " + party.abbreviation,
                  "Ennakkoäänet: " + party.advance_votes + " - " + old_1[0] + ": " + old_1[1] + " - " + old_2[0] + ": " + old_2[1],
                  "Ennakko %: " + party.advance_votes_percent + " - " + old_1[0] + ": " + old_1[2] + " - " + old_2[0] + ": " + old_2[2],
                  "Vaalipäivän äänet: " + party.election_day_votes + " - " + old_1[0] + ": " + old_1[3] + " - " + old_2[0] + ": " + old_2[3],
                  "Vaalipäivän %: " + party.advance_votes_percent + " - " + old_1[0] + ": " + old_1[4] + " - " + old_2[0] + ": " + old_2[4],
                  "Äänet yhteensä: " + party.total_votes + " - " + old_1[0] + ": " + old_1[5] + " Muutos: " + old_1[7] + " - " + old_2[0] + ": " + old_2[5] + " Muutos: " + old_2[7],
                  "Äänet %: " + party.total_votes_percent + " - " + old_1[0] + ": " + old_1[6] + " Muutos %: " + old_1[8]+ " - " + old_2[0] + ": " + old_2[6] + " Muutos %: " + old_2[8],
                  "Paikkoja: " + party.seats + " - " + old_1[0] + ": " + old_1[9] + " muutos: " + old_1[10]])

    print("---")


def run():
    print(list_data_files[1])
    print(" --- ")
    nominators(list_data_files[1])
