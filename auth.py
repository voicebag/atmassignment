#register
#username, password, email
#generation of user account

#login
#account number and password

#Bank bankOperations
# withdrawal, deposit, complaints 

import random
#database =
database = {}

#Initializing the system
def init():
    print('Welcome to Bank Django')
    print('Do you have an account with us?')
    haveAccount = int(input('select 1 if you have an account with us or select 2 if not \n'))
    if (haveAccount == 1):
        login()
    elif (haveAccount == 2):
        register()
    else:
        print('You have pressed the wrong response. Try again.')
        init()


#Bank operations
def login():
    print('Welcome, login into your account')

    yourAccountNo = int(input('Your account number \n'))
    yourPassword = input('Your password \n')
    for accountNumber,userDetails in database.items():
        if(accountNumber == yourAccountNo):
            if(userDetails[3] == yourPassword):
                print("Your login is successful")
                bankOperations(userDetails)

    print('Invalid account or password')
    login()



def register():
    print('*******Register*******')
    email = input('What is your email address? \n')
    fname = input('What is your first name? \n')
    lname = input('What is your last name? \n')
    password = input('create a password \n')

    accountNumber = generateAccountNo()


    database[accountNumber] = [fname, lname, email, password]

    print('Your account has been created')
    print('*****   *****   *****    ****')
    print('Your Account number is: %d' % accountNumber)
    print('Make sure you keep it safe')
    print('*****   *****   *****    ****')

    login()

def bankOperations(user):
    print('Welcome %s %s ' % ( user[0], user[1] ) )

    opOption = int(input('What do you like to do? (1) deposit (2) withdrawal (3) logout (4) exit \n'))
    if (opOption == 1):
        depositOperation()
    elif(opOption == 2):
        withdrawalOperation()
    elif(opOption == 3):
        logout()
    elif(opOption == 4):
        exit()
    else:
        print('Invalid option selected')
        bankOperations(user)


def withdrawalOperation():
    print('withdrawal operation')

def depositOperation():
    print('Deposit operation')

def logout():
    login()

def generateAccountNo():
    print('This is to generate account no.')
    return random.randrange(1111111111, 9999999999)


init()
