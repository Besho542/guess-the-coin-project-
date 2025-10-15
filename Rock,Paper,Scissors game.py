import random
paper = "📜📜📜📜\n📜📜📜📜\n📜📜📜📜\n📜📜📜📜\n📜📜📜📜"
Rock = "🧱🧱🧱🧱\n🧱🧱🧱🧱\n🧱🧱🧱🧱\n🧱🧱🧱🧱\n🧱🧱🧱🧱"
scissor = "✂️✂️✂️✂️\n✂️✂️✂️✂️\n✂️✂️✂️✂️\n✂️✂️✂️✂️\n✂️✂️✂️✂️"
total = [paper, Rock, scissor]

ai_choice = random.choice(total)

print ("Welcome to the Rock, Paper, Scissors game: ")
Help = input("press Enter to continue or type (Help) for the rules ..")



if Help.lower() == "help" :
    print(""" \n
            ********* RULES *********
        1) You choose and the computer chooses
        2) Rock smashes cut paper -> Rock wins
        3) Scissors cut Paper -> Scissors wins
        4) Paper covers Rocks -> Paper wins
                                                \n """)
    
    your_choice = input("Enter your choice (rock, paper, scissor):..  ").lower()
    if your_choice == "paper" and ai_choice == paper :
        print (f"\n your choice:\n{paper}\n\n computer choice:\n{paper}")
        print("this is tail")
    elif your_choice == "paper" and ai_choice == Rock :
        print(f"\n your choice:\n{paper}\n\n computer choice:\n{Rock}")
        print("You win...")
    elif your_choice == "paper" and ai_choice == scissor :
        print(f"\n your choice:\n{paper}\n\n computer choice:\n{scissor}")
        print("You lost...")
    elif your_choice == "rock" and ai_choice == Rock :
        print(f"\n your choice:\n{Rock}\n\n computer choice:\n{Rock}")
        print("this is tail")
    elif your_choice == "rock" and ai_choice == paper : 
        print(f"\n your choice:\n{Rock}\n\n computer choice:\n{paper}")
        print("You lost...")
    elif your_choice == "rock" and ai_choice == scissor :
        print(f"\n your choice:\n{Rock}\n\n computer choice:\n{scissor}")
        print("You win...")
    elif your_choice == "scissor" and ai_choice == scissor : 
        print(f"\n your choice:\n{scissor}\n\n computer choice:\n{scissor}")
        print("this is tail")
    elif your_choice == "scissor" and ai_choice == paper : 
        print(f"\n your choice:\n{scissor}\n\n computer choice:\n{paper}")
        print("You win...")
    elif your_choice == "scissor" and ai_choice == Rock :
        print(f"\n your choice:\n{scissor}\n\n computer choice:\n{Rock}")
        print("You lost...")
    else: 
        print("invalied choice. please run the program again and choose Rock, paper, or scissors")


else :     
    your_choice = input("Enter your choice (rock, paper, scissors):..  ").lower()
    if your_choice == "paper" and ai_choice == paper :
        print (f"\n your choice:\n{paper}\n\n computer choice:\n{paper}")
        print("this is tail")
    elif your_choice == "paper" and ai_choice == Rock :
        print(f"\n your choice:\n{paper}\n\n computer choice:\n{Rock}")
        print("You win...")
    elif your_choice == "paper" and ai_choice == scissor :
        print(f"\n your choice:\n{paper}\n\n computer choice:\n{scissor}")
        print("You lost...")
    elif your_choice == "rock" and ai_choice == Rock :
        print(f"\n your choice:\n{Rock}\n\n computer choice:\n{Rock}")
        print("this is tail")
    elif your_choice == "rock" and ai_choice == paper : 
        print(f"\n your choice:\n{Rock}\n\n computer choice:\n{paper}")
        print("You lost...")
    elif your_choice == "rock" and ai_choice == scissor :
        print(f"\n your choice:\n{Rock}\n\n computer choice:\n{scissor}")
        print("You win...")
    elif your_choice == "scissor" and ai_choice == scissor : 
        print(f"\n your choice:\n{scissor}\n\n computer choice:\n{scissor}")
        print("this is tail")
    elif your_choice == "scissor" and ai_choice == paper : 
        print(f"\n your choice:\n{scissor}\n\n computer choice:\n{paper}")
        print("You win...")
    elif your_choice == "scissor" and ai_choice == Rock :
        print(f"\n your choice:\n{scissor}\n\n computer choice:\n{Rock}")
        print("You lost...")
    else: 
        print("invalied choice. please run the program again and choose Rock, paper, or scissors")
