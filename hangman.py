# set variable that has list of alphabet (capital, lower)
    # set to lower
# set variable that has list of "body parts"
# user selects word 
# have output that shows numbers of characters in word represented with underscores
# have output that shows an empty noose
# user inputs letter
# input is compared against letters in selected word for matching
    # if match fill in empty space(s) with letter
    # otherwise draw body part under noose

def hang_man():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    words = ["home", "school", "work", "casino"]
    allowed_guesses = 6
    guessed_letters = []

    print("Welcome to hangman!")
    print(f"You are allowed {allowed_guesses} chances to guess the word.")
    user_select = input(f"Select a word from the following {', '.join(words)}: ")
    if user_select in words:
        print(f"You selected {user_select}")
    else:
        print("Please pick a word from the word list")
    while allowed_guesses > 0:
        guess = input("Please guess a letter: ")
        if len(guess) > 1:
            print("Please select one letter")
        else: 
            pass
        if guess in list(user_select):
            print("Correct!")
        else:
            allowed_guesses -= 1                                        # decrease number of guesses left
            print("Incorrect")
    
    else: 
        print(f"Game over! The word was: {user_select}")

if __name__ == "__main__":
    hang_man()



    # user_word = list(user_select)
    # guess = input("Guess a letter: ")
    #if len(guess) > 1:
    #    print("Please guess one letter")
    #else:
    #    print() 
        #pass
    #if guess in user_word:
    #    print("Correct")
    #else:
    #    print("Incorrect")

    

    # word = input("Please enter a word: ")       # ask user to enter a word
    # word_list = list(word)                      # split selected word into string
    # if word_list in alphabet:
    #    word_string = ''.join(word_list)
    #    print(word_string)
    #else:
    #    print("Error")


# def match():
    # alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    # body_parts = ["O", "|", "/", "\\", "-"]



# def no_match():



# def main():



# if __name__ == "__main__":
    # main()