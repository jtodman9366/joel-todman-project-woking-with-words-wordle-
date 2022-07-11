import colorama 
# We'll learn about how this line of code works later in the course - for now just know it loads the colored text
from colorama import Fore, Back, Style

# Function that prints out a letter with a colorful background
def printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False):

  # If it's not in the word, display it with a red background
  if(not isLetterInWord):
    print(Back.RED + Fore.WHITE + f" {letter} ", end="")

  # If it's in the word...
  else:

    # ...and it's also in the right place, display it with a green background
    if(isLetterInCorrectPlace):
      print(Back.LIGHTGREEN_EX + Fore.WHITE + f" {letter} ", end="")  

    # ...but in the wrong place, display it with a yellow background
    else:
      print(Back.LIGHTYELLOW_EX + Fore.BLACK + f" {letter} ", end="")




# Display a guess, where each letter is color-coded by it's accuracy
def printGuessAccuracy(guess, actual):
  
  # Loop through each index/position 
  for index in range(6):
   
    # Grab the letter from the guess
    letter = guess[index]
    print(letter)
    
  

    # Check if the letter at this index of the user's guess is in the secret word AT ALL or not
  if letter == guess[index]:
    print(Back.LIGHTYELLOW_EX + Fore.WHITE + f" {letter} ", end="")  

  else:
    print(Back.RED + Fore.WHITE + f" {letter} ", end="") 
         
      

      # If the letter is in the secret word, is it also AT THE CURRENT INDEX in the secret word?
    if(letter == secret[position]):

        # Then print it out with a green background
      printColorfulLetter(letter, True, True)

      # If it's not at the current index, we know by this point in the code that it's still used in the secret word somewhere...
   
    elif f(letter != secret[position]):
      print(Back.LIGHTYELLOW_EX + Fore.WHITE + f" {letter} ", end="") 
        # ...so we'll print it out with a yellow background

    # ...but if the letter is not in the word at all...
    else:
      # ...print it out with a red background
      print(Back.RED + Fore.WHITE + f" {letter} ", end="")
    # Don't worry about the line of code below, it works. It just handles the transition between colors
  print(Style.RESET_ALL + " ", end="")

# TO-DO: Write a Function that takes in a six-lettered word from the user
actual = "codes"
letter = ""
index = 0
numOfGuess = 0
guess = ""  

for index in range(0,6):
#while numOfGuess != 6:
#Test
  guess =input("enter sixc-letter word: ").lower()
  print(actual)
  print(actual)
  if guess[index] == letter[:
    printColorfulLetter(guess[index], True, True) 
    #print(end="")
    
    #printGuessAccuracy(guess, actual)
  if guess[index] == letter:
    printColorfulLetter(guess[index], True, False) 
else:
    printColorfulLetter(guess[index], False, False)
    
main()
printColorfulLetter(letter, isLetterInWord, isLetterInCorrectPlace = False)
printGuessAccuracy(guess, actual)

#if actual != guess:
 # print(f"you guess[index] guess the correct word: {guess}")

#if 'letter' in guess:
 # print(guess)
    #print(guess[0])
#numOfGuess +=1
#printColorfulLetter("t", True, False)
#printColorfulLetter(guess[index+1], False, False)
#printColorfulLetter("t", True, True)
#printColorfulLetter("t", False, True)
#printColorfulLetter("t", False, True)