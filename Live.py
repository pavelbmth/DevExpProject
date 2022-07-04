from curses.ascii import isdigit
from re import A


class Welcome:
    def __init__(self, name):
        self.name = name
        

    def hello():
        name = input("Enter your name >>> ")

    def menu():
        game_list = {
            1 : "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
            2 : "2. Guess Game - guess a number and see if you chose like the computer",
            3 : "3. Currency Roulette - try and guess the value of a random amount of USD in ILS",
        }
        print("Game menu")
        for game in game_list.values():
            print (game)

    def choose_game():
        game_num = int(input("Choose your game >>> "))

        if game_num.isdigit() == True:
            # Welcome.choose_level()
            print("True")
        else:
            # Welcome.choose_game()
            print("False")

        def choose_level():
            level_num = int(input("Choose your level 1-5 >>> "))
       


Welcome.hello()
Welcome.menu()
Welcome.choose_game()
