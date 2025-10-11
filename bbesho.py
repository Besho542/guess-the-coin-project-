book_own = []


yourowm1_book = input("Enter the name of a book you own : \n ")
book_own.append(yourowm1_book)
yourown2_book = input("Enter the name of anther book you own  : (or press enter to skip) \n ")
book_own.append(yourown2_book)

if yourown2_book :
    print(f" \n  your liberey is : \n {book_own} \n ")
else:
    print(f"your liberey is \n {yourowm1_book}")



book_wish = []

yourwish1_book = input("Enter the name of book you wish to have in the future : \n ")
book_wish.append(yourwish1_book)
yourwish2_book = input("Enter the name of another book you wish to have in the future : (or press Enter to skip ) \n ")
book_wish.append(yourwish2_book)

if yourwish2_book : 
    print(f" \n Your wishlist is : \n {book_wish} \n ")
else:
    print(f"your wishlist is {yourwish1_book}")



haved_book = input("Enter the name of book from your wishlist that you'v acquired : (or press Enter to skip) \n")
if haved_book in book_wish :
    book_wish.remove(haved_book)
    book_own.append(haved_book) 
    print(f"\n Updated liberey : {book_own}\n Updated wishlist : {book_wish} \n ")
else:
    print (f"Finally, liberey after updated is {book_own}. ")



Last_book = input("Enter the name of book from liberey you wish to donate: (or press Enter to skip) \n ")
if Last_book in book_own : 
    book_own.remove(Last_book)
    print(f"Finally, liberey after Donation is {book_own}")
else:
    print(f"\n Finalyy,\n  the liberey book is {book_own}\n  the wishlist is {book_wish}")
