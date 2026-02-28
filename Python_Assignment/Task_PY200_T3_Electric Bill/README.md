# ⚡ Electricity Bill Calculator

This is a simple Python program that calculates the total electricity bill based on the number of units consumed. The program follows a slab-based billing system and adds a fixed charge.

---

## 📌 Features

- Takes electricity units as input from the user
- Applies slab-wise billing calculation
- Adds a fixed charge of ₹50 (if units > 0)
- Displays the total electricity bill

---

## 🧮 Billing Slabs

| Units Consumed | Rate per Unit |
|---------------|--------------|
| 0 – 100       | ₹2 per unit  |
| 101 – 200     | ₹3 per unit  |
| 201 – 500     | ₹5 per unit  |
| Above 500     | ₹8 per unit  |

✅ Fixed Charge: ₹50 (if units > 0)

---

## 💻 How It Works

1. User enters the number of electricity units.
2. Program checks which slab the units fall into.
3. Calculates the bill according to slab rates.
4. Adds ₹50 fixed charge (if applicable).
5. Prints the final bill amount.

---

## ▶️ How to Run

1. Install Python (version 3.x recommended).
2. Save the file as `electricity_bill.py`.
3. Open terminal or command prompt.
4. Run the program:

```bash
python electricity_bill.py
```

5. Enter the electricity units when prompted.

---

## 📂 Example Output

```
Enter electricity units: 250
Total Electricity Bill = ₹ 1050
```

---

## 🧾 Formula Logic Used

```
0–100 units      → units × 2
101–200 units    → (100 × 2) + (remaining × 3)
201–500 units    → (100 × 2) + (100 × 3) + (remaining × 5)
Above 500 units  → (100 × 2) + (100 × 3) + (300 × 5) + (remaining × 8)
+ ₹50 fixed charge (if units > 0)
```

---

## 👨‍💻 Author

Created as a beginner-friendly Python project to understand:
- Conditional statements (`if-elif-else`)
- Basic arithmetic operations
- User input handling

---

## 📜 License

This project is free to use for educational purposes.