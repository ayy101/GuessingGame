def main():
    import random

    play = True
    usernum = 0
    compnum = 0
    level = 0
    p1Turns = 0
    p2Turns = 0
    pxTurns = 1
    p1Wins = 0
    p2Wins = 0
    y = True
    n = False
    Y = y
    N = n

    def askforNum():
        if level == 1:
            return int(input("Please enter a number between 1-10."))
        if level == 2:
            return int(input("Please enter a number between 1-20."))
        if level == 3:
            return int(input("Please enter a number between 1-100."))

    def wrong():
        if usernum < compnum:
            return "The number you entered is too low."
        if usernum > compnum:
            return "The number you entered is too high."

    def wrong2(numrange):
        if numrange < compnum:
            return "The number you entered is too low."
        if numrange > compnum:
            return "The number you entered is too high."

    def computer(numrange):
        if numrange > compnum and numrange % 2 == 0:
            return numrange/2
        if numrange > compnum and numrange % 2 != 0:
            return (numrange+1)/2
        if numrange < compnum and numrange % 2 == 0:
            return numrange + xnumrange/2
        if numrange < compnum and numrange % 2 != 0:
            return (numrange + xnumrange/2)

    while play == True:

        if p1Wins == 0 and p2Wins == 0:
            print("Welcome to the Guessing Game!\n")

            print("Choose a player mode!\n1. Single Player\n2. Human vs Human\n3.Human vs Computer")

            modenum = (int(input("Please enter the number of your desired mode.")))

            print("Choose a level!\n"
                  "1 (Easy)\n"
                  "2 (Medium)\n"
                  "3 (Hard)\n")

            level = int(input("Please enter the number of your desired level."))

            if level == 1:
                compnum = random.randrange(1,11)
            elif level == 2:
                compnum = random.randrange(1, 21)
            elif level == 3:
                compnum = random.randrange(1, 101)

        if modenum == 2:
            print("Player One's turn!")

        print("I'm thinking of a number... what is it?")

        usernum = askforNum()

        while usernum != compnum:
            print(wrong())
            pxTurns = pxTurns + 1
            usernum = askforNum()
            if level == 1:
                if pxTurns > 10:
                    print("Sorry, you took too many turns. You lose this round.")
            if level == 2:
                if pxTurns > 15:
                    print("Sorry, you took too many turns. You lose this round.")
            if level == 3:
                if pxTurns > 30:
                    print("Sorry, you took too many turns. You lose this round.")

        if modenum == 1 and usernum == compnum:
            print("Congratulations, you got it!\nWould you like to play again? (Y/N)")
            play = (input("Please enter your choice:"))
            if play == False:
                print("Thanks for playing!")

        if modenum == 2:
            p1Turns = pxTurns
            pxTurns = 1
            if usernum == compnum:
                print("Congratulations, you got it!\n")
            print("Now it's Player Two's turn!")
            if level == 1:
                compnum = random.randrange(1, 11)
            elif level == 2:
                compnum = random.randrange(1, 21)
            elif level == 3:
                compnum = random.randrange(1, 101)

            print("I'm thinking of a number... what is it?")

            usernum = askforNum()

            while usernum != compnum:
                print(wrong())
                pxTurns = pxTurns + 1
                usernum = askforNum()
                if level == 1:
                    if pxTurns > 10:
                        print("Sorry, you took too many turns. You lose this round.")
                if level == 2:
                    if pxTurns > 15:
                        print("Sorry, you took too many turns. You lose this round.")
                if level == 3:
                    if pxTurns > 30:
                        print("Sorry, you took too many turns. You lose this round.")

            p2Turns = pxTurns
            if p1Turns < p2Turns:
                print("Congratulations, you got it!\n")
                print("Player One wins this round!")
                p1Wins = p1Wins + 1
            if p1Turns > p2Turns:
                print("Congratulations, you got it!\n")
                print("Player Two wins this round!")
                p2Wins = p2Wins + 1
            if p1Turns == p2Turns:
                print("Congratulations, you got it!\n")
                print("This round is a tie!")

            if p1Wins >= 3 and p1Wins > p2Wins:
                print("Player One wins the game!")
                print("Would you like to play again?")
                play = (input("Please enter your choice:"))
                if play == False:
                    print("Thanks for playing!")
            if p2Wins >= 3 and p2Wins > p1Wins:
                print("Player Two wins the game!")
                print("Would you like to play again?")
                play = (input("Please enter your choice:"))
                if play == False:
                    print("Thanks for playing!")

        if modenum == 3:
            p1Turns = pxTurns
            pxTurns = 1
            print("Congratulations, you got it!\nNow it's the computer's turn!")
            if level == 1:
                compnum = random.randrange(1, 11)
                numrange = 10
            elif level == 2:
                compnum = random.randrange(1, 21)
                numrange = 20
            elif level == 3:
                compnum = random.randrange(1, 101)
                numrange = 100

            print("I'm thinking of a number... what is it?")

            xnumrange = numrange
            numrange = computer(numrange)
            print(numrange)
            pxTurns = pxTurns + 1

            while numrange != compnum:
                print(wrong2(numrange))
                pxTurns = pxTurns + 1
                print(numrange)
                numrange = computer(numrange)

            p2Turns = pxTurns
            if p1Turns < p2Turns:
                print("Congratulations, you got it!")
                print("Human wins this round!")
                p1Wins = p1Wins + 1
            if p1Turns > p2Turns:
                p2Wins = p2Wins + 1
                print("Congratulations, you got it!")
                print("Computer wins this round!")
            if p1Turns == p2Turns:
                print("Congratulations, you got it!")
                print("This round is a tie!")

            if p1Wins >= 3 and p1Wins > p2Wins:
                print("Human wins the game!")
                print("Would you like to play again?")
                play = (input("Please enter your choice:"))
                if play == False:
                    print("Thanks for playing!")
            if p2Wins >= 3 and p2Wins > p1Wins:
                print("Computer wins the game!")
                print("Would you like to play again?")
                play = (input("Please enter your choice:"))
                if play == False:
                    print("Thanks for playing!")
main()


