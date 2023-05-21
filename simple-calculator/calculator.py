first_number = int(input('First Number :'))
second_number = int(input('Second Number :'))
operator = input('Operator :')

def switch(operator):
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number*second_number
    elif operator == '/':
        return first_number/second_number
    else:
        return 'Invalid Operator !!'

        
if type(switch(operator)) != 'str':
    print('Your Result is a : '+ str(switch(operator)))
else:
    print(switch(operator))
        