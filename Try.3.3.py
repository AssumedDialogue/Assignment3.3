import sys #import used to exit code

class Bank: #creates accounts
    def __init__(self):
        self.BankName = "Areeba's Bank"
    def openAccount(self):
        Michelangelo=Account("10438391","Michelangelo", 4, 1200, SavingAccount(1000), CheqAccount(500))
        Leonardo=Account("24565421","Leonardo", 4, 2200, SavingAccount(1000), CheqAccount(500))
        Donatello=Account("31445473","Donatello", 4, 3200, SavingAccount(1000), CheqAccount(500))        
        Raphael=Account("44800114","Raphael", 4, 4200, SavingAccount(1000), CheqAccount(500))
        Splinter=Account("50927581","Splinter", 4, 5200, SavingAccount(1000), CheqAccount(500))
        
        self.list=[Michelangelo, Leonardo, Donatello, Raphael, Splinter]
        return self.list


class Account: #initalizes the variables for the selected object account
    def __init__(self, num, name, roi, balance, sav, chq):
        self.num=num
        self.name=name
        self.roi=roi
        self.balance=balance
        self.sav=sav
        self.chq=chq
    def deposit(self): #deposit function
        while True:
            try:
                amnt=int(input("Enter amount you would like to deposit: "))
                choice= int(input("For savings account Enter 1: "+ '\n' +"For chequing account Enter 2: "))
            except ValueError:
                continue
            if choice==1 :
                self.sav.sdeposit(amnt)
            elif choice ==2:
                self.chq.cdeposit(amnt)
            else:
                print('\n'+"Sorry you did not enter a valid option please try again")

    def withdraw(self): #withdrawl function
        while True:
            try:
                amnt=int(input("Enter the amount you would like to withdraw: "))
                choice= int(input("For savings account Enter 1: "+'\n' +"For chequing account Enter 2: "))
            except ValueError:
                continue
            if (choice==1) and ((self.balance-amnt)>= self.sav):
                self.sav.swithdraw(amnt)
            elif choice ==2:
                self.chq.cwithdraw(amnt)
            else:
                print('\n'+"Sorry you did not enter a valid option please try again")
    def getBalance(self): #sends current Balance
        return ('\n'"Your current balance is: ",self.balance)
    def getID(self):    #sends the id number
        return self.num
    def getName(self): #sends the name
        return self.name


class SavingAccount:  #the savings account function
    def __init__(self, min):
        self.min=min
    def sdeposit(self,amnt): #deposit for savings
        self.min=min+amnt
        return ("Your current amount in savings account: ",self.min)
    def swithdraw(self,amnt): #withdraw for savings
        self.min=min-amnt
        return ("Your current amount in savings account: ",self.min)

class CheqAccount:  #the chequing account functions
    def __init__(self, min):
        self.min=min
    def cdeposit(self, amnt): #deposit for chequing
        self.min=min+amnt
        return ("Your current amount in chequing account: ",self.min)
    def cwithdraw(self,amnt): #withdraw for chequing
        self.min=min-amnt
        return ("Your current amount in chequing account: ",self.min)


class Program: #handles the interaction with the user
    def showAccountMenu(self): #account actions menu
        while True: #loops if error occurs
            try:
                self.User3=input('\n'+"Select one from the following menu:"+'\n'+"1. Check balance"+'\n'+"2. Deposit"+'\n'+"3. Withdraw Money"+'\n'+"4. Exit Account")
            except ValueError:
                continue
            if self.User3 == "1":
                myBank=Bank()
                list=myBank.openAccount()
                print(list[self.i].getBalance())
                break
            elif self.User3 == "2":
                myBank=Bank()
                list=myBank.openAccount()
                print(list[self.i].deposit())
                break
            elif self.User3 == "3":
                myBank=Bank()
                list=myBank.openAccount()
                print(list[self.i].withdraw())
                break
            elif self.User3 == "4":
                Program.showMainMenu(self)
                break
            else:
                print('\n'+"Sorry you did not enter a valid option please try again")    

    def showMainMenu(self): #main display menu
        self.MMChoice= ("1","2")
        while True:
            try:
                self.user1 = input('\n'+"Welcome to the Bank! (please select an option)"+'\n'+"1. Select account (type 1)"+'\n'+"2. Exit Program (type 2)")
            except ValueError:
                continue
            if self.user1 == "1":
                self.SAChoice= ("10438391","24565421","31445473","44800114","50927581")
                while True:
                    try:
                        self.User2 = input('\n'+"Select an Account from the following menu:"+'\n'+"1.10438391 "+'\n'+"2.24565421 "+'\n'+"3.31445473 "+'\n'+"4.44800114 "+'\n'+"5.50927581 ")
                    except ValueError:
                        continue
                    if self.User2 in self.SAChoice:
                        myBank=Bank()
                        list=myBank.openAccount()
                        self.i=0
                        while True:
                            if list[self.i].getID() == self.User2:
                                Program.showAccountMenu(self)
                                break
                            else:
                                self.i=+1
                    else:    
                        print('\n',"Sorry you did not enter a valid option please try again")

            elif self.user1 == "2":
                sys.exit()
            else:
                print('\n'+"Sorry you did not enter a valid option please try again")

p=Program()
p.showMainMenu()   #calls the program main menu



