class TerminalView:

    def welcome(self):
        print("\n--- 🐝 Welcome to Spelling Bee 🐝 ---")

    def rules(self, letters, keyletter):
        print("\n[RULES]")
        print(f"You can use any of these letters: {letters}")
        print(f"You must you use the letter {keyletter}")
        print("Guesses must be more than 3 letters long")

    def get_guess(self):
        print("\n---Enter word:---")
        guess = input(" > ")
        return guess.upper()

    def correct(self):
        print("\n  -correct!-  ")

    def already_guessed(self):
        print("\n  -you've already guessed this word...-  ")
            
    ### 💻 Finish writing the required methods 
