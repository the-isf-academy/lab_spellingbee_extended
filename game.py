# import modules
from model import SpellingBee
from view import TerminalView
from wordslist import letter_list, keyletter, word_list

# creates an instance of SpellingBee
spelling_bee = SpellingBee(word_list, letter_list, keyletter)

# create an instance of TerminalView
terminal_view = TerminalView()                                       

terminal_view.welcome()

terminal_view.rules(spelling_bee.letter_list, spelling_bee.keyletter)

game_play = True

while game_play == True:

    # user guesses a word
    user_guess = terminal_view.get_guess()

    #check for keyletter
    if spelling_bee.check_guess(user_guess) == True:
        terminal_view.correct()

    ### 💻 Finish the game logic

   
