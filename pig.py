import random
import argparse

def roll_die():
    """Roll a 6 face die"""
    return random.randint(1, 6)


class Die:
    def __init__(self, faces=6):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)


class Player:
    def __init__(self, name):
        self.name = name
        self.total = 0
        # turn total might note be necessary here
        self.turn_total = 0

    def get_total(self):
        return self.total

    def __str__(self):
        return f"Player {self.name} total = {self.total}"

    def display(self):
        print(self.__str__())


class Game:
    def __init__(self, players, die):
        self.players = players
        self.die = die

    def play(self):

        active_player = 0
        choice = input("Roll(r) or Hold(h)? ")

        # loop until one player total turn >= 100
        while not self.check_winner():
            pass
            #   get an active player
            #   active player turn total = 0
            #   loop until hold or roll is 1
            #       ask for roll or hold
            #       if roll, roll the die
            #       if roll != 1: Update turn total
            #
            #   if hold, update player's total = total + turn total
            #   if not (the player rolled a one)

    def check_winner(self):
        """Check if one player has more than 100 points"""
        # if a player has a total > 100, return True else return False
        for player in self.players:
            if player.total >= 100:
                return True

        return False


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--numPlayers", help="URL to the datafile", type=int)
    # args = parser.parse_args()

    print("Welcome to the Pig Game")
    common_die = Die()
    players = [Player("One"), Player("Two")]
    game = Game(players, common_die)
    game.play()
