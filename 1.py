# 1. Take the price of an item as input. If the price is more than 1000, apply a 10%  discount. Otherwise, check if the price is more than 500 and apply a 5% discount.  Print the final price. 

price=int(input("Enter pice of an item="))
if price>1000:
    discount=price*10/100
    print(f"You got 10% off your discounted amount is {discount}")
    final=price-discount
    print(f"Your final price is {final}")
elif price>500:
    discount=price*5/100
    print(f"You got 5% off your discounted amount is {discount}")
    final=price-discount
    print(f"Your final price is {final}")

