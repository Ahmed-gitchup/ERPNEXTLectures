import random

def hugman():
      words = ["apple", "banana", "orange", "pear", "grape", "mango"]  # List of words to choose from
      ChoiceWord =random.choice(words)
      Gussess= []
      TryCounnt = 6

      while True:
            
            word_Display= ""
            for letter in ChoiceWord:
                  if letter in Gussess:
                        word_Display += letter
                  else: 
                        word_Display += "_"
                        
            print("Word: ", word_Display)

            if word_Display == ChoiceWord:
                  print("Congratulations! You guessed the word correctly.")
                  break

            guess =input("Enter Your LetterGuess : ").lower()

            if guess in Gussess:
                  print("You've already guessed that letter. Try again.")
                  continue

            Gussess.append(guess)

            if guess in ChoiceWord:
                  print("Correct Guess ... Try Again\n")

            else: 
                  TryCounnt-=1
                  print(" Wrong Guess !!!!!!")
                  if TryCounnt == 0:
                        print("Game over! You ran out of attempts.")
                        print("The word was:", ChoiceWord)
                        break
            print("TryCounnt remaining:", TryCounnt)
            print()

hugman()