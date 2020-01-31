#Function for loging up
def logup():
    users = open('users.txt','a')
    usernameOne = input('What is your name ')
    usernameOneP = input('What is your password. Note it must be larger than 3 letters ')
    Ua = ('\n'+usernameOne + '\t' + usernameOneP)
    users.write(Ua)
    while len(usernameOneP) < 3:
        usernameOneP = input('Error ')
        Ua = ('\n'+usernameOne + '\t' + usernameOneP)
        users.write(Ua)
    users.close()

def login():
    users = open('users.txt','r')
    usernameone = input('What is your name')
    usernameonepassword = input('What is your password')
    Ua = (usernameone + '\t' + usernameonepassword)
    users.close()

#Ask The User if they Have an Account
log = input('Do You Have an Account ').title()
if log == 'Yes':
    login()
elif log == 'Y':
    login()
elif log == 'No':
    logup()
elif log == 'N':
    logup()
else:
    print('Program Has Crashed, Please Try Again')
    quit()
