import pyfiglet
import termcolor2

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
        import math
        # ============= functions(calculator) =============
        def plus(x,y):
            result = x + y
            res = termcolor2.colored(result,"red")
            print(f"{x} + {y} = {res}")
            
        def minus(x,y):
            result = x - y
            res = termcolor2.colored(result,"red")
            print(f"{x} - {y} = {res}")

        def multy(x,y):
            result = x * y
            res = termcolor2.colored(result,"red")
            print(f"{x} × {y} =  {res}")

        def dev(x,y):
            result = x / y
            res = termcolor2.colored(result,"red")
            print(f"{x} ÷ {y} = {res}")

        def sqrtfunc(x):
            result = math.sqrt(x)
            res = termcolor2.colored(result,"red")
            print(f"Result is: {res}")

        def tavan(x,y):
            result = x ** y
            res = termcolor2.colored(result,"red")
            print(f"{x} ^ {y} = {res}")

        def tangent(x):
            result = math.tan(x)
            res = termcolor2.colored(result,"red")
            print(f"tangent of {x} = {res}")

        # ============= run func =============

        def runcalc():
            termcolor2.colored("\n\nCalculator","yellow")
            a = 0
            while a < 1:
                try:
                    OneTwo = "\n[1] + \t [2] -"
                    print(termcolor2.colored(OneTwo,"magenta"))
                    ThreeFour = "[3] × \t [4] ÷"
                    print(termcolor2.colored(ThreeFour,"magenta"))
                    five = "[5] sqrt"
                    print(termcolor2.colored(five,"magenta"))
                    six = "[6] forse"
                    print(termcolor2.colored(six,"magenta"))
                    seven = "[7] factorial"
                    print(termcolor2.colored(seven,"magenta"))
                    eight = ("[8] tangent")
                    print(termcolor2.colored(eight,"magenta"))
                    tryAgain = "Try again!"
                    zero = "[0] Quit!"
                    print(termcolor2.colored(zero,"magenta"))

                    z = 0
                    while z < 1:
                        solve = input("\n>>> What do you want to do? ")
                        if solve == "1":
                            first_num = int(input(">>> first number: "))
                            second_num = int(input(">>> second number: "))
                            plus(first_num,second_num)
                            z += 1
                                
                        elif solve == "2":
                            first_num = int(input(">>> first number: "))
                            second_num = int(input(">>> second number: "))
                            minus(first_num,second_num)
                            z += 1

                        elif solve == "3":
                            first_num = int(input(">>> first number: "))
                            second_num = int(input(">>> second number: "))
                            multy(first_num,second_num)
                            z += 1

                        elif solve == "4":
                            first_num = int(input(">>> first number: "))
                            second_num = int(input(">>> second number: "))
                            dev(first_num,second_num)
                            z += 1

                        elif solve == "5":
                            num = int(input(">>> number: "))
                            sqrtfunc(num)
                            z += 1

                        elif solve == "6":
                            first_num = int(input(">>> first number: "))
                            second_num = int(input(">>> second number: "))
                            tavan(first_num,second_num)
                            z += 1

                        elif solve == "7":
                            num = int(input(">>> number: "))
                            a = 1
                            x = num
                            for i in range(1,x+1):
                                a = a * i
                            print(f"factorial of {x} is {a}")
                            z += 1
                        
                        elif solve == "8":
                            num = int(input(">>> number: "))
                            tangent(num)
                            z += 1

                        elif solve == "0":
                            z += 1
                            a += 1
                        else:
                            print(termcolor2.colored(tryAgain,"red","on_white",attrs=["bold"]))
                    z -= 1
                except:
                    print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
            a -= 1
        runcalc()
    elif firstQ == "2":
        import time 
        from jdatetime import JalaliToGregorian
        import datetime as dt
        # import termcolor2

        print(termcolor2.colored("\nTime Tool\n\n","yellow"))

        # ============= variables =============

        todayMiladi = time.localtime()
        year = todayMiladi[0]
        month = todayMiladi[1]
        day = todayMiladi[2]
        hour = todayMiladi[3]
        minute = todayMiladi[4]
        second = todayMiladi[5]
        dayOfWeek = todayMiladi[6]
        dayOfYear = todayMiladi[7]

        # ============= functions(time) =============

        def animalshamsi(year):
            trueYear = year - 7
            if trueYear % 12 == 0:
                print(termcolor2.colored("your birth year is : <Mouse>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 1:
                print(termcolor2.colored("your birth year is : <Cow>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 2:
                print(termcolor2.colored("your birth year is : <Tiger>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 3:
                print(termcolor2.colored("your birth year is : <Rabbit>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 4:
                print(termcolor2.colored("your birth year is : <Dragon>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 5:
                print(termcolor2.colored("your birth year is : <Snake>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 6:
                print(termcolor2.colored("your birth year is : <Houre>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 7:
                print(termcolor2.colored("your birth year is : <Goat>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 8:
                print(termcolor2.colored("your birth year is : <Monkey>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 9:
                print(termcolor2.colored("your birth year is : <Rooster>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 10:
                print(termcolor2.colored("your birth year is : <Dog>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 11:
                print(termcolor2.colored("your birth year is : <Pig>","green"))
                print(termcolor2.colored("================\n","red"))

        def animalmiladi(year):
            trueYear = year - 4
            if trueYear % 12 == 0:
                print(termcolor2.colored("your birth year is : <Mouse>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 1:
                print(termcolor2.colored("your birth year is : <Cow>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 2:
                print(termcolor2.colored("your birth year is : <Tiger>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 3:
                print(termcolor2.colored("your birth year is : <Rabbit>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 4:
                print(termcolor2.colored("your birth year is : <Dragon>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 5:
                print(termcolor2.colored("your birth year is : <Snake>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 6:
                print(termcolor2.colored("your birth year is : <Houre>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 7:
                print(termcolor2.colored("your birth year is : <Goat>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 8:
                print(termcolor2.colored("your birth year is : <Monkey>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 9:
                print(termcolor2.colored("your birth year is : <Rooster>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 10:
                print(termcolor2.colored("your birth year is : <Dog>","green"))
                print(termcolor2.colored("================\n","red"))
            elif trueYear % 12 == 11:
                print(termcolor2.colored("your birth year is : <Pig>","green"))
                print(termcolor2.colored("================\n","red"))

        def todayMiladifunc():
            print(termcolor2.colored("\nGregorian date:","yellow"))
            print(termcolor2.colored(f"{year}/{month}/{day}","green"))
            print(termcolor2.colored(f"\n{hour} : {minute} : {second}","blue"))
            print(termcolor2.colored(f"{dayOfYear} days from {year}\n","green"))

        def gLeapYear(y):
            if (y%4==0) and ((y%100!=0) or (y%400==0)):
                return True
            else: 
                return False

        def sLeapYear(y):
            ary = [1, 5, 9, 13, 17, 22, 26, 30]
            result = False
            b = y%33
            if b in ary: 
                result = True
            return result

        def todayShamsifunc(gyear, gmonth, gday):
            _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            
            deydiffjan = 10
            if gLeapYear(gyear-1):  
                deydiffjan = 11
            if gLeapYear(gyear):  
                gd = _gl[gmonth-1]+gday
            else: 
                gd = _g[gmonth-1]+gday
            
            if gd>79:
                sy = gyear - 621
                gd = gd - 79
                if gd<=186:
                    gmod = gd%31
                    if gmod==0:
                        sd = 31
                        sm = int(gd/31)
                    else:
                        sd = gmod
                        sm = int(gd/31) + 1
                else:
                    gd = gd - 186
                    gmod = gd%30
                    if gmod==0:
                        sd = 30
                        sm = int(gd/30) + 6
                    else:
                        sd = gmod
                        sm = int(gd/30) + 7
            else:
                sy = gyear - 622
                gd = gd+deydiffjan
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 9 
                else:
                    sd = gmod 
                    sm = int(gd/30) + 10 
            # result = [sy, sm, sd]
            # return result
            print(termcolor2.colored("\ntoday is:","yellow"))
            if dayOfWeek == 0:
                print(termcolor2.colored("Monday\n","blue"))
            elif dayOfWeek == 1:
                print(termcolor2.colored("Tuesday\n","blue"))
            elif dayOfWeek == 2:
                print(termcolor2.colored("Wednesday\n","blue"))
            elif dayOfWeek == 3:
                print(termcolor2.colored("Thursday\n","blue"))
            elif dayOfWeek == 4:
                print(termcolor2.colored("Friday\n","blue"))
            elif dayOfWeek == 5:
                print(termcolor2.colored("Saturday\n","blue"))
            elif dayOfWeek == 6:
                print(termcolor2.colored("Sunday\n","blue"))
            print(termcolor2.colored("Shamsi date:","yellow"))
            print(termcolor2.colored(f"{sd}/{sm}/{sy}","green"))

        def miladiToShamsi(gyear, gmonth, gday):
            _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            
            deydiffjan = 10
            if gLeapYear(gyear-1):  
                deydiffjan = 11
            if gLeapYear(gyear):  
                gd = _gl[gmonth-1]+gday
            else: 
                gd = _g[gmonth-1]+gday
            
            if gd>79:
                sy = gyear - 621
                gd = gd - 79
                if gd<=186:
                    gmod = gd%31
                    if gmod==0:
                        sd = 31
                        sm = int(gd/31)
                    else:
                        sd = gmod
                        sm = int(gd/31) + 1
                else:
                    gd = gd - 186
                    gmod = gd%30
                    if gmod==0:
                        sd = 30
                        sm = int(gd/30) + 6
                    else:
                        sd = gmod
                        sm = int(gd/30) + 7
            else:
                sy = gyear - 622
                gd = gd+deydiffjan
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 9 
                else:
                    sd = gmod
                    sm = int(gd/30) + 10 
            # result = [sy, sm, sd]
            # return result
            print(termcolor2.colored(f"\nResult: \n{sd}/{sm}/{sy}\n","green"))

        def shamsiToMiladi(gyear, gmonth, gday):
            gregorian_date_obj = JalaliToGregorian(gyear,gmonth,gday)
            gregorian_date =gregorian_date_obj.getGregorianList()
            d = gregorian_date[0]
            m = gregorian_date[1]
            y = gregorian_date[2]
            print(termcolor2.colored("\nResult:","green"))
            print(termcolor2.colored(f"{d}/{m}/{y}","green"))
            print(termcolor2.colored("==============\n","red"))


        def daysOfLifeMiladi():
            year2 = int(input("\nYear of birth: "))
            month2 = int(input("Month of birth: "))
            day2 = int(input("Day of birth: "))
            year_born =  dt.date(year2,month2,day2)
            input_year = f"{year}.{month}.{day}"
            syear = dt.datetime.strptime(input_year, "%Y.%m.%d")
            days_life = (syear.date()- year_born).days
            if days_life <= 0:
                print('You were not born on this date.')
            else:
                print(termcolor2.colored('\nIt\'s been {} days from birthday!\n'.format(days_life),"green"))

        def daysOfLifeShamsi(gyear,gmonth,gday):
            _gl = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
            _g  = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
            
            deydiffjan = 10
            if gLeapYear(gyear-1):  
                deydiffjan = 11
            if gLeapYear(gyear):  
                gd = _gl[gmonth-1] + gday
            else: 
                gd = _g[gmonth-1] + gday
            
            if gd>79:
                sy = gyear - 621
                gd = gd - 79
                if gd<=186:
                    gmod = gd%31
                    if gmod == 0:
                        sd = 31
                        sm = int(gd/31)
                    else:
                        sd = gmod
                        sm = int(gd/31) + 1
                else:
                    gd = gd - 186
                    gmod = gd%30
                    if gmod==0:
                        sd = 30
                        sm = int(gd/30) + 6
                    else:
                        sd = gmod
                        sm = int(gd/30) + 7
            else:
                sy = gyear - 622
                gd = gd+deydiffjan
                gmod = gd%30
                if gmod==0:
                    sd = 30
                    sm = int(gd/30) + 9 
                else:
                    sd = gmod
                    sm = int(gd/30) + 10
            year2 = int(input("\nYear of birth: "))
            month2 = int(input("Month of birth: "))
            day2 = int(input("Day of birth: "))
            year_born =  dt.date(year2,month2,day2)
            input_year = f"{sy}.{sm}.{sd}"
            syear = dt.datetime.strptime(input_year, "%Y.%m.%d")
            days_life = (syear.date()- year_born).days
            if days_life <= 0:
                print('You were not born on this date.')
            else:
                print(termcolor2.colored('\nIt\'s been {} days from birthday!'.format(days_life),"green"))
                print(termcolor2.colored("==============\n","red"))

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
        import wikipedia

        print(termcolor2.colored("\nWikipedia","yellow"))

        # ============= functions =============
        def searchEn():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("en")
            print(wikipedia.summary(searchText))

        def searchFa():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("fa")
            print(wikipedia.summary(searchText))

        def searchAr():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("ar")
            print(wikipedia.summary(searchText))

        def searchFr():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("fr")
            print(wikipedia.summary(searchText))

        def searchGe():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("de")
            print(wikipedia.summary(searchText))

        def searchCh():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("zh")
            print(wikipedia.summary(searchText))
            
        def searchRe():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("ru")
            print(wikipedia.summary(searchText))

        def searchEs():
            searchText = input(">>> Text: ")
            wikipedia.set_lang("es")
            print(wikipedia.summary(searchText))

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
        from text_to_speech import speak

        print(termcolor2.colored("\n\nText to Speech\n\n","yellow"))
        # ============== functions ==============

        def searchEn():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="en", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="en", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchJa():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="ja", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="ja", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchAr():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="ar", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="ar", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchFr():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="fr", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="fr", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchGe():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="de", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="de", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchCh():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="zh", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="zh", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchRe():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="ru", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="ru", slow=True)
                    w += 1
                else:
                    pass
            w = 0
        def searchEs():
            text = input(">>> Text: ")
            w = 0
            while w < 1:
                save = input(">>> DO you want save it? y/n: ")
                if save == "y":
                    speak("hello", lang="es", slow=True, save=True, file=r"Desktop\filename .mp3")
                    w += 1
                elif save == "n":
                    speak(text, lang="es", slow=True)
                    w += 1
                else:
                    pass

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
        import ctypes
        print(termcolor2.colored("\n\nBackground Changer","yellow"))\

        def change_wallpaper():
            try:
                n = 0
                while n < 1:
                    address = input("\n>>> Enter address of your image: ")
                    value = ctypes.windll.user32.SystemParametersInfoW(20,0,address)
                    print(termcolor2.colored("Background Changed!\n","blue"))
                    print(termcolor2.colored("[1] Change again","magenta"))
                    print(termcolor2.colored("[0] Quit\n","magenta"))
                    m = 0
                    while m < 1:
                        secondInput = input(">>> Choose: ")
                        if secondInput == "1":
                            m += 1
                        elif secondInput == "0":
                            m += 1
                            n += 1
                        else:
                            print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
                n -= 1
                m -= 1
            except:
                print(termcolor2.colored("ٍError!","red","on_white",attrs=["bold"]))
        change_wallpaper()
    elif firstQ == "0":
        a += 1
