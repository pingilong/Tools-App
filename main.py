import pyfiglet
import termcolor2

"""

Put everything in Kernel .
Run the from here .

"""

# Import * from Kernel .
from kernel import *

# ============= functions =============

# ============= labels =============

name = pyfiglet.figlet_format("Tool App")
print(termcolor2.colored(name,"red"))

by = "By: Mohammad Shokouhian"
print(termcolor2.colored(by,"green",attrs=["bold","underline"]))

# ============= if =============

a = 0
while a < 1:
    print(termcolor2.colored("\n[1] Caculator","magenta"))
    print(termcolor2.colored("[2] Time tool","magenta"))
    print(termcolor2.colored("[3] Wikipedia Search","magenta"))
    print(termcolor2.colored("[4] Rock-Scissor-Paper","magenta"))
    print(termcolor2.colored("[5] Guess Number","magenta"))
    print(termcolor2.colored("[6] Text to Speech","magenta"))
    print(termcolor2.colored("[7] Shut down","magenta"))
    print(termcolor2.colored("[8] Backgroud Changer","magenta"))
    print(termcolor2.colored("[0] Quit\n","magenta"))
    firstQ = input(">>> What would you like to do: ")
    
    if firstQ == "1":
        runcalc()
    elif firstQ == "2":
        # ============= inputs and texts(time) =============

        print(termcolor2.colored("[1] Animal of birth (Miladi)","magenta"))
        print(termcolor2.colored("[2] Animal of birth (Shamsi)","magenta"))
        print(termcolor2.colored("[3] Today","magenta"))
        print(termcolor2.colored("[4] Miladi to Shamsi","magenta"))
        print(termcolor2.colored("[5] Shamsi to Miladi","magenta"))
        print(termcolor2.colored("[6] Days of life (Miladi)","magenta"))
        print(termcolor2.colored("[7] Days of life (Shamsi)","magenta"))

        work = input(">>> what do you want to do? ")

        # ============= if(time) =============

        if work == "1":
            try:
                animalmiladi(int(input("\n>>> Enter your year of birth: ")))
            except:
                print("Error!")
        elif work == "2":
            try:
                animalshamsi(int(input("\n>>> Enter your year of birth: ")))
            except:
                print("Error!")
        elif work == "3":
            try:
                todayShamsifunc(year,month,day)
                todayMiladifunc()
            except:
                print("Error!")
        elif work == "4":
            try:
                y1 = int(input("\n>>> year: "))
                m1 = int(input(">>> month: "))
                d1 = int(input(">>> day: "))
                miladiToShamsi(y1,m1,d1)
            except:
                print("Error!")
        elif work == "5":
            try:
                y2 = int(input("\n>>> year: "))
                m2 = int(input(">>> month: "))
                d2 = int(input(">>> day: "))
                shamsiToMiladi(y2,m2,d2)
            except:
                print("Error!")
        elif work == "6":
            try:
                daysOfLifeMiladi()
            except:
                print("Error!")
        elif work == "7":
            try:
                daysOfLifeShamsi(year,month,day)
            except:
                print("Error!")
        else:
            print("You should enter number of each parameter!")
    elif firstQ == "3":

        # ============= inputs and texts =============

        print("[1] English")
        print("[2] Persian")
        print("[3] Arabic")
        print("[4] French")
        print("[5] German")
        print("[6] Chinese")
        print("[7] Russian")
        print("[8] Spanish")
        searchLang = input(">>> Enter language of your search: ")

        # ============= if =============

        if searchLang == "1":
            try:
                searchEn()
            except:
                print("Error!")
        elif searchLang == "2":
            try:
                searchFa()
            except:
                print("Error!")
        elif searchLang == "3":
            try:
                searchAr()
            except:
                print("Error!")
        elif searchLang == "4":
            try:
                searchFr()
            except:
                print("Error!")
        elif searchLang == "5":
            try:
                searchGe()
            except:
                print("Error!")
        elif searchLang == "6":
            try:
                searchCh()
            except:
                print("Error!")
        elif searchLang == "7":
            try:
                searchRe()
            except:
                print("Error!")
        elif searchLang == "8":
            try:
                searchEs()
            except:
                print("Error!")
    elif firstQ == "4":
        import random

        # ============== first input ==============

        print(termcolor2.colored("\n\nRock Scissor Paper","yellow"))
        OneTwo = "\n[1] Computer \n[2] Player 2\n"
        print(termcolor2.colored(OneTwo,"magenta"))
        b = 0
        try:
            while b < 1:
                first_input = input(">>> Choose your player rival: ") 
                if first_input == "2":
                    print(termcolor2.colored("\n2 Player","yellow"))

                    player_name1 = input("\n>>> Player1! What is your name? ")
                    player_name2 = input("\n>>> Player2! What is your name? ")
                    playerScore1 = 0
                    playerScore2 = 0

                    e = 0
                    try:
                        while e < 1:
                            c = 0
                            while c < 1:
                                print(termcolor2.colored("\n[1] Rock\n[2] Scissor\n[3] Paper\n[0] Back","magenta"))
                                playerMove1 = input(f">>> {player_name1}! Choose: ")
                                if playerMove1 == "1":
                                    playerMove1 = "rock".lower()
                                    c += 1
                                    print(termcolor2.colored("==========\n","red","on_white"))
                                elif playerMove1 == "2":
                                    playerMove1 = "scissor".lower()
                                    c += 1
                                    print(termcolor2.colored("==========\n","red","on_white"))
                                elif playerMove1 == "3":
                                    playerMove1 = "paper".lower()
                                    c += 1
                                    print(termcolor2.colored("==========\n","red","on_white"))
                                elif playerMove1 == "0":
                                    playerMove1 = "0"
                                    c += 1
                                    e += 1
                                else:
                                        print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
                                        print(termcolor2.colored("==========================\n","red","on_white"))
                            f = 0
                            while f < 1:
                                print(termcolor2.colored("\n[1] Rock\n[2] Scissor\n[3] Paper\n[0] Back","magenta"))
                                playerMove2 = input(f">>> {player_name2}! Choose: ")
                                if playerMove2 == "1":
                                    playerMove2 = "rock".lower()
                                    f += 1
                                    print(termcolor2.colored("==========\n","red","on_white"))
                                elif playerMove2 == "2":
                                    playerMove2 = "scissor".lower()
                                    f += 1
                                    print(termcolor2.colored("==========\n","red","on_white"))
                                elif playerMove2 == "3":
                                    playerMove2 = "paper".lower()
                                    f += 1
                                    print(termcolor2.colored("==========\n","red","on_white"))
                                elif playerMove2 == "0":
                                    playerMove2 = "0"
                                    f += 1
                                    e += 1
                                else:
                                    print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                            if playerMove1 == playerMove2:
                                print(termcolor2.colored("Draw!","green"))
                                print(termcolor2.colored("===========","red"))
                                print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                print(termcolor2.colored("==========================\n","red","on_white"))
                                c -= 1
                                f -= 1
                            elif playerMove1 == "rock":
                                if playerMove2 == "scissor":
                                    print(termcolor2.colored(f"Winner: {player_name1}","green"))
                                    playerScore1 += 1
                                    print(termcolor2.colored(f"===========","red"))
                                    print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                                    
                                elif playerMove2 == "paper":
                                    print(termcolor2.colored(f"Winner: {player_name2}","green"))
                                    playerScore2 += 1
                                    print(termcolor2.colored(f"===========","red"))
                                    print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                                c -= 1
                                f -= 1    
                            elif playerMove1 == "scissor":
                                if playerMove2 == "paper":
                                    print(termcolor2.colored(f"Winner: {player_name1}","green"))
                                    playerScore1 += 1
                                    print(termcolor2.colored("===========","red"))
                                    print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                    
                                elif playerMove2 == "rock":
                                    print(termcolor2.colored(f"Winner: {player_name2}","green"))
                                    playerScore2 += 1
                                    print(termcolor2.colored("===========","red"))
                                    print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                                c -= 1
                                f -= 1     
                            elif playerMove1 == "paper":
                                if playerMove2 == "rock":
                                    print(termcolor2.colored(f"Winner: {player_name1}","green"))
                                    playerScore1 += 1
                                    print(termcolor2.colored("===========","red"))
                                    print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                                    
                                elif playerMove2 == "scissor":
                                    print(termcolor2.colored(f"Winner: {player_name2}","green"))
                                    playerScore2 += 1
                                    print(termcolor2.colored("===========","red"))
                                    print(termcolor2.colored(f"{player_name1}: {playerScore1}","yellow"))
                                    print(termcolor2.colored(f"{player_name2}: {playerScore2}","yellow"))
                                    print(termcolor2.colored("==========================\n","red","on_white"))
                                c -= 1
                                f -= 1    
                    except:
                        print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
                    b += 1
                elif first_input == "1":
                    b += 1
                else:
                    print(termcolor2.colored("Try again!","red","on_white"))
        except:
            pass

        if first_input == "1":
            player_name = input("\n>>> What is your name? ")
            computerScore = 0
            playerScore = 0

            p = 0
            try:
                while p < 1:
                    computerMove = random.randint(1,3)
                    if computerMove == 1:
                        computerMove = "rock"
                    elif computerMove == 2:
                        computerMove = "paper"
                    elif computerMove == 3:
                        computerMove = "scissor"
                    d = 0
                    while d < 1:
                        print(termcolor2.colored("\n[1] Rock\n[2] Scissor\n[3] Paper\n[0] Back","magenta"))
                        playerMove1 = input(">>> Choose: ")
                        if playerMove1 == "1":
                            playerMove = "rock".lower()
                            d += 1
                        elif playerMove1 == "2":
                            playerMove = "scissor".lower()
                            d += 1
                        elif playerMove1 == "3":
                            playerMove = "paper".lower()
                            d += 1
                        elif playerMove1 == "0":
                            playerMove = "0"
                            d += 1
                        else:
                            print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
                            print(termcolor2.colored("==========================\n","red","on_white"))
                            
                    if computerMove == playerMove:
                        print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                        print(termcolor2.colored("Draw!","green"))
                        print(termcolor2.colored("===========","red"))
                        print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                        print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                        print(termcolor2.colored("==========================\n","red","on_white"))
                    
                    elif playerMove == "rock":
                        if computerMove == "paper":
                            print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                            print(termcolor2.colored(f"Winner: Computer","green"))
                            computerScore+=1
                            print(termcolor2.colored("===========","red"))
                            print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                            print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                            print(termcolor2.colored("==========================\n","red","on_white"))
                        elif computerMove == "scissor":
                            print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                            print(termcolor2.colored(f"Winner: {player_name}","green"))
                            playerScore+=1
                            print(termcolor2.colored("===========","red"))
                            print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                            print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                            print(termcolor2.colored("==========================\n","red","on_white"))

                    elif playerMove == "scissor":
                        if computerMove == "paper":
                            print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                            print(termcolor2.colored(f"Winner: Computer","green"))
                            playerScore+=1
                            print(termcolor2.colored("===========","red"))
                            print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                            print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                            print(termcolor2.colored("==========================\n","red","on_white"))
                        elif computerMove == "rock":
                            print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                            print(termcolor2.colored(f"Winner: {player_name}","green"))
                            computerScore+=1
                            print(termcolor2.colored("===========","red"))
                            print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                            print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                            print(termcolor2.colored("==========================\n","red","on_white"))

                    elif playerMove == "paper":
                        if computerMove == "rock":
                            print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                            print(termcolor2.colored(f"Winner: Computer","green"))
                            playerScore+=1
                            print(termcolor2.colored("===========","red"))
                            print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                            print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                            print(termcolor2.colored("==========================\n","red","on_white"))
                        elif computerMove == "scissor":
                            print(termcolor2.colored(f"\nComputer move: {computerMove}","blue"))
                            print(termcolor2.colored(f"Winner: {player_name}","green"))
                            computerScore+=1
                            print(termcolor2.colored("===========","red"))
                            print(termcolor2.colored(f"Player score: {playerScore}","yellow"))
                            print(termcolor2.colored(f"Computer score: {computerScore}","yellow"))
                            print(termcolor2.colored("==========================\n","red","on_white"))
                    elif playerMove == "0":
                        p += 1
                    else:
                        print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
                        print(termcolor2.colored("==========================\n","red","on_white"))
            except:
                print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
    elif firstQ == "5":
        import random

        print(termcolor2.colored("\nGuess number\n","yellow"))

        a = 0 
        while a < 1:
            b = 0
            while b < 1:
                try:
                    distanceS = int(input("\n>>> From what number start: "))
                except:
                    print(termcolor2.colored("Try again!\n","red","on_white"))
                else:
                    b += 1
            c = 0
            while c < 1:
                try:
                    distanceF = int(input(">>> Till what number finish: "))
                except:
                    print(termcolor2.colored("Try again!\n","red","on_white"))
                else:
                    c += 1
            if distanceF < distanceS:
                computerNum = random.randint(distanceF,distanceS)
            else:
                computerNum = random.randint(distanceS,distanceF)
            d = 0
            while d < 1:
                try:
                    print(termcolor2.colored("\n[Start number - 1] Quit","magenta"))
                    guess = int(input("\n>>> Enter your guess: "))
                except:
                    print(termcolor2.colored("Try again!\n","red","on_white"))
                else:
                    if guess == computerNum:
                            print(termcolor2.colored(f"Well done! your number was: {computerNum}","green"))
                            print(termcolor2.colored("===============\n","red"))
                            d += 1
                    elif guess == (distanceS - 1):
                            d += 1
                            a += 1
                    elif guess < computerNum:
                            print(termcolor2.colored(f"It is higher than {guess}","blue"))
                            print(termcolor2.colored("===============\n","red"))
                    elif guess > computerNum:
                            print(termcolor2.colored(f"It is lower than {guess}","blue"))
                            print(termcolor2.colored("===============\n","red"))
            if guess != (distanceS - 1):
                f = 0
                while f < 1:
                    exit = input("\n>>> DO you want to exit?y/n: ")
                    if exit == "y":
                            f += 1
                            a += 1
                    elif exit == "n":
                            f += 1
                    else:
                            print(termcolor2.colored("Try again!\n","red","on_white"))

        a = 0;b = 0;c = 0;d = 0;f = 0
    elif firstQ == "6":

        # ============= inputs and texts =============

        print(termcolor2.colored("[1] English","magenta"))
        print(termcolor2.colored("[2] Japanese","magenta"))
        print(termcolor2.colored("[3] Arabic","magenta"))
        print(termcolor2.colored("[4] French","magenta"))
        print(termcolor2.colored("[5] German","magenta"))
        print(termcolor2.colored("[6] Chinese","magenta"))
        print(termcolor2.colored("[7] Russian","magenta"))
        print(termcolor2.colored("[8] Spanish","magenta"))
        searchLang = input(">>> Enter language of your search: ")

        # ============= if =============

        if searchLang == "1":
            try:
                searchEn()
            except:
                print("Error!")
        elif searchLang == "2":
            try:
                searchJa()
            except:
                print("Error!")
        elif searchLang == "3":
            try:
                searchAr()
            except:
                print("Error!")
        elif searchLang == "4":
            try:
                searchFr()
            except:
                print("Error!")
        elif searchLang == "5":
            try:
                searchGe()
            except:
                print("Error!")
        elif searchLang == "6":
            try:
                searchCh()
            except:
                print("Error!")
        elif searchLang == "7":
            try:
                searchRe()
            except:
                print("Error!")
        elif searchLang == "8":
            try:
                searchEs()
            except:
                print("Error!")
    elif firstQ == "7":
        import os

        print(termcolor2.colored("\n\nShut Down","yellow"))

        try:
            a = 0
            while a < 1:
                b = 0
                print(termcolor2.colored("\n[1] Shut Down","magenta"))
                print(termcolor2.colored("[2] Restart","magenta"))
                print(termcolor2.colored("[0] Quit","magenta"))
                while b < 1:
                    firstInput = input("\n>>> Choose: ")
                    if firstInput == "1":
                        os.system('shutdown -s')
                        b += 1
                    elif firstInput == "2":
                        os.system('shutdown -r')
                        b += 1
                    elif firstInput == "0":
                        b += 1
                        a += 1
                    else:
                        print(termcolor2.colored("Try again","red","on_white"))
        except:
            print(termcolor2.colored("Error","red","on_white"))
    elif firstQ == "8":
        change_wallpaper()
    elif firstQ == "0":
        a += 1
