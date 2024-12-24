#2. Ask the user if they want vegetarian or non-vegetarian. Based on the choice, give  them options. If vegetarian, ask if they want "Salad" or "Pasta". If non-vegetarian, ask  if they want "Chicken" or "Fish". 

choice=input("Do you want vegetarian or non-vegetarian\nyour choice=?")
if choice=="vegetarian":
    veg=input("Do you want Salad or Pasta?\nyour choice=")
elif choice=="non-vegetarian":
    non_veg=input("Do you want Chicken or Fish?\nyour choice=")
