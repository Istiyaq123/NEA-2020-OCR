#initialiser
p1_score = 0
p2_score = 0
roll = 0

#import random
import random

#define login
def login():
    usernameone = input('Enter Username One Username: ')
    passwordone = input('Enter Username One Password: ')
    usernametwo = input('Enter Username Two Username: ')
    while usernameone == usernametwo:
        usernametwo = input('Error ')
    passwordtwo = input('Enter Username Two Password: ')

#define logup
def logup():
    usernameone = input('Enter Username One: ')
    passwordone = input('Enter Username One Password (Must be more than 3 letters): ')
    while len(passwordone)<3:
        passwordone = input('Error ')
    usernametwo = input('Enter Username Two: ')
    while usernameone == usernametwo:
        usernametwo = input('That name has arealdy been signed up ')
    passwordtwo = input('Enter Username Two Password (Must be more than 3 letters): ')
    while len(passwordtwo)<3:
        passwordtwo = input('Error ')

#define play()
def play():
    number = random.randint(1,6)
    p1_roll = input('Player One Roll. Yes or No').title()
    if p1_roll == 'Yes':
        print(number)
        if number <6:
            p1_score = p1_score + number
            check = number %2
            if check %2:
                p1_score = p1_score + 10
            else:
                p1_score = p1_score - 5
        elif number == 6:
            p1_score = p1_score + number
            number = random.randint(1,6)
            print(number)
            p1_score = p1_score + number


#Loging in or loging up
log = input('Do you have an account? ').title()
if log == 'Yes':
    login()
elif log == 'Y':
    login()
elif log == 'No':
    logup()
elif log == 'N':
    logup()
else:
    print('Program has crashed.\nPlease try again.')
    quit()

#Rules
print('\nEvery player has 5 rolls')
print('If you roll and even number ten points is added to your score\nIf you roll and odd number 5 points is subtracted from your score')

#Play

play()