print("Welcome to place the rabbit \n ")

loop1 =["🌿", "🌿", "🌿"]
loop2 =["🌿", "🌿", "🌿"]
loop3 =["🌿", "🌿", "🌿"]

print(f"{loop1}\n{loop2}\n{loop3}")
print("\nWhere should the rabbit go ? 🐇")
place =int(input("Please choose a row and a column ? "))

if place == 11 :
    loop1.remove(loop1[0])
    loop1.insert(0,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 12 :
    loop1.remove(loop1[1])
    loop1.insert(1,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 13 :
    loop1.remove(loop1[2])
    loop1.insert(2,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 21 :
    loop2.remove(loop2[0])
    loop2.insert(0,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 22 :
    loop2.remove(loop2[1])
    loop2.insert(1,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 23 :
    loop2.remove(loop2[2])
    loop2.insert(2,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 31 :
    loop3.remove(loop3[0])
    loop3.insert(0,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 32 : 
    loop3.remove(loop3[1])
    loop3.insert(1,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
elif place == 33 :
    loop3.remove(loop3[2])
    loop3.insert(2,"🐇")
    print(f"\n success .... \n\n{loop1}\n{loop2}\n{loop3}")
else:
    print("sorry, this is out of game! 🤷‍♀️🤦‍♀️")
