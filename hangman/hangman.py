import random,json
import man as man

prepare_word = None
word_count = None
empty_word = []
erroCount =0

with open("words.json", "r") as dosya:
    words = json.load(dosya)['words']




def welcome():
    global prepare_word,word_count,empty_word
    total_words = len(words)
    select_rand_word = words[random.randint(0,total_words-1)]

    prepare_word = list(select_rand_word)
    word_count = len(prepare_word)
    
    empty_word = []
    for i in range(0,word_count):
        empty_word.append('_')
    
    print(''.join(empty_word)+'\n')
    userInput()

    



def userInput():
    global empty_word,erroCount
    if erroCount == 6:
        print('Adam Öldü !\n')
        
        print('Kelilmen : '+str(''.join(prepare_word)))
        man.drawDeathRow(erroCount)
       
        newGame()

    
    if empty_word.count('_') == 0 :
        print('Tebrikler kazandınız !\n')
        newGame()
    else:    
        user_input = input('Harf giriniz : ')
        sira = []
        for indeks, eleman in enumerate(prepare_word):
            if eleman == user_input:
                sira.append(indeks)

        if not user_input in prepare_word:
            erroCount +=1
            man.drawDeathRow(erroCount)
            print('harf bulunamadı adamın uzvu gitti \n')
        else:
          
            for i in range(0,word_count):
                if i in sira:
                    if empty_word[i] == '_':
                        empty_word[i]= prepare_word[i]
            man.drawDeathRow(erroCount)
               

        print(''.join(empty_word)+'\n')
        userInput()


def newGame():
    global erroCount
    new_game= input('Yeni Oyun İster Misiniz ? (E/H)').upper()
    if new_game == 'E':
        erroCount =0
        welcome()
    else:
        exit(0)    

welcome()    