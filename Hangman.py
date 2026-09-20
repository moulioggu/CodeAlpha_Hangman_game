import random
import time

words =['apple','banana','grapes','orange','mango']
chances=6
r_word=random.choice(words)
print('Welcome to the Hangman game')
time.sleep(0.5)
print("You Have only 6 chances to guess the word")
time.sleep(0.5)
print("Note:The names are from the fruits")
while chances !=0 :
    a=input('Now,Guess the word: ')
    if a==r_word:
        print("you're guess is correct")
        print("The word is: ",r_word)
        break
    else:
        chances-=1
        print("You're Guess is incorrect and you have ",chances,'chances left')

if chances == 0:
    print("Game Over!")
    print("The word was:", r_word)