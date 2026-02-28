#  Password Strength Checker (Python)

This Python program checks the strength of a user-entered password based on specific validation rules.

---

##  Features

- ✔ Password length validation (8 to 16 characters)
- ✔ Space detection (spaces not allowed)
- ✔ Checks for:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters
- ✔ Classifies password as:
  - STRONG
  - MEDIUM
  - WEAK

---

##  Password Rules

### 🔹 Length Requirement
Password must be between **8 and 16 characters** (inclusive).

### 🔹 Space Rule
Password **must not contain spaces**.

---

##  Strength Criteria

| Conditions Met | Strength |
|---------------|----------|
| Lower + Upper + Digit + Special | STRONG  |
| Any 3 of the above | MEDIUM  |
| Less than 3 conditions | WEAK  |

---

##  How It Works

1. User enters a password.
2. Program checks length.
3. Program scans each character to detect:
   - `islower()` → lowercase
   - `isupper()` → uppercase
   - `isdigit()` → number
   - `not isalnum()` → special character
4. Based on conditions met, strength is displayed.

---
##  Here to Run:

5. Enter your password when prompted.

---

##  Example Output

### Example 1
```
Enter password: Abc123@1
STRONG Password 
```

### Example 2
```
Enter password: Abc12345
MEDIUM Password 
```

### Example 3
```
Enter password: abc12
Password must be between 8 and 16 characters
```

---

##  Concepts Used

- Conditional Statements (`if-elif-else`)
- Boolean Variables
- Loops (`for`)
- String Methods:
  - `islower()`
  - `isupper()`
  - `isdigit()`
  - `isalnum()`
- Logical Operators (`and`, `or`)

---

##  Learning Objective

This project helps beginners understand:

- Password validation logic
- Input handling
- Character classification
- Logical condition building

---

##  License

Free to use for educational purposes.