death_row = [
'========|===========|\n',
'========O===========|\n',
'=======/|\==========|\n',
'=======/=\==========|\n',
'====================|\n',
'====================|\n',

]


new_canvas = []


def drawDeathRow(errorCount):
    global new_canvas
    if errorCount == 6:
        print(''.join(death_row))
    else:
        new_canvas = []
        for i in range(0,errorCount):
            new_canvas.append(death_row[i]+'\n')

        print(''.join(new_canvas))



    