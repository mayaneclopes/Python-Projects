"""
 Challenge: Simple Bill Splitter

Write a Python script that helps split a bill evenly between friends.

Your program should:
1. Ask how many people are in the group.
2. Ask for each person's name.
3. Ask for the total bill amount.
4. Calculate each person's share of the bill.
5. Display how much each person owes in a clean, readable format.

Example:
Total bill: $1200  
People: Aman, Neha, Ravi

Each person owes: $400

Final output:
  Aman owes $400  
  Neha owes $400  
  Ravi owes $400

Bonus:
- Round to 2 decimal places
- Print a decorative summary box
"""

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid  number")

num_people = int(input("How many people are there? "))
names = []

for i in range(num_people): #loop will keep going accordinly with num_people input
    name = input(f"Enter the mane of person #{i+1}: ").strip().title()
    names.append(name)

total_bill = get_float("Enter bill amount (number only): ")

share = round(total_bill/num_people)

print(f"\n" + "*" * 40)
print(f"Total bill: {total_bill}")
print(f"Each person share: {share}")

for name in names:
    print(f"{name} share is {share} dollars")