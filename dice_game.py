import random

# Constants
GAME_GOAL               =   21
GAME_MIN_PLAYERS        =   1
GAME_MAX_PLAYERS        =   2
GAME_OUTPUT_YOULOST     =   "* Du förlorade."
GAME_OUTPUT_YOUWON      =   "* Du vann!"

class Player():
    def __init__(self, name):
        self.name = name

class Dice():
    def __init__(self, sides = 6):
        self.sides = sides
    def throw(self):
        return random.randint(1, self.sides)

class PlayerData:
    def __init__(self, player: Player):
        self.player = player
        self.total_sum = 0
        self.throws = 0

class GameData:
    def __init__(self):
        # Data of active players.
        self.playerData = []

class Game():
    def __init__(self, playerCount = GAME_MIN_PLAYERS):
        self.isActive = False
        self.dice = Dice()
        self.data = GameData()

        # Instantiate player(s)
        for i in range(playerCount):
            player = Player(f"Spelare_{i+1}")
            entry = PlayerData(player)
            self.data.playerData.append(entry)

        self._currentPlayerIndex = random.randint(0, playerCount-1)

    def start(self):
        self.isActive = True
        while self.isActive:
            self._nextPlayer()

            if input_yesNo("Vill du kasta? (j/n)") == False:
                print()
                continue

            playerData = self._getCurrentPlayerData()
            diceResult = self.dice.throw()
            playerData.throws += 1
            playerData.total_sum += diceResult
            print(f"Tärningskastet blev en {diceResult}:a. Totalsumma: {playerData.total_sum}")

            if playerData.total_sum == GAME_GOAL:
                print(GAME_OUTPUT_YOUWON)
                print()
                break
            if playerData.total_sum > GAME_GOAL:
                if self.getPlayerCount() == 1:
                    print(GAME_OUTPUT_YOULOST)
                    print()
                    break
                else:
                    self._removePlayer(playerData)
                    print(f"* {playerData.player.name} förlorade.")
                    print()
                    if self.getPlayerCount() == 1:
                        print(f"-- {self._getCurrentPlayerData().player.name} --")
            else:
                print()
        
        self.end()

    def end(self):
        self.isActive = False
        print("// Spelet avslutades. //")
        
    def _getNextPlayerIndex(self) -> int:
        playerCount = self.getPlayerCount()
        i = self._currentPlayerIndex + 1
        if self._currentPlayerIndex == playerCount-1:
            # Index is the last item in the list.
            i = 0
        return i

    def _nextPlayer(self):
        self._currentPlayerIndex = self._getNextPlayerIndex()
        if self.getPlayerCount() != 1:
            print(f"-- {self._getCurrentPlayerData().player.name} --")

    def getPlayerCount(self) -> int:
        return len(self.data.playerData)

    def _removePlayer(self, playerData: PlayerData):
        playerDataIndex = self.data.playerData.index(playerData)

        self.data.playerData.pop(playerDataIndex)

        # Make sure _currentPlayerIndex stays within range of the list as its index could have been altered after using list.pop().
        # Check if _currentPlayerIndex was affected by the change.
        if self._currentPlayerIndex >= playerDataIndex:
            # Decrement index but stay within range.
            if self._currentPlayerIndex == 0:
                self._currentPlayerIndex = self.getPlayerCount() - 1
            else:
                self._currentPlayerIndex -= 1
        
    def _getCurrentPlayerData(self) -> PlayerData:
        return self.data.playerData[self._currentPlayerIndex]

def input_game_playerCount():
    playerCount : int
    while True:
        inp = input(f"Antal spelare (max {GAME_MAX_PLAYERS}): ").strip()
        try:
            playerCount = int(inp)
        except:
            print("Vänligen ange ett heltal.")
            continue
        if playerCount < GAME_MIN_PLAYERS or playerCount > GAME_MAX_PLAYERS:
            print(f"Antalet spelare får inte understiga {GAME_MIN_PLAYERS} eller överstiga {GAME_MAX_PLAYERS}.")
            continue
        break
    return playerCount

def input_yesNo(message: str) -> bool:
    while True:
        inp = input(message).lower().strip()
        if inp == "j":
            return True
        elif inp == "n":
            return False

# Application entry point
def main():
    playerCount = input_game_playerCount()
    game = Game(playerCount)

    print()
    game.start()

main()