#3. Take an employee's monthly salary as input. If it's more than 50,000, classify as  "High Earner". If less than or equal to 50,000, check if it's more than 20,000 to  classify as "Mid Earner", else classify as "Low Earner".

sal=int(input("Enter your monthly salary="))
if sal>50000:
    print("You are classified as High Earner.")
elif sal<=50000:
    print("You are classified as Mid Earner.")
elif sal>20000:
    print("You are classified as Low Earner.")
else:
    print("Invalid salary")