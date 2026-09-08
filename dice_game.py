import random

# Constants
GOAL = 21

# States
total_sum : int = 0
game_continues : bool = True

def dice_throw():
    global total_sum
    throw = random.randint(1,6)
    total_sum += throw
    print(f"Tärningskastet blev en {throw}:a. Totalsumma: {total_sum}")

def input_yesNo_se(message: str) -> bool:
    while True:
        inp = input(message).lower().strip()
        if inp == "j":
            return True
        elif inp == "n":
            return False

def game_start():
    global game_continues
    while game_continues:
        dice_throw()
        if total_sum == GOAL:
            print("Du vann!")
            break
        if total_sum > GOAL:
            print("Du förlorade.")
            break
        if input_yesNo_se("Vill du kasta igen? (j/n)") == False:
            break
    game_continues = False

def game_end():
    print("// Spelet avslutades. //")

def main():
    game_start()
    game_end()

main()