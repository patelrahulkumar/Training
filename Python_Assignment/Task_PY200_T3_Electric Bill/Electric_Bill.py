# Electricity Bill Calculator

# Step 1: Take units from user
units = int(input("Enter electricity units: "))

bill = 0

# Step 2: Apply slab logic
if units <= 100:
    bill = units * 2

elif units <= 200:
    bill = (100 * 2) + (units - 100) * 3

elif units <= 500:
    bill = (100 * 2) + (100 * 3) + (units - 200) * 5

else:
    bill = (100 * 2) + (100 * 3) + (300 * 5) + (units - 500) * 8

# Step 3: Add fixed charge if units > 0
if units > 0:
    bill += 50

# Step 4: Print total bill
print("Total Electricity Bill = INR", bill)