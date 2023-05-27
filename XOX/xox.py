wood = [
   
        [1],[2],[3],
   
        [4],[5],[6],
    
        [7],[8],[9],
     
]

select_box= 2
one_line = []
x_or_o= True

def game():
    global wood,select_box,one_line,x_or_o
    for i in range(0,len(wood)):
        if select_box > -1 and select_box < 10:
           
            if  wood[select_box] == 'X' or wood[select_box] == 'O':
               # one_line.append(wood[select_box])
               print('a')
            else:
                x_or_o = not x_or_o
                wood[select_box] = 'X' if x_or_o else 'O'
                one_line.append(wood[select_box])
               
            select_box = -1       
        else:
            one_line.append(wood[i])
            select_box = -1

        if len(one_line) % 3 == 0:
            print(str(one_line)+'\n')  
            one_line = []  
            #select_box = -1

    
    
    #select_box = int(input('Select Box : (for : '+('X' if not x_or_o else 'O')+')'))-1
   # game()



game()    