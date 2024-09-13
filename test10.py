# Word Guessing Game! 

words = [
    "apple", "banana", "grapefruit", "kiwi", "mango", 
    "orange", "pear", "blueberry", "strawberry", "pineapple", 
    "watermelon", "avocado", "dragonfruit", "peach", "coconut"
]

number = int(input("Enter a number!")) 
selection = words[number] 
guess = input("What word am I thinking?") 
guesses = 10 
guessattempts = guesses

def game():    
    # Global Variables 
    global guessattempts
    global guesses
    global guess 
    global selection
    global number
    global again 
    global hint
    global hinter
    
    # Main game
    while guess != selection and guessattempts > 0: 
        print("That is not the word I am thinking")
        guessattempts -= 1
        print("You have " + str(guessattempts) + " attempts left") 
        hint = input("Would you like a hint!").lower()
        if hint != 'n' and hint != 'y': 
            hint = input("Please enter a valid key word!").lower() 
    if hint == 'y': 
        hinter = selection[0] 
        print(f"The word I am thinking starts with a '{hinter}' in it!") 
        guess = input("What word am I thinking?") 
    else: 
        guess = input("Enter a word!") 
    if guessattempts == 0: 
        print("You ran out of turns") 
        print("The word I was thinking was: " + selection) 
        again = input("Would you like to play again!") 
    if guess == selection: 
        print("You got it! the word is " + selection) 
        again = input("Would you like to play again!").lower() 
    

game() 