import random
random_number = 0
user_guess = 0

def welcome():
    generateNumber()
    print('Hoşgeldiniz ! \nBir Sayı tuttum tahmin edebilir misin ?')   
    global user_guess
    user_guess = int(input('Your Guess : '))  
    matchInput()

def tryAgain():
    global user_guess
    user_guess = int(input('Your Guess : '))
    matchInput() 

def matchInput():
    if user_guess < random_number:
        print('Daha yüksek bir rakam :)')
        tryAgain()
    elif user_guess > random_number:
        print('Daha küçük bir rakam')
        tryAgain()
    elif user_guess == random_number:
        print('Tebrikler DOğru Bildiniz')
        welcome()
    else:
        print('Tanımsız işlem')   
        welcome() 

def generateNumber():
        global random_number
        random_number = random.randint(1,500)


welcome()