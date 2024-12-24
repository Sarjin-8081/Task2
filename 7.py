greet=input("WELCOME TO THE FOREST ADVENTURE\nchoose a path:- left or right\nyour choice=")
if greet=="left":
    pick1=input("Do you want to explore or rest?\nyour choice=")
    if pick1=="explore":
        print("You found treasure!")
    else:
        print("You were attacked by wild animals.Game over.")
else:
    print("You are lost.")