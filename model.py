class SpellingBee:
    def __init__(self, word_list, letter_list, keyletter):
        # initializes a spelling bee object with it's attributes

        self.word_list = word_list
        self.letter_list = letter_list
        self.keyletter = keyletter
        self.guessed_words = []

    def check_guess(self, user_guess):
        if user_guess in self.word_list:
            return True
        else:
            return False

    ### 💻 Finish writing the required methods 
    






if __name__ == "__main__":
    # run python model.py to test 

    spelling_bee = SpellingBee(
        word_list = ["hat","cat"],
        letter_list = ["h","a","t","b","c"],
        keyletter= "a"
    ) 

    # testing check_guess()
    print(spelling_bee.check_guess("hat"))
    print(spelling_bee.check_guess("mat"))