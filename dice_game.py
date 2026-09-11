import random

# Constants
GAME_GOAL   = 21

class Player():
    def __init__(self, name):
        self.name = name

class Dice():
    def __init__(self, sides = 6):
        self.sides = sides
    def throw(self):
        return random.randint(1, self.sides)

class Game():
    def __init__(self):
        self.isActive = True
        self.dice = Dice()
        self.total_sum = 0
        self._players = []
    def start(self):
        if len(self._players) == 0:
            self.addPlayer(Player())
        while self.isActive:
            diceResult = self.dice.throw()
            self.total_sum += diceResult
            print(f"Tärningskastet blev en {diceResult}:a. Totalsumma: {self.total_sum}")
            if self.total_sum == GAME_GOAL:
                print("Du vann!")
                break
            if self.total_sum > GAME_GOAL:
                print("Du förlorade.")
                break
            if input_yesNo_se("Vill du kasta igen? (j/n)") == False:
                break
        self.end()

    def addPlayer(self, player: Player):
        self._players.insert(player)

    def _onEnd(self):
        print("// Spelet avslutades. //")

    def end(self):
        self.isActive = False
        self._onEnd()

def input_yesNo_se(message: str) -> bool:
    while True:
        inp = input(message).lower().strip()
        if inp == "j":
            return True
        elif inp == "n":
            return False

def main():
    game = Game()
    game.start()

main()