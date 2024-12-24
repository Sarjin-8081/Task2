greet=input("WELCOME TO THE JNGLE OF SURVIVAL CHALLENGE\ndo you wan to :- search for food OR build a shelter\nyour choice=")
if greet=="search for food":
    pick1=input("Do you want to hunt or gather?\nyour choice=")
    if pick1=="hunt":
        print("You were attacked by wild animals.Game over")
    else:
        print("You found enough food.You win.")
else:
    print("You Died.")