#Initialisers
p1Points = 0
P2Points = 0
rolls = 0

#Opens Files
u = open("users.txt","a")
p = open("passwords.txt","a")

#function signing up
def SignUp():
    user = input("Enter User one Name")
    passwords = input("Enter User One Password. (Must Be Larger Than Three Letters)")
    while len (passwords)< 3:
        passwords = input("Error")
    user2 = input("Enter User Two")
    while user2 == user:
        user2 = input("Error")
    passwords2 = input("Enter Password Two")
    while len (passwords2)< 3:
        passwords2 = input("Error")
    u.write(user+"\n")
    u.write(user2+"\n")
    p.write(passwords+"\n")
    p.write(passwords2+"\n")
u.close()
p.close()

#function Sign In
def SignIn():
    user = input("Enter User One")
    password = input("Enter Password")
    user2 = input("Enter User Two")
    while user2 == user:
        user2 = input("Error")
    password2 = input("Enter Password Two")

NtSu = input("Do You Have An Account").title()
if NtSu == "Yes":
    SignIn()
elif NtSu == "Y":
    SignIn()
elif NtSu == "No":
    SignUp()
elif NtSu == "N":
    SignUp()
else:
    quit()

#Rules
print("The Rules:\nEvery Player Has 5 Rolls\nIf You Roll an Even Number you get 10 points, and If You Roll a Odd Number lose 5 Points\nWhat you get is added to your score")

#The Rolls
rolls = 0
while rolls > 5:
    number = random.randint(1,6)
    playOneRoll = input("Player 1 Roll. Yes or No").title()
    if playOneRoll == "Yes":
        print(number)
        if number <6:
            p1Points= p1Points + number
            check = number %2
            if check %2:
                p1Points = p1Points + 10
            else:
                p1Points = p1Points - 5
        elif number == 6:
            p1Points = p1Points + number
            number = random.randint(1,6)
            print(number)
            p1Points = p1Points + number
    else:
        quit()
    number = random.randint(1,6)
    playTwoRoll = input("Player 2 Roll. Yes or No").upper()
    if playTwoRoll == "Yes":
        print(number)
        if number <6:
            P2Points= P2Points + number
            check = number %2
            if check %2:
                P2Points = P2Points + 10
            else:
                P2Points = P2Points - 5
        elif number == 6:
            P2Points = P2Points + number
            number = random.randint(1,6)
            print(number)
            P2Points = P2Points + number
    else:
        quit()
    rolls = rolls + 1   
print("Every Person has had 5 rolls")