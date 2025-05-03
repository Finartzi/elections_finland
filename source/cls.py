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

class ElectionComparison:
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


