print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

# print(type(bill))
# print(type(tip))
# print(type(people))

tip_amount = float(bill) * ((int(tip) / 100))

total = (float(bill) / int(people)) + (tip_amount / int(people))
new_total = "{:.2f}".format(total)

print(f"Each person should pay: ${new_total}")
