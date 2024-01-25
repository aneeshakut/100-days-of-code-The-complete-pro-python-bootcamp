#Tip Calculator

print("Welcome to the tip calculator.")
Bill = float(input("What was the total bill?$"))
Tip_ptg = int(input("What percentage tip would you like to give?10,12 or 15"))
Split = int(input("How many people to split the bill?"))

Total = Bill + (Tip_ptg*0.01)*Bill
Per_Person = Total / Split

print("Each person should pay:$",Per_Person)
