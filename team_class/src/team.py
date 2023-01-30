class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach
        self.points = 0

    def add_player(self, new_player):
        self.players.append(new_player)

    def has_player(self, player_name):
        return player_name in self.players

    def play_game(self, won_game):
        if won_game:
            self.points += 3
