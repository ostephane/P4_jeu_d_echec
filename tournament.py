from tinydb import TinyDB

db = TinyDB('db.json')
tournament_table = db.table('tournoi')
tournament_table.truncate()  # clear the table first


class Tournament:
    """ Creates a tournament"""
    def __init__(self, name, place, date, rounds=4):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds

    def serialize_tournament(self):
        tournament_id = {'name': self.name, 'place': self.place, 'date': self.date, 'rounds': self.rounds}
        db.insert(tournament_id)

    @staticmethod
    def deserialize_tournament(serialized_tournament):
        name = serialized_tournament['name']
        place = serialized_tournament['place']
        date = serialized_tournament['date']
        rounds = serialized_tournament['rounds']
        return Tournament(name, place, date, rounds)

    def round(self):
        """ Manages one round """
        pass

    def time(self):
        """ Sets time for one round """
        pass

    def description(self):
        """ Prints instructions from the tournament director """
        pass
