greet=input("Welcome to the Haunted Castle\ndo you wan to :-enter the castle or run away\nyour choice=")
if greet=="enter the castle":
    pick1=input(" choose a door: red, green, or black\nyour choice=")
    if pick1=="red":
        print("You entered a room full of flames. Game Over.")
    elif pick1=="green":
        print("You found the treasure. You Win!")
    else:
        print("You were captured by ghosts. Game Over.")
else:
    print("You escaped safely.")