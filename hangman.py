import os
from random import choice

def cls():
    os.system("cls")


def hang(status):
    if status==0:
        print('  ----------+')
        print('  |         |')
        print('  |')
        print('  |')         
        print('  |')   
        print('  |') 
        print('  |') 
        print('  |')
        print('  |_________________')    
    elif status==1:
        print('  ----------+')
        print('  |         |')
        print('  |        ( )')
        print('  |')         
        print('  |')   
        print('  |') 
        print('  |') 
        print('  |')
        print('  |_________________')      
    elif status==2:
        print('  ----------+')
        print('  |         |')
        print('  |        ( )')
        print('  |       / | \\ ')         
        print('  |')   
        print('  |') 
        print('  |') 
        print('  |')
        print('  |_________________')       
    elif status==3:
        print('  ----------+')
        print('  |         |')
        print('  |        ( )')
        print('  |       / | \\')         
        print('  |         |')   
        print('  |') 
        print('  |') 
        print('  |')
        print('  |_________________')      
    elif status==4:
        print('  ----------+')
        print('  |         |')
        print('  |        ( )')
        print('  |       / | \\')         
        print('  |         |')   
        print('  |         |') 
        print('  |') 
        print('  |')
        print('  |_________________')   
    else:
        print('  ----------+')
        print('  |         |')
        print('  |        ( )')
        print('  |       / | \\')         
        print('  |         |')   
        print('  |         |') 
        print('  |        / \\') 
        print('  |')
        print('  |_________________')     
                 
     
                 
                

words=["apple","orange","burry"]
random_word=choice(words)

word_list=[]
for i in random_word:
    word_list.append(i)
 

hide=[]
for i in range(len(random_word)):
    hide.append('___')

print("#############")
print("HANGMAN GAME")
print("#############")
print("Are you ready to play?")
input("just press the enter to start")
cls()
error=[]
while len(error)<=5:
    hang(len(error))
    print(f'correct word:{" ".join(hide)}')
    print(f'wrong inputs:{",".join(error)}')
    a=input("input the letter:")
    if a in word_list:
        hide[word_list.index(a)]=a
        word_list[word_list.index(a)]=" "
    else:
        error.append(a)
        print(f'it was a wrong choice')
    if random_word == ''.join(hide):
        print('You won!')
        break
    cls()
else:
    print(f'you lose ')
        

