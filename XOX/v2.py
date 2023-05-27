wood = [
    ['1','2','3'],
    ['4','5','6'],
    ['7','8','9']
]

user_choose =0
x_or_o = True
counter = 0

array_test = []

array_test.append(
    
)

print('Game Start')

def game():
    winnerCheckLine()
    winnerCheckColumn()
    global counter,user_choose,x_or_o
    
    for i in range(0,len(wood)):
        print(wood[i])
    user_choose = input('Kutu : ')
    user_choose = int(user_choose)-1 if user_choose else -1
    quotient, remainder = divmod(user_choose, 3)
    if user_choose  > -1:
        if wood[quotient][remainder] != 'X' or wood[quotient][remainder] != 'O':
            wood[quotient][remainder] =  'X' if x_or_o else 'O'
            x_or_o = not x_or_o
       
    else:
        print('Geçerli bir seçim yapınız')
        
    game()


def debug():
    print('Buradasın')

def winnerCheckCross():
    one_to_nine =0
    three_to_seven =0
    row_counter =0
    for i in range(0,len(0,wood)):
        
        for sub_i in range(0,len(0,wood[i])):
            if wood[i][row_counter] == 'X':
                one_to_nine+=1
                row_counter+=1
                continue
        print(row_counter)    

def winnerCheckLine():
    

    for i in range(0,len(wood)):
        line_x_control =0
        line_o_control =0
        for sub_i in range(0,len(wood[i])):
            
            if wood[i][sub_i] == 'X':
                line_x_control+=1
            elif wood[i][sub_i] == 'O':
                line_o_control+=1

        if line_x_control > 2:
            winner('X')
        elif line_o_control > 2:    
            winner('O')

def winnerCheckColumn():
    column_control ={
        'X':0,
        'O':0
    }
    for i in range(0,len(wood)):
        for sub_i in range(0,len(wood[i])):

            if wood[i][sub_i] == 'X':
                column_control['X'] +=1
            elif wood[i][sub_i] == 'O':
                column_control['O'] +=1  

        if column_control['X'] == 3:
            winner('X')    
        elif column_control['O'] == 3:
            winner('O')    

def winner(winner_name):
    if winner_name:
        print('Winner is a '+winner_name)
    else:
        print('Winner is a '+ winner_name)    
    quit()    



game()