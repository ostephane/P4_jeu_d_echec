from tinydb import TinyDB

db_players = TinyDB('db.json')
players_table = db.table('players')
db.all()
players_table.truncate()  # clear the table first


class Player:
    """Creates a player"""

    def __init__(self, first_name='NIKO', last_name='BELL', date_of_birth="1/1/1", gender=None, rank=1):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rank = rank

    def serialize_player(self):
        player_id = {'first_name': self.first_name, 'last_name': self.last_name, 'date_of_birth': self.date_of_birth,
                     'gender': self.gender, 'rank': self.rank}
        db_players.insert(player_id)

    @staticmethod
    def deserialize_player(serialized_player):
        first_name = serialized_player['first_name']
        last_name = serialized_player['last_name']
        date_of_birth = serialized_player['date_of_birth']
        gender = serialized_player['gender']
        rank = serialized_player['rank']
        return Player(first_name, last_name, date_of_birth, gender, rank)

    @staticmethod
    def add_player():
        first_name = input("Tapez son prénom: ")
        last_name = input("Tapez son nom: ")
        date_of_birth = input("Tapez sa date de naissance: ")
        gender = input("Quel est son genre: ")
        Player(first_name, last_name, date_of_birth, gender).serialize_player()

    def update_rank(self):
        try:
            first_name = input("Tapez son prénom: ")
            last_name = input("Tapez son nom: ")
        except:
            first_name

# Player(gender='M').serialize_player()
# Player(first_name='LEA', gender='F').serialize_player()
