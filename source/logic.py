"""
    Logic
"""
import pathlib
import pprint as p
from os import WCONTINUED

from Cython.Shadow import returns
from IPython.testing.tools import help_output_test
from jaraco.functools import except_
from jedi.inference.helpers import is_number

import file_handling as handle
import cls as c

list_data_files = ["JSON-data/kv2025_nominators.json", "JSON-data/av2025_nominators.json",
                   "JSON-data/kv2025_results.json", "JSON-data/av2025_results.json",
                   "JSON-data/kv2025_candidates.json", "JSON-data/av2025_candidates.json"]


def get_datafiles():
    return [f for f in pathlib.Path("JSON-data").glob("*.json")]


def nominators(data_file):
    print(data_file)
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
    print(data_file)
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
              "Aiemmissa vaaleissa annetuista äänistä ..",
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
              "Ulkomailta yhteensä %: " + supplemental.total_voting_turnout_abroad,
              "Ennakkoäänestys % kotimaassa: " + supplemental.advance_voting_turnout_living_in_finland,
              "Äänestyspäivän % kotimaassa: " + supplemental.election_day_voting_turnout_living_in_finland,
              "Kotimaassa yhteensä %: " + supplemental.total_voting_turnout_living_in_finland,
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


def candidate_data(data_file, areaIndex, communityIndex, partyIndex, candidateIndex=-1):
    def area(obj):
        retval = []
        for i in range(len(obj["election"]["electoral-area"])):
            mainArea = c.Area(
                obj["election"]["electoral-area"][i]["area-data"]["@abbreviation"],
                obj["election"]["electoral-area"][i]["area-data"]["@name"],
                obj["election"]["electoral-area"][i]["area-data"]["@number-of-polling-districts"])

            retval.append(["Index: " + str(i) +
                      " Alue: " + mainArea.name +
                      " Lyhenne: " + mainArea.abbreviation +
                      " Piirien määrä: " + mainArea.number_of_polling_districts])
        return retval

    def community(obj, areaIndex):
        retval = []
        for i in range(len(obj["election"]["electoral-area"][areaIndex]["electoral-area"])):
            cityArea = c.Area(
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][i]["area-data"]["@abbreviation"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][i]["area-data"]["@name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][i]["area-data"]["@number-of-polling-districts"])

            retval.append(["Index: " + str(i) +
                      " Alue: " + cityArea.name +
                      " Lyhenne: " + cityArea.abbreviation +
                      " Piirien määrä: " + cityArea.number_of_polling_districts])
        return retval

    def party(obj, areaIndex, communityIndex):
        retval = []
        for i in range(
                len(obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"])):
            retval.append(["Index: " + str(i) +
                     " Puolue: " + obj["election"]["electoral-area"][areaIndex]
                     ["electoral-area"][communityIndex]["nominator"][i]["@name"] +
                     " Lyhenne: " + obj["election"]["electoral-area"][areaIndex]
                     ["electoral-area"][communityIndex]["nominator"][i]["@abbreviation"]])
        return retval

    def candidates(obj, areaIndex, communityIndex, partyIndex):
        retval = []

        def candidate_add(obj, areaIndex, communityIndex, partyIndex, candidateIndex):
        # Had to split info this way, cause KV- and AV-files here different ..
            try:
                candidate = c.Candidate(None, None, None, None, None,
                                        None, None, None, None,
                                        None, None, None,
                                        None, None, None,
                    obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex][
                        "candidate"][candidateIndex]["@elected-information"],
                    obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex][
                        "candidate"][candidateIndex]["@position"],
                    obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex][
                        "candidate"][candidateIndex]["@final-position"])
                return " Valinta: " + candidate.elected_information + " Sija: " + candidate.final_position
            except KeyError:
                return ""

        def compare_old(obj, areaIndex, communityIndex, partyIndex, candidateIndex):
            # {'@election-event-name-abbreviation': 'KV-2021', '@total-votes': 59}
            retval = []
            try:
                for i in range(len(
                    obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                        partyIndex]["candidate"][candidateIndex]["comparison-election"])):
                    old = c.CandidateCompare(
                        obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex][
                             "candidate"][candidateIndex]["comparison-election"][i]["@election-event-name-abbreviation"],
                        obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex][
                            "candidate"][candidateIndex]["comparison-election"][i]["@total-votes"])
                    retval.append(" Vaalit: " + old.election_event_name_abbreviation + " Äänet yhteensä: " + old.total_votes)
                return retval
            except KeyError:
                pass

        for i in range(len(
            obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                partyIndex]["candidate"])):
            candidate = c.Candidate(
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@candidate-number"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@first-name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@last-name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@gender"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@age"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@occupation"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@home-municipality"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@language"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@advance-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@election-day-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@total-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@advance-votes-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@election-day-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@total-vote-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][
                    partyIndex][
                    "candidate"][i]["@comparative-index"])

            tmp = candidate_add(obj, areaIndex, communityIndex, partyIndex, i)
            old = str(compare_old(obj, areaIndex, communityIndex, partyIndex, i))

            retval.append("Index: " + str(i) + " Numero: " + candidate.candidate_number + " Name: " + candidate.last_name +
                     " " + candidate.first_name + " Ikä: " + candidate.age + " Ammatti: " + candidate.occupation +
                     " Ennakkoäänet: " + candidate.advance_votes + ", " + candidate.advance_votes_percent + "%" +
                     " Vaalipäivän äänet: " + candidate.election_day_votes + ", " + candidate.election_day_percent + "%" +
                     " Yhteensä: " + candidate.total_votes + ", " + candidate.total_vote_percent + "%" +
                     " Vertailuluku: " + candidate.comparative_index + tmp + old)

        if (candidateIndex >= 0):
            return retval[candidateIndex]
        else:
            return retval


    print(data_file)
    values = handle.getJSON(data_file)
    p.pprint(values["election"]["country-data"]["area-data"]["@number-of-polling-districts"])
    print("---")
    print("Hyvinvointialueet:")
    p.pprint(area(values))
    print("---")
    print(f"Valitun {(values["election"]["electoral-area"][areaIndex]["area-data"]["@name"])} hyvinvointialueen kunnat:")
    p.pprint(community(values,areaIndex))
    print("---")
    print("Puolueet:")
    #p.pprint(party(values, areaIndex, communityIndex))
    print("---")
    print("Valittu kunta:")
    p.pprint(values["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["area-data"]["@name"])
    print("Valittu puolue:")
    p.pprint(values["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex]["@name"])
    print("Ehdokaslistan pituus:")
    p.pprint(len(values["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["nominator"][partyIndex]["candidate"]))
    print("---")
    print("Kandidaatit:")
    #p.pprint(candidates(values,areaIndex, communityIndex, partyIndex))
    print("---")

def candidates_districts(obj, areaIndex, communityIndex, nominatorIndex=-1, districtIndex=-1, candidateIndex=-1, shortlist=True):

    def districts(obj, areaIndex, communityIndex):
        retval = []
        for i in range(len(obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                           ["electoral-area"])):
            district = c.Area(
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][i]["area-data"]["@abbreviation"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][i]["area-data"]["@name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][i]["area-data"]["@number-of-polling-districts"])
            retval.append("Index: " + str(i) + ", Alueen nimi " + district.name)
        return retval

    def district_nominators(obj, areaIndex, communityIndex, districtIndex, nominatorIndex, shortlist):
        # dict_keys(['@standard-party-number', '@nominator-number', '@party-identifier', '@name', '@name-in-swedish', '@name-in-english', '@abbreviation', '@abbreviation-in-swedish', '@abbreviation-in-english', '@lowest-candidate-number', '@highest-candidate-number', '@electoral-alliance-number', '@electoral-alliance-name', '@electoral-alliance-name-in-swedish', '@advance-votes', '@election-day-votes', '@total-votes', '@advance-votes-percent', '@election-day-votes-percent', '@total-votes-percent', '@seats', 'candidate'])
        retval = []
        district = districts(obj, areaIndex, communityIndex)

        for i in range(len(
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"])):
            party = c.Nominators(
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@abbreviation"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@advance-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@advance-votes-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@election-day-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@election-day-votes-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@total-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@total-votes-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]["electoral-area"][districtIndex][
                    "nominator"][i]["@seats"])
            if (shortlist):
                retval.append(district[districtIndex] +
                              ", Lyhenne: " + party.abbreviation +
                              ", Äänet yhteensä: " + party.total_votes)
            else:
                retval.append(district[districtIndex] +
                              ", Puolue: " + party.name +
                              ", Lyhenne: " + party.abbreviation +
                              ", Ennakkoäänet: " + party.advance_votes +
                              ", Ennakko %: " + party.advance_votes_percent +
                              ", Vaalipäivän äänet: " + party.election_day_votes +
                              ", Vaalipäivän %: " + party.election_day_votes_percent +
                              ", Äänet yhteensä: " + party.total_votes +
                              ", Äänet %: " + party.total_votes_percent)
        if (nominatorIndex >= 0):
            return retval[nominatorIndex]
        else:
            return retval

    def candidate_districts(obj, areaIndex, communityIndex, districtIndex, nominatorIndex, candidateIndex=-1):
        retval = []
        nominators = district_nominators(obj, areaIndex, communityIndex, districtIndex, nominatorIndex,True)
        counter = len(obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                           ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"])
        for i in range(counter):
            candidate = c.Candidate(
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                   ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@candidate-number"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@first-name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@last-name"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@gender"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@age"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@occupation"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@home-municipality"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@language"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@advance-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@election-day-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@total-votes"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@advance-votes-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@election-day-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@total-vote-percent"],
                obj["election"]["electoral-area"][areaIndex]["electoral-area"][communityIndex]
                ["electoral-area"][districtIndex]["nominator"][nominatorIndex]["candidate"][i]["@comparative-index"],
                None,None, None)
            retval.append("Index: " + str(i) + ", Nimi: " + candidate.last_name + " " + candidate.first_name + ", Äänet: " + candidate.total_votes)
        tmp = ""
        if(candidateIndex >= 0):
            return retval[candidateIndex]
        else:
            return retval

    print(" === ")
    # List districts and parties
    list_districts = districts(obj, areaIndex, communityIndex)
    list_nominators = []
    for i in range(len(list_districts)):
        list_nominators.append(district_nominators(obj, areaIndex, communityIndex, i, nominatorIndex, shortlist))
    if (districtIndex > -1):
        p.pprint(list_nominators[districtIndex])
    #elif(nominatorIndex > -1):
    #    p.pprint(list_nominators[nominatorIndex])
    else:
        p.pprint(list_nominators)

    # List candidates of a party
    list_candidate = []
    if (nominatorIndex > -1):
        for i in range(len(list_districts)):
            list_candidate.append([list_districts[i],
                                   candidate_districts(obj, areaIndex, communityIndex, i, nominatorIndex,
                                                       candidateIndex)])
    # andidate_districts(obj, areaIndex, communityIndex, districtIndex, nominatorIndex, candidateIndex=-1
    else:
        for i in range(len(list_districts)):
            list_candidate.append(candidate_districts(obj,areaIndex, communityIndex, districtIndex,
                                                      nominatorIndex, candidateIndex))

    return list_candidate


def run():
    print(list_data_files[1])
    values = handle.getJSON(list_data_files[4])
    print(" --- ")
    #nominators(list_data_files[1])
    #results(list_data_files[2])
    healthareaindex = 3  # VaKe
    communityindex = 1  # Vantaa, ja Kerava = 0
    district_nominator_index = 7  # Perussuomalaiset = 7
    districtindex = -1 # if less than 0 creates whole list, otherwise only indexed district

    # KV-file
    partyindex = -1  # Perussuomalaiset = 7
    candidateindex = -1  # 52
    #candidate_data(list_data_files[4], healthareaindex, communityindex, partyindex) # all
    #candidate_data(list_data_files[4], healthareaindex, communityindex, partyindex, candidateindex) # single candidate

    # AV-file
    #partyindex = 12 # Perussuomalaiset
    #candidateindex = 17
    #candidate_data(list_data_files[5], healthareaindex, communityindex, partyindex) # all
    #candidate_data(list_data_files[5], healthareaindex, communityindex, partyindex, candidateindex) # single candidate

    print("Kaikki puolueet äänestysalueittain:")
    #p.pprint(candidates_districts(values,healthareaindex, communityindex, district_nominator_index, districtindex, False)) # long version
    #p.pprint(candidates_districts(values, healthareaindex, communityindex, district_nominator_index, districtindex)) # short version

    print("Kandidaatit äänestysalueittain:")
    p.pprint(candidates_districts(values, healthareaindex, communityindex, district_nominator_index, districtindex, candidateindex))


