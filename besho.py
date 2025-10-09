import random  


print(" welcome to the coin guessing game \n Choose a method to toss the coin ")
print(" 1. using random.random() \n 2. using random.randint()")
your_choice = int(input("Enter your choice (1 or 2) ? \n "))

if your_choice == 1 : 

    if random.random () >= 0.5 : 
        computer_result = "Heads"
    else:
        computer_result = "Tails"
        

elif your_choice == 2 : 
    if random.randint (0,1) == 0 :
        computer_result = "Heads" 
    else:
        computer_result = "Tails"

else: 
    print(" invalid choice , please select 1 or 2")


your_toss = input(" Enter your guess (Heads or Tails) \n ")

if your_toss.lower() == computer_result.lower() : 
    print(" you win !! ") 

else: 
    print ("you lost !! ")
    print(f"the computer's guess {computer_result}")

