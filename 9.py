greet=input("Welcome to the Space Adventure\ndo you wan to :-land on Mars or fly to Jupiter\nyour choice=")
if greet=="land on mars":
    pick1=input("Do you want to explore or build a base?\nyour choice=")
    if pick1=="explore":
        print("You found alien artifacts. You Win!")
    else:
        print("You ran out of resources. Game Over.")
else:
    print("Your spaceship crashed. Game Over.")