class Nominators:
    def __init__(self, name, abbreviation, advance_votes, advance_votes_percent,
                 election_day_votes, election_day_votes_percent,
                 total_votes, total_votes_percent, seats):
        self.name = name
        self.abbreviation = abbreviation
        self.advance_votes = str(advance_votes)
        self.advance_votes_percent = str(advance_votes_percent)
        self.election_day_votes = str(election_day_votes)
        self.election_day_votes_percent = str(election_day_votes_percent)
        self.total_votes = str(total_votes)
        self.total_votes_percent = str(total_votes_percent)
        self.seats = str(seats)

class ElectionCompare:
    def __init__(self, election_event_name_abbreviation, advance_votes, advance_votes_percent,
                 election_day_votes, election_day_votes_percent,
                 total_votes, total_votes_percent,
                 number_of_votes_total_change, votes_total_percent_change,
                 seats=0, seat_change=0):
        self.election_event_name_abbreviation = election_event_name_abbreviation
        self.advance_votes = str(advance_votes)
        self.advance_votes_percent = str(advance_votes_percent)
        self.election_day_votes = str(election_day_votes)
        self.election_day_votes_percent = str(election_day_votes_percent)
        self.total_votes = str(total_votes)
        self.total_votes_percent = str(total_votes_percent)
        self.number_of_votes_total_change = str(number_of_votes_total_change)
        self.votes_total_percent_change = str(votes_total_percent_change)
        self.seats = str(seats)
        self.seat_change = str(seat_change)

class BasicVotingData:
    def __init__(self, eligible_voters_total, eligible_voters_men, eligible_voters_women,
                 eligible_voters_living_in_finland_total, eligible_voters_living_in_finland_men,
                 eligible_voters_living_in_finland_women, advance_voting_turnout,
                 election_day_voting_turnout, total_voting_turnout, number_to_be_elected):
        self.eligible_voters_total = str(eligible_voters_total)
        self.eligible_voters_men = str(eligible_voters_men)
        self.eligible_voters_women = str(eligible_voters_women)
        self.eligible_voters_living_in_finland_total = str(eligible_voters_living_in_finland_total)
        self.eligible_voters_living_in_finland_men = str(eligible_voters_living_in_finland_men)
        self.eligible_voters_living_in_finland_women = str(eligible_voters_living_in_finland_women)
        self.advance_voting_turnout = str(advance_voting_turnout)
        self.election_day_voting_turnout = str(election_day_voting_turnout)
        self.total_voting_turnout = str(total_voting_turnout)
        self.number_to_be_elected = str(number_to_be_elected)

class BasisVotingDataCompare:
    def __init__(self,
                 election_event_name_abbreviation, eligible_voters_living_in_finland_total,
                 advance_voting_turnout, election_day_voting_turnout, total_voting_turnout,
                 approved_votes_total, invalid_votes_total, number_to_be_elected):
        self.election_event_name_abbreviation = election_event_name_abbreviation
        self.eligible_voters_living_in_finland_total = str(eligible_voters_living_in_finland_total)
        self.advance_voting_turnout = str(advance_voting_turnout)
        self.election_day_voting_turnout = str(election_day_voting_turnout)
        self.total_voting_turnout = str(total_voting_turnout)
        self.approved_votes_total = str(approved_votes_total)
        self.invalid_votes_total = str(invalid_votes_total)
        self.number_to_be_elected = str(number_to_be_elected)

class BasicVotingDataSupplemental:
    def __init__(self,
                 advance_votes, advance_votes_males, election_day_votes, election_day_votes_males,
                 total_votes, total_votes_males, advance_votes_living_in_finland,
                 advance_votes_living_in_finland_males, election_day_votes_living_in_finland,
                 election_day_votes_living_in_finland_males, total_votes_living_in_finland,
                 total_votes_living_in_finland_males, advance_voting_turnout_living_in_finland,
                 election_day_voting_turnout_living_in_finland, total_voting_turnout_living_in_finland,
                 advance_votes_abroad, advance_votes_abroad_males, election_day_votes_abroad,
                 election_day_votes_abroad_males, total_votes_abroad, total_votes_abroad_males,
                 advance_voting_turnout_abroad, election_day_voting_turnout_abroad,
                 total_voting_turnout_abroad, approved_advance_votes, approved_election_day_votes,
                 approved_total_votes, invalid_advance_votes, invalid_election_day_votes, invalid_total_votes,
                 calculation_status_percent_advance_votes, calculation_status_percent_election_day_votes,
                 calculation_status_percent):
        self.advance_votes = str(advance_votes)
        self.advance_votes_males = str(advance_votes_males)
        self.election_day_votes = str(election_day_votes)
        self.election_day_votes_males = str(election_day_votes_males)
        self.total_votes = str(total_votes)
        self.total_votes_males = str(total_votes_males)
        self.advance_votes_living_in_finland = str(advance_votes_living_in_finland)
        self.advance_votes_living_in_finland_males = str(advance_votes_living_in_finland_males)
        self.election_day_votes_living_in_finland = str(election_day_votes_living_in_finland)
        self.election_day_votes_living_in_finland_males = str(election_day_votes_living_in_finland_males)
        self.total_votes_living_in_finland = str(total_votes_living_in_finland)
        self.total_votes_living_in_finland_males = str(total_votes_living_in_finland_males)
        self.advance_voting_turnout_living_in_finland = str(advance_voting_turnout_living_in_finland)
        self.election_day_voting_turnout_living_in_finland = str(election_day_voting_turnout_living_in_finland)
        self.total_voting_turnout_living_in_finland = str(total_voting_turnout_living_in_finland)
        self.advance_votes_abroad = str(advance_votes_abroad)
        self.advance_votes_abroad_males = str(advance_votes_abroad_males)
        self.election_day_votes_abroad = str(election_day_votes_abroad)
        self.election_day_votes_abroad_males = str(election_day_votes_abroad_males)
        self.total_votes_abroad = str(total_votes_abroad)
        self.total_votes_abroad_males = str(total_votes_abroad_males)
        self.advance_voting_turnout_abroad = str(advance_voting_turnout_abroad)
        self.election_day_voting_turnout_abroad = str(election_day_voting_turnout_abroad)
        self.total_voting_turnout_abroad = str(total_voting_turnout_abroad)
        self.approved_advance_votes = str(approved_advance_votes)
        self.approved_election_day_votes = str(approved_election_day_votes)
        self.approved_total_votes = str(approved_total_votes)
        self.invalid_advance_votes = str(invalid_advance_votes)
        self.invalid_election_day_votes = str(invalid_election_day_votes)
        self.invalid_total_votes = str(invalid_total_votes)
        self.calculation_status_percent_advance_votes = str(calculation_status_percent_advance_votes)
        self.calculation_status_percent_election_day_votes = str(calculation_status_percent_election_day_votes)
        self.calculation_status_percent = str(calculation_status_percent)

class Area:
    # for districts as well
    def __init__(self, abbreviation, name, number_of_polling_districts):
        self.abbreviation = abbreviation
        self.name = name
        self.number_of_polling_districts = str(number_of_polling_districts)

class Candidate:
    def __init__(self, candidate_number, first_name, last_name, gender, age, occupation,
                 home_municipality, language, advance_votes, election_day_votes, total_votes,
                 advance_votes_percent, election_day_percent, total_vote_percent, comparative_index,
                 elected_information="not available", position="not available", final_position="not available"):
        self.candidate_number = str(candidate_number)
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = str(age)
        self.occupation = occupation
        self.home_municipality = home_municipality
        self.language = language
        self.advance_votes = str(advance_votes)
        self.election_day_votes = str(election_day_votes)
        self.total_votes = str(total_votes)
        self.advance_votes_percent = str(advance_votes_percent)
        self.election_day_percent = str(election_day_percent)
        self.total_vote_percent = str(total_vote_percent)
        self.comparative_index = str(comparative_index)
        self.elected_information = str(elected_information)
        self.position = str(position)
        self.final_position = str(final_position)

class CandidateCompare:
    def __init__(self, election_event_name_abbreviation, total_votes):
        self.election_event_name_abbreviation = election_event_name_abbreviation
        self.total_votes = str(total_votes)

