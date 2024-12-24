marks=int(input("Enter your marks="))
if marks>50:
    if marks>90:
        print("Excellent.")
    elif marks>51 and marks<90:
        print("Good.")
else:
    print('Fail.')