class SpellingBee:
    def __init__(self, word_list, letter_list, keyletter):
        # initializes a spelling bee object with it's attributes

        self.word_list = word_list
        self.letter_list = letter_list
        self.keyletter = keyletter
        self.guessed_words = []

    def check_guess(self, user_guess):
        if user_guess in self.word_list:
            self.guessed_words.append(user_guess)
            return True
        else:
            return False
        
    def check_already_guessed(self,user_guess):
        if user_guess in self.guessed_words:
            return True
        else:
            return False

    ### 💻 Finish writing the required methods, reference the UML diagram
    


if __name__ == "__main__":
    # run python model.py to test 
    
    print("-- testing SpellingBee() -- ")


    spelling_bee = SpellingBee(
        word_list = ["hat","cat"],
        letter_list = ["h","a","t","b","c"],
        keyletter= "a"
    ) 

    print("\n-- testing check_guess() -- ")
    print(spelling_bee.check_guess("cat"))
    print(spelling_bee.check_guess("mat"))

    print("\n-- testing check_already_guessed() -- ")
    print(spelling_bee.check_already_guessed("cat"))

    ### 💻 Finish testing new methods