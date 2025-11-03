import random
words = ["bad", "good", "ugly"]
ai_word = random.choice(words)
position = ["_"] * len(ai_word)
print(" ".join(position))
lives = 6
Hangman_stages = ("""
 +_____+
 |     |
 |     
 |    
 |
_|_

""", """

  _____
 |     |
 |     O
 |    
 |   
_|_

""", """
  _____
 |     |
 |     O
 |     |
 |  
_|_
""" , """
  _____
 |     |
 |     O
 |    /|
 |    
_|_
""", """
  _____
 |     |
 |     O
 |    /|/
 |    
_|_
""", """
  _____
 |     |
 |     O
 |    /|/
 |    / 
_|_
""", """
  _____
 |     |
 |     O
 |    /|/
 |    / /
_|_
""")

guessed_latter = []
print(Hangman_stages[0])
while "_" in position and lives > 0  :
    guess = input("Plase enter a latter: ")

    if guess in guessed_latter :
        print("you already guessed it, try again")
        print(f"you have {lives} tries . ")
        continue 
    
    guessed_latter.append(guess) 

    if guess not in ai_word :
        lives -= 1
        print(f"You have {lives} tries . ")
        print(Hangman_stages[6-lives])

    else:
        for x in range(len(ai_word)) :
            if ai_word[x] == guess :
               position[x] = guess
               print(" ".join(position))


if lives == 0 :
    print(f"""
**** YOU LOST ****
    {Hangman_stages[-1]}
""")
else:
    print("""
YOU WIN !!!!!
""")

        

