import os
def clear():
    os.system("cls")

def guessSystem(answer, strike_limit):
    # Variables
    letter_guess = ""
    strikes = 0
    out_of_strikes = False

    guessed_letters = ""
    unguessed_letters = answer

    answer_blank = ""

    game_won = False

    for letter in answer:
        answer_blank = answer_blank + "-"

    # print("\033[H\033[J")
    clear()

    # guessing system
    while not(out_of_strikes) and not(game_won):

        print("\n\t(" + answer_blank + ")\n")
        print("Incorrect guesses remaining: " + str(strike_limit - strikes))
        
        letter_guess = (input("Enter your guess: ")).lower()

        if letter_guess == "0":
            return 0

        if letter_guess in unguessed_letters: # if letter is in answer

            # sort accordingly to what letters have been guessed and what haven't
            guessed_letters += letter_guess
            unguessed_letters = unguessed_letters.replace(letter_guess, "")

            answer_blank = answer
            for letter in unguessed_letters:
                answer_blank = answer_blank.replace(unguessed_letters[int(unguessed_letters.index(letter))], "-")
        else: # if letter is not in answer, add strike
            strikes += 1
                    
        # print("Guessed letters: " + guessed_letters)
        # print("Not guessed letters: " + unguessed_letters)
        
        if unguessed_letters == "":
            game_won = True
        
        if strikes >= strike_limit:
            out_of_strikes = True
        
        if not(game_won) and not(out_of_strikes):
            # print("\033[H\033[J")
            clear()

    if game_won:
        return 1
    else:
        return 2

    
print("\n- - - - - H A N G M A N - - - - -")
answer = (input("Host, choose your word: ")).lower()

try:
    strikes = int(input("How many incorrect guesses should be allowed?: "))
except ValueError:
    print("* Must enter integer number *")
    print("\n    - - - - - - - -")
    print("    - E X I T E D -")
    print("    - - - - - - - -\n")
    exit()

game_result = guessSystem(answer, strikes)

if game_result == 1:
    print("\n    - - - - - - - - - - - - -")
    print("    - You Guessed The Word! -")
    print("    - - - - - - - - - - - - -\n")

elif game_result == 2:
    print("\n    - - - - - - - - -")
    print("    - You Have Lost -")
    print("    - - - - - - - - -\n")
else:
    print("\n    - - - - - - - -")
    print("    - E X I T E D -")
    print("    - - - - - - - -\n")