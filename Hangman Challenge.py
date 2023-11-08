#creating a hangman game 

def showDashes(word):
    index_word = word - 1
    len_word = len(words[index_word])
    for i in range(len_word):
        print("-", end = " ")
       
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
       if word_split[j] in word:
          dashes[j] = word_split[j]
       
    if dashes == word_split:
        print("Winner Winner chicken dinner !")          
    
    
    print(word_split , dashes , good_letters , index_element)  
    
#End of the function                   
        
def startGame(word_game):
    lives = 6
    points = 0
    print(word_game)
    while lives >  0:
        letter = input("Input a letter: ")
        if letter not in word_game.lower():
            lives = lives - 1
            print(wrong_letters(letter))
            print(f"You have: {lives} lives")
        elif letter in word_game.lower():
            points +=1 
            replace_dashes(letter , word_game)
    
    if lives == 0:
        lostGame(points)
       
    


words = ["Shoes" , "Shirt" , "Flat" , "Coding" , "Python" , "Sleep" , "Token" , "Knocked" , "Loose"]
picked_word = int(input(f"Pick a number from 1 to {len(words) }: "))
bad_letters = []
good_letters = []
index_element = []
showDashes(picked_word)
