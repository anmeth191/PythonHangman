from random import *

#creating a hangman game 

def showDashes(word):
    index_word = word - 1
    counter = 0 
    len_word = len(words[index_word])
    for i in range(len_word):
        counter += 1
        print("-", end = " ")
    print("\n" + f"Your word has {counter} secret letters !")
    print("You have: 6 lives")
       
    startGame(words[index_word])
    
def wrong_letters(letter):
    bad_letters.append(letter)
    for i in bad_letters:
        return  f"{i}",          
        
def lostGame(points):
    print(f"Game Over, your Score is: {points}")
    print("Your wrong Letters are: ")
    for wrongLetters in bad_letters:
     print(wrongLetters , end=" ")   

#This function is the one who returns the dashes and letter when is a good input
def replace_dashes(letter , word):
    word_split = []
    dashes = []
    cnt = 0
     
    for item in word.lower():
        word_split.append(item)
        dashes.append("-")
    
    #old solution but it did not worked because when a letter is duplicated does not works
    #good_letters.append(letter)    
    #for j in good_letters:
     #   test = word_split.index(j)
      #  dashes[test] = j
    #dashes[test].append(letter)
        
    for i in word.lower():
        if i == letter:
            index_element.append(cnt)
        cnt = cnt+1
        
    for j in index_element:
       if word_split[j] in word.lower():
          dashes[j] = word_split[j]
     
    for l in dashes:
        print(l , end=" ") 
         
    if dashes == word_split:
        return True    
#End of the function

def won_game(points):
    print("\n" + "You have Won ! Congratulations !!!!!")
    print(f"Your Score is: {points} points")                   
        
def startGame(word_game):
    lives = 6
    points = 0
    won = False
   
    while lives >  0 and won == False:
        letter = input("\n" + "Input a letter: ")
        if letter not in word_game.lower():
            lives = lives - 1
            print("Wrong Letter")
            print(f"You have: {lives} lives")
        elif letter in word_game.lower():
            points +=1 
            state_game = replace_dashes(letter , word_game)
            if state_game == True:
                won = True
                won_game(points)    
    if lives == 0:
        lostGame(points)
       
#verifies that the entry is a number in the specified range
def verify_correct_number(number):
    if number > len(words) or number <= 0:
        another_try = input(f"Pick a number from 1 to {len(words) }: ")
        while int(another_try) > len(words) or int(another_try) <= 0:
            another_try = input(f"Pick a number from 1 to {len(words) }: ")
        if int(another_try) > 0 and int(another_try) <= len(words):
            showDashes(int(another_try)) 
    elif number > 0 and number <= len(words):
        showDashes(number)        

#verifies that the entry is not a letter or a different char
def verify_not_letter(word):
    if not word.isdigit():
     print("You must Enter a Valid Number")
     another_try = input(f"Pick a number from 1 to {len(words) }: ")
     while not another_try.isdigit():
        another_try = input(f"Pick a number from 1 to {len(words) }: ")
     verify_correct_number(int(another_try))
    else:
        verify_correct_number(int(word))
    
    

bad_letters = []
good_letters = []
index_element =[]
words = ["Shoes" , "Shirt" , "Flat" , "Coding" , "Python" , "Sleep" , "Token" , "Knocked" , "Loose" , "Music" , "Computer" , "Monitor" , "Printer" , "Water" , "Fire" , "Cold" , "Electricity"]
shuffle(words)
picked_word = input(f"Pick a number from 1 to {len(words) }: ")  
 
#send the picked item to be verified and display an error if there is a wrong input
verify_not_letter(picked_word)
