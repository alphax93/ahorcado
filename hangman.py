import random

board=[['  ','+-','--','+',],
       ['  ','| ','  ','|',],
       ['  ','| ','  ',' ',],
       ['  ','|  ',' ',' ','  '],
       ['  ','| ','  ',' ',],
       ['  ','|  ','  ',' ','  '],
       ['  ','| ','  ','  '],
       ['======'],]

def print_row(row):
    for x in row:
        print(x,end='')
    print('')
    
def print_board(board):
    for row in board:
        print_row(row)
        

def choose_word():
    with open('sowpods.txt','r') as f:
        words=list(f)
    return random.choice(words).strip()

def check_letter(word,letter):
    if letter in word:
        return True    
    return False

def fill_word(word,secret_word,letter):
    last=0
    for c in secret_word:
        if c == letter:
            index = secret_word.index(c,last)
            word[index]=c
            last=index+1
    
def add_part(board,chances):
    if chances==6:
        board[2][3]='O'
    elif chances==5:
        board[3][3]='|'
        board[4][3]='|'
    elif chances==4:
        board[3][2]='/'
    elif chances==3:
        board[3][4]='\\'
    elif chances==2:
        board[5][2]='/'
    elif chances==1:
        board[5][4]='\\'


print("Vamos a jugar al Ahorcado")
secret_word = choose_word()
word='_' * len(secret_word)
secret_word=list(secret_word)
word=list(word)
used=[]
chances=6
solved=False
print_board(board)
while not solved and chances>0:
    
    print(" ".join(word))
    letter = input("Elige una letra: ").upper()
    if letter in used:
        print("*****Ya has usado esa letra*****")
    elif check_letter(secret_word,letter):
        fill_word(word,secret_word,letter)
        used.append(letter)
        if '_' not in word:
            solved=True
    else:
        print("Esa letra no está en la palabra secreta")
        add_part(board,chances)
        used.append(letter)
        chances-=1

    print_board(board)
    
if solved:
    print("¡¡¡FELICIDADES!!! Has encontrado la palabra secreta: " + " ".join(word) )
else:
    print("¡¡¡NOOOO!!! HAS MATADO A KENNY")
