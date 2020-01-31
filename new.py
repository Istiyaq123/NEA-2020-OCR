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

log = input('Do you have an account? ').title()
if log == 'Yes':
    login()
elif log == 'Y':
    login()
elif log == 'No':
    logup()
elif log == 'N':
    logup()