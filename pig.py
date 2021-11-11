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

    def add_turn_total(self, value):
        self.turn_total += value
        print(f"Player {self.name} turn total is {self.turn_total}. Possible points {self.total + self.turn_total}")

    def bank(self):
        self.total += self.turn_total
        self.turn_total = 0
        print(f"Player {self.name} has accumulated {self.total} points")

    def roll_hold(self):
        """Roll or Hold"""
        choice = input("Roll(r) or Hold(h)? ")
        return choice


def ComputerPlayer(Player):
    def roll_hold(self):
        pass


class Game:
    def __init__(self, players, die):
        self.players = players
        self.die = die
        self.active_player = None

    def next_player(self):
        """Returns next player"""
        if self.active_player is None:
            self.active_player = 0
        else:
            self.active_player += 1
            if self.active_player == len(players):
                self.active_player = 0

        print(f"Player {self.players[self.active_player].name} turn...")
        return self.players[self.active_player]

    def play(self):
        """Play the game"""
        # loop until one player total turn >= 100
        active_player = self.next_player()
        while not self.check_winner():
            choice = active_player.roll_hold().lower()
            if choice == 'r':
                roll_value = self.die.roll()
                print(f"You roll a {roll_value}")
                if roll_value == 1:
                    print(f"Player {active_player.name} scratch!!!")
                    active_player.turn_total = 0
                    active_player = self.next_player()
                else:
                    active_player.add_turn_total(roll_value)
            elif choice == 'h':
                active_player.bank()
                active_player = self.next_player()
            else:
                print("Wrong choice. Enter r(oll) or h(hold)")
                continue

    def check_winner(self):
        """Check if one player has more than 100 points"""
        # if a player has a total > 100, return True else return False
        for player in self.players:
            if player.total >= 100:
                print(f"There is a Winner. {player.name} won with {player.total} points")
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
