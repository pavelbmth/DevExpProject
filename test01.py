def hello() -> object:
    name = input("Enter your name >>> ")
    print(f"Hello {name}!")
    choose = input("Please choose the game >>> ")


def game_menu():
    game_list = {
        1: "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
        2: "2. Guess Game - guess a number and see if you chose like the computer",
        3: "3. Currency Roulette - try and guess the value of a random amount of USD in ILS",
    }

    for games in game_list.values():
        print(games)

game_menu()
hello()
