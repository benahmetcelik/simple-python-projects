import json,random
accounts_file_path = 'accounts.json'
accounts_file = open(accounts_file_path)
accounts = json.load(accounts_file)
online_user = {}
username = ''
new_user_information = {
    "accountId": 0,
        "username": "",
        "accountName": "",
        "password": "",
        "accountBalance": 0,
        "lastActions": []
}

COLOR_RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"


def question(text):
   return input(YELLOW + str(text) + COLOR_RESET)

def alert(text):
    print(RED + str(text) + COLOR_RESET)

def success(text):
    print(GREEN + str(text) + COLOR_RESET)
def normalText(text):
    print(BLUE + str(text) + COLOR_RESET)
def title(text):
    print(PURPLE + str(text) + COLOR_RESET)



def selectAction():
    return int(question('Your Action ? \n'))
   
def createAccountScreen():
    username = str(question('Username : \n'))
    accountName = str(question('Your Name : \n'))
    password = str(question('Password (Only Numbers) : \n'))
    global new_user_information
    new_user_information['accountBalance'] = 0
    new_user_information['username'] = username
    new_user_information['accountName'] = accountName
    new_user_information['password']= password
    new_user_information['accountId'] = random.randint(1,55555555)
    new_user_information['lastActions'] = []

    global accounts
    updated_data = []
    for account in accounts: 
        updated_data.append(account)   

    updated_data.append(new_user_information)    
    updated_json = open(accounts_file_path,'w')
    updated_json = json.dump(updated_data,updated_json,indent=4)
    new_user_information = {}
    accounts_file = open(accounts_file_path)
    accounts = json.load(accounts_file)
    loginScreen()

def welcomeScreen():
    title('Welcome To Simple Bank')
    normalText('Please Choose Your Action')
    normalText('1 = Create Account | 2 = Login Account | 3 = Quit')
    selectActionValue = selectAction()
    if(selectActionValue == 2):
       loginScreen()
    elif(selectActionValue == 1):
        createAccountScreen()   
    else:
       quit()
       
def dashboard():
  
    global online_user
    title('Welcome To Simple Bank '+ username)
    normalText('these are the operations you can perform.')
    normalText('1 = Change Password , 2 = Change Username , 3 = Learn Balance , \n 4 = Get Money , 5 = Send Money , 6 = Deposit Money , 7 = Quit System')

    match selectAction():
        case 1:
            updateField('password')
        case 2 :
            updateField('username')
        case 3:
            success('your balance is : '+str(online_user['accountBalance']))
            dashboard()
        case 4:
           
            if online_user['accountBalance'] < 1 :
                alert('you havent money')
            else:    
                withdrawMoney()
        case 5:
            sendMoney()
        case 6:
            depositMoney()
        case 7:
            online_user = {}
            welcomeScreen()
        case _:
            alert('please select a valid transaction')  
            dashboard()     


def sendMoney():
    buyerUserId = int(question('Please enter buyer user id number \n'))
    amount = int(question('Please enter amount for the transfer'))
    if amount < 1:
        print('Transfer amount not been 0')
    else:
        user_exist = False
        for account in accounts:
            if int(account['accountId']) == buyerUserId:
                user_exist = True

        if not user_exist:
            print('User not found, please try again')
            sendMoney()
        else:
            online_user['accountBalance'] = online_user['accountBalance'] - amount
            updateJson()
            updated_data_transfer = []

            for account in accounts:
                if int(account['accountId']) == buyerUserId:
                   account['accountBalance']=account['accountBalance']+amount
                   updated_data_transfer.append(account)   
                else:
                    updated_data_transfer.append(account)

            
            updated_json = open(accounts_file_path,'w')
            updated_json = json.dump(updated_data_transfer,updated_json,indent=4)

            print('Action Success!')
            dashboard()
def withdrawMoney():
    print('your current balance is '+str(online_user['accountBalance'])+' TRY')
    withdrawMoneyAmount = int(question('How many TRY do you want to withdraw?'))
    if withdrawMoneyAmount > online_user['accountBalance']:
        print('you don\'t have enough money')
        withdrawMoney()
    else:
        online_user['accountBalance'] = online_user['accountBalance']-withdrawMoneyAmount
        updateJson()
        print(str(withdrawMoneyAmount)+' TRY money has been withdrawn from your account. Your current balance is '+str(online_user['accountBalance'])+' TRY')
        dashboard()
def depositMoney():
    print('your current balance is '+str(online_user['accountBalance'])+' TRY')
    depositMoney = int(question('How many TRY do you want to deposit?'))
    online_user['accountBalance'] = online_user['accountBalance']+depositMoney
    updateJson()
    print(str(depositMoney)+' TRY money has been deposit from your account. Your current balance is '+str(online_user['accountBalance'])+' TRY')
    dashboard()
def loginScreen():
    username = str(question('Username : '))
    password = str(question('Password : '))
    login(username,password)

def login(username,password):
    for account in accounts:
        if (account['username'] == username and account['password'] == password):
            global online_user
            online_user = account
            dashboard()
    alert('Wrong Information !!')
    loginScreen()
def updateField(field_name):
    if online_user[field_name] !=  str(question('Please enter the current '+field_name)) :
        alert('Wrong '+field_name)
        updateField(field_name)
    new_field = question('Please enter the new '+field_name)
    new_field_validate = question('Please again enter the new '+field_name)  
    if new_field != new_field_validate:
        alert('Wrong Information')
        updateField(field_name)
    online_user[field_name] = str(new_field)
    updateJson()
    print('your '+field_name+' changed')
    dashboard()  
def updateJson():
    updated_data = []
    for account in accounts:
        if account['accountId'] == online_user['accountId']:
            account = online_user 
        updated_data.append(account)   
    updated_json = open(accounts_file_path,'w')
    updated_json = json.dump(updated_data,updated_json,indent=4)
welcomeScreen()