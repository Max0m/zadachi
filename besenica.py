import random
import time

words = ["bit","byte","internet","ssd","regret","sofa","return","manage","fight","hold","deep","test","trunk","hole","swing","monkey","door","sheep","random","outfit"]
hidden_word = random.choice(words)
wrong = 0



guess = ("-") * len(hidden_word)

print("Welcome! You have 6 guesses to guess the word!")
print("Your guess: ", guess)


while guess != hidden_word and wrong < 6:  
    
    print("Enter letter")
    letter = str(input())
    
    #print(letter)

    if letter == hidden_word:
        guess = letter

    
    elif letter in hidden_word and letter != "":
        
        new = ""
        
        for i in range(len(hidden_word)):
        
            if letter == hidden_word[i]:
                new += letter
            else: 
                new += guess[i]

        guess = new
    
    else:
        wrong += 1
        print("INCORRECT! Guesses left:",6 - wrong)
    print("Your guess: ", guess)
  
print("Hidden word was:", hidden_word)
time.sleep(15)