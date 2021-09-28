import os
from random import choice

def cls():
    os.system("cls")

#function to make gibbet
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

# function for hint 
              
def hint(status):
    if(status==3):
        print()
        print("\t\t*********** Hint ***********")
        print("\t\tIt is a name of an animal !!")
        print("\t\t****************************")

 #  function for display the score board
     
def score_board(score):
    print("*---------------------------*")
    print("|--------SCORE BOARD--------|")
    print("|---------------------------|")
    print(f'|\t  SCORE::{score}\t    |')
    print("*---------------------------*")

# empty dictionary 
words = {}  
file=open('animal.txt','r')
for i in file.readlines():
    i=i.replace('\n','')
    number,animal=i.split('.')
    words[number]=animal
file.close
random_word=choice(list(words.values()))

#list to store the actual word
word_list = []
for i in random_word:
    word_list.append(i)
 
#list to store the word hidden
hide = []
for i in range(len(random_word)):
    hide.append('___')
print()
print("########################")
print("##### HANGMAN GAME #####")
print("########################\n")

print("INSTRUCTIONS")
print("-------------")
print("1. You can use either upper or lower case letters(A and a are same).\n")
print("2. You have to type the letter in a word as many times as it is repeated in that word\n   Eg:-\n   Word: APPLE, you have to enter P two times.\n")
print("3. After three wrong choice ,we will provide a hint for you.\n")
print("4. You can make wrong choice only 5 times.after that game will terminated.")
print("5. Guess the word before your man gets hung!\n")
print("Get Ready Folks !!\n")
name=input("Enter your name : ")
input("Just Press The Enter To Start !")
cls()

#list to store the wrong choices
wrong_choices = []
score = 0
while len(wrong_choices)<=5:
    hang(len(wrong_choices))
    hint(len(wrong_choices))
    print("\n")
    score_board(score)
    print(f'correct word:{" ".join(hide)}\n')
    print(f'wrong inputs:{",".join(wrong_choices)}\n')
    letter=input("input the letter:")
    letter=letter.lower()
    if letter in word_list:
        hide[word_list.index(letter)]=letter
        word_list[word_list.index(letter)]=" "
        score +=1
    else:
        wrong_choices.append(letter)
        print(f'it was a wrong choice')
    if random_word == ''.join(hide):
        cls()
        print("congratulations "+name)
        print('You won!')
        score_board(score)
        break
    cls()
else:
    hang(len(wrong_choices))
    print(f'you lose ,try again\n')
    print(f'The word was {random_word}\n')
        

