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


def results(data_file):
    def old_country_data(data, data_selection):
        values = data
        old = c.BasisVotingDataCompare(
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@election-event-name-abbreviation"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@eligible-voters-living-in-finland-total"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@advance-voting-turnout"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@election-day-voting-turnout"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@total-voting-turnout"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@approved-votes-total"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@invalid-votes-total"],
            values["election"]["country-data"]["basic-voting-data"]["comparison-election"][data_selection]["@number-to-be-elected"])
        value = [old.election_event_name_abbreviation,
                 old.eligible_voters_living_in_finland_total,
                 old.advance_voting_turnout,
                 old.election_day_voting_turnout,
                 old.total_voting_turnout,
                 old.approved_votes_total,
                 old.invalid_votes_total,
                 old.number_to_be_elected]
        return value

    values = handle.getJSON(data_file)
    print("Vaalipiirien lukumäärä: " + str(values["election"]["country-data"]["area-data"]["@number-of-polling-districts"]))
    print(" - ")
    voting = c.BasicVotingData(
        values["election"]["country-data"]["basic-voting-data"]["@eligible-voters-total"],
        values["election"]["country-data"]["basic-voting-data"]["@eligible-voters-men"],
        values["election"]["country-data"]["basic-voting-data"]["@eligible-voters-women"],
        values["election"]["country-data"]["basic-voting-data"]["@eligible-voters-living-in-finland-total"],
        values["election"]["country-data"]["basic-voting-data"]["@eligible-voters-living-in-finland-men"],
        values["election"]["country-data"]["basic-voting-data"]["@eligible-voters-living-in-finland-women"],
        values["election"]["country-data"]["basic-voting-data"]["@advance-voting-turnout"],
        values["election"]["country-data"]["basic-voting-data"]["@election-day-voting-turnout"],
        values["election"]["country-data"]["basic-voting-data"]["@total-voting-turnout"],
        values["election"]["country-data"]["basic-voting-data"]["@number-to-be-elected"])

    supplemental = c.BasicVotingDataSupplemental(
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-votes-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-votes-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-votes-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-votes-living-in-finland"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-votes-living-in-finland-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-votes-living-in-finland"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-votes-living-in-finland-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-votes-living-in-finland"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-votes-living-in-finland-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-voting-turnout-living-in-finland"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-voting-turnout-living-in-finland"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-voting-turnout-living-in-finland"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-votes-abroad"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-votes-abroad-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-votes-abroad"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-votes-abroad-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-votes-abroad"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-votes-abroad-males"],
        values["election"]["country-data"]["supplemental-voting-data"]["@advance-voting-turnout-abroad"],
        values["election"]["country-data"]["supplemental-voting-data"]["@election-day-voting-turnout-abroad"],
        values["election"]["country-data"]["supplemental-voting-data"]["@total-voting-turnout-abroad"],
        values["election"]["country-data"]["supplemental-voting-data"]["@approved-advance-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@approved-election-day-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@approved-total-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@invalid-advance-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@invalid-election-day-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@invalid-total-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@calculation-status-percent-advance-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@calculation-status-percent-election-day-votes"],
        values["election"]["country-data"]["supplemental-voting-data"]["@calculation-status-percent"])

    p.pprint(["Äänioikeutettuja: " + voting.eligible_voters_total + ", " +
              old_country_data(values,0)[0] + ": " + old_country_data(values, 0)[1] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[1],
                  ", joista miehiä: " + voting.eligible_voters_men,
                  ", ja naisia: " + voting.eligible_voters_women,
                  "Suomessa asuvia: " + voting.eligible_voters_living_in_finland_total,
                  ", joista miehiä: " + voting.eligible_voters_living_in_finland_men,
                  ", ja naisia: " + voting.eligible_voters_living_in_finland_women,
                  "Ennakkoäänet %:" + voting.advance_voting_turnout + ", " +
              old_country_data(values, 0)[0] + ": " + old_country_data(values, 0)[2] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[2],
                  "Vaalipäivän äänet %:" + voting.election_day_voting_turnout + ", " +
              old_country_data(values, 0)[0] + ": " + old_country_data(values, 0)[3] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[3],
                  "Kokonais %: " + voting.total_voting_turnout + ", " +
              old_country_data(values, 0)[0] + ": " + old_country_data(values, 0)[4] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[4],
                  "Kokonaispaikkamäärä: " + voting.number_to_be_elected + ", " +
              old_country_data(values, 0)[0] + ": " + old_country_data(values, 0)[7] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[7],
              "Aiemmmissa vaaleissa annetuista äänistä ..",
              "Hyväksyttyjä: " +
              old_country_data(values, 0)[0] + ": " + old_country_data(values, 0)[5] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[5],
              "Hylättyjä: "+
              old_country_data(values, 0)[0] + ": " + old_country_data(values, 0)[6] + " " +
              old_country_data(values, 1)[0] + ": " + old_country_data(values, 1)[6]])
    print(" - - - ")

    p.pprint(["Ennakkoääniä: " + supplemental.advance_votes +
              ", joista miehiä: " + supplemental.advance_votes_males +
              ", ja naisia: " + str(int(supplemental.advance_votes) - int(supplemental.advance_votes_males)),
              "Äänestyspäivän äänet: " + supplemental.election_day_votes +
              ", joista miehiä: " + supplemental.election_day_votes_males +
              ", ja naisia: " + str(int(supplemental.election_day_votes) - int(supplemental.election_day_votes_males)),
              "Kokonaisäänimäärä: " + supplemental.total_votes +
              ", joista miehiä:" + supplemental.total_votes_males +
              ", ja naisia: " + str(int(supplemental.total_votes) - int(supplemental.total_votes_males)),
              "Suomessa asuvien ennakkoääniä: " + supplemental.advance_votes_living_in_finland +
              ", joista miehiä: " + supplemental.advance_votes_living_in_finland_males +
              ", ja naisia: " + str(int(supplemental.advance_votes_living_in_finland) - int(supplemental.advance_votes_living_in_finland_males)),
              "Suomen ulkopuolelta ennakkoääniä: " + supplemental.advance_votes_abroad +
              ", joista miehiä: " + supplemental.advance_votes_abroad_males +
              ", ja naisia: " + str(int(supplemental.advance_votes_abroad) - int(supplemental.advance_votes_abroad_males)),
              "Suomessa asuvien äänestyspäivän ääniä: " + supplemental.election_day_votes_living_in_finland +
              ", joista miehiä: " + supplemental.election_day_votes_living_in_finland_males +
              ", ja naisia: " + str(int(supplemental.election_day_votes_living_in_finland) - int(supplemental.election_day_votes_living_in_finland_males)),
              "Suomessa ulkopuolelta äänestyspäivän ääniä: " + supplemental.election_day_votes_abroad +
              ", joista miehiä: " + supplemental.election_day_votes_abroad_males +
              ", ja naisia: " + str(int(supplemental.election_day_votes_abroad) - int(supplemental.election_day_votes_abroad_males)),
              "Kaikkien Suomessa asuvien äänet: " + supplemental.total_votes_living_in_finland +
              ", joista miehiä: " + supplemental.total_votes_living_in_finland_males +
              ". ja naisia: " + str(int(supplemental.total_votes_living_in_finland) - int(supplemental.total_votes_living_in_finland_males)),
              "Kaikkien Suomen ulkopuolella asuvien äänet: " + supplemental.total_votes_abroad +
              ", joista miehiä: " + supplemental.total_votes_abroad_males +
              ", ja naisia: " + str(int(supplemental.total_votes_abroad) - int(supplemental.total_votes_abroad_males)),
              "Ennakkoäänestys % ulkomailla: " + supplemental.advance_voting_turnout_abroad,
              "Äänestyspäivän % ulkomailla: " + supplemental.election_day_voting_turnout_abroad,
              "Ulkomailta %: " + supplemental.total_voting_turnout_abroad,
              "Ennakkoäänestys % kotimaassa: " + supplemental.advance_voting_turnout_living_in_finland,
              "Äänestyspäivän % kotimaassa: " + supplemental.election_day_voting_turnout_living_in_finland,
              "Kotimaassa %: " + supplemental.total_voting_turnout_living_in_finland,
              "Hyväksytyt ennakkoäänet: " + supplemental.approved_advance_votes,
              "Hyväksytyt äänestyspäivän äänet: " + supplemental.approved_election_day_votes,
              "Hyväksytyt äänet: " + supplemental.approved_total_votes,
              "Hylätyt ennakkoäänet: " + supplemental.invalid_advance_votes,
              "Hylätyt äänestypäivän äänet: " + supplemental.invalid_election_day_votes,
              "Hylätyt äänet: " + supplemental.invalid_total_votes,
              "Ennakkoäänistä laskettu %: " + supplemental.calculation_status_percent_advance_votes,
              "Äänestyspäivän äänistä laskettu %: " + supplemental.calculation_status_percent_election_day_votes,
              "Äänistä laskettu %: " + supplemental.calculation_status_percent])
    print(" - - - ")

# values - keys (['@identity-code', '@election-type', 'election'])
# Election -> (['@latest-snapshot-timestamp', '@calculation-phase', 'country-data', 'electoral-area'])
# country-data -> (['@identifier', '@area-type', '@joined-area', 'area-data', 'basic-voting-data', 'supplemental-voting-data'])

# p.pprint(values["election"]["country-data"]["basic-voting-data"]["comparison-election"].keys())
#p.pprint(values["election"]["country-data"]["basic-voting-data"]["comparison-election"])





def run():
    print(list_data_files[1])
    print(" --- ")
    #nominators(list_data_files[1])
    results(list_data_files[2])
