def welcome(name):
 print(f"Hello {name} and welcome to the World of Games (WoG).")
 print("Here you can find many cool games to play.")
 print(" ")


def load_game():
    def print_menu():
        print("Please choose a game to play:")
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
        print("2. Guess Game - guess a number and see if you chose like the computer")
        print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    print_menu()

    def choose_difficulty():
        print("Please choose game difficulty from 1 to 5:")

        difficulty_option = int(input("Choose a difficulty >> "))
        if difficulty_option == 1:
            print(f"Game Difficulty {difficulty_option}")
        elif difficulty_option == 2:
            print(f"Difficulty {difficulty_option}")
        elif difficulty_option == 3:
            print(f"Difficulty {difficulty_option}")
        elif difficulty_option == 4:
            print(f"Difficulty {difficulty_option}")
        elif difficulty_option == 5:
            print(f"Difficulty {difficulty_option}")
        else:
            print("Invalid Option, please try again")
            choose_difficulty()


    def choose_option():

        option = int(input("Choose a game >> "))
        if option == 1:
            choose_difficulty()
        elif option == 2:
            choose_difficulty()
        elif option == 3:
            choose_difficulty()
        else:
            print("Invalid Option, please try again")
            choose_option()
    choose_option()




    # def choose_option():
    #     option = int(input("Choose a game >> "))
    #     while option == "1" and option == "2" and option == "3":
    #         choose_difficulty()
    #     else:
    #         print("Invalid Option, please try again")
    #
    # choose_option()


    # print("Please choose game difficulty from 1 to 5:")
    # difficulty = int(input("Your difficulty >> "))
    #print("Invalid Option, please try again")










