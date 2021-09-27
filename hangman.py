import os
from random import choice

def cls():
    os.system("cls")


def hang(status):
    if status==0:
        print('  ----------')
        print('  |')
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
        print('  |')
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
        print('  |')         
        print('  |')   
        print('  |') 
        print('  |') 
        print('  |')
        print('  |_________________')      
    elif status==3:
        print('  ----------+')
        print('  |         |')
        print('  |        ( )')
        print('  |       / | \\ ')         
        print('  |')   
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
        print('  |') 
        print('  |') 
        print('  |')
        print('  |_________________')      
    elif status==5:
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
                 

words=["apple","mango"]
random_word=choice(words)

word_list=[]
for i in random_word:
    word_list.append(i)
 

hide=[]
for i in range(len(random_word)):
    hide.append('___')

print("########################")
print("######HANGMAN GAME######")
print("########################\n")

print("INSTRUCTIONS")
print("-------------")
print("1.you can use either upper or lower case letters(A and a are same)\n")
print("2.you have to type the letter in a word as many times as it is repeated in that word\neg:-word:APPLE ,you have to enter P two times\n")
print("3.after three wrong choice ,we will provide a hint for you\n")
print("4.you can make wrong choice only 5 times.after that game will terminated\n")
print("5.guess the word before your man gets hung!\n")
print("Are you ready to play?\n")
name=input("Enter your name:")
input("just press the enter to start  :")
cls()
error=[]
while len(error)<=5:
    hang(len(error))
    print("\n")
    print(f'correct word:{" ".join(hide)}\n')
    print(f'wrong inputs:{",".join(error)}\n')
    a=input("input the letter:")
    a=a.lower()
    if a in word_list:
        hide[word_list.index(a)]=a
        word_list[word_list.index(a)]=" "
    else:
        error.append(a)
        print(f'it was a wrong choice')
    if random_word == ''.join(hide):
        cls()
        print("congratulations "+name)
        print('You won!')
        break
    cls()
else:
    hang(len(error))
    print(f'you lose ,try again/n')
    print(f'The word was {random_word}')
        

        

