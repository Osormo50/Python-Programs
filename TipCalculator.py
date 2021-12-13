print("Welcome to the Tip Calculator")
subtotal = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total = round((subtotal/people) * (1+tip/100),2)
print(f"Each Person Should Pay ${total}")

