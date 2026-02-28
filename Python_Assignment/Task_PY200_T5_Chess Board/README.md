# ♟️ Chessboard with Numbers

This is a simple Python program that prints a chessboard-style pattern using numbers and a special diagonal rule.

---

## 📌 Project Description

The program:

- Takes an integer **N** as input.
- Generates an **N × N grid**.
- Applies special rules to print:
  - `"X"` on the main diagonal
  - `1` on even positions
  - `0` on odd positions

---

## 🧠 Pattern Rules

For each position `(row, col)`:

1. If `row == col` → Print **X** (Main Diagonal)
2. Else if `(row + col) % 2 == 0` → Print **1**
3. Else → Print **0**

---

## 💻 How It Works

- Outer loop → Controls rows
- Inner loop → Controls columns
- Conditional statements determine what to print
- `end=" "` keeps output in the same row
- `print()` moves to next line after each row

---

## ▶️ How to Run

1. Install Python (3.x recommended)
2. Save the file as `chessboard.py`
3. Open terminal or command prompt
4. Run:

```bash
python chessboard.py
```

5. Enter a value for `N`

---

## 📂 Example Output

### Input:
```
Enter N: 4
```

### Output:
```
X 0 1 0
0 X 0 1
1 0 X 0
0 1 0 X
```

---

## 📚 Concepts Used

- Nested loops
- Conditional statements (`if-elif-else`)
- Modulus operator `%`
- Pattern printing
- User input handling

---

## 🎯 Learning Purpose

This project helps beginners understand:

- 2D grid logic
- Pattern generation
- Even/Odd position checking
- Basic matrix-style printing

---

## 📜 License

Free to use for educational purposes.