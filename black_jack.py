class Player:
    def __init__(self, name, amount):
        self.name = name
        self.bankroll = amount
        self.wins = 0
        self.loses = 0

    def add(self, amount):
        self.bankroll += amount

    def reduce(self, amount):
        self.bankroll -= amount

    def win(self):
        self.wins += 1

    def lose(self):
        self.loses += 1

    def stat(self):
        print(self.wins, self.loses)


