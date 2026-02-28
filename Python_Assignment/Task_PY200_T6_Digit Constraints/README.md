
---

#  TaskPY200_T6: Find the Smallest Number With Digit Constraints

This is a simple Python program that finds the smallest number within a given range that satisfies specific digit-based conditions.

---

##  Project Description

The program:

* Takes an integer **N** as input.
* Checks numbers from **1 to N**.
* Finds the **smallest number** that:

  * Does NOT contain digit `0`
  * Contains exactly **two `3`s**
  * Has a digit sum divisible by **7**
* Prints `-1` if no such number exists.

---

##  Conditions Applied

For each number `x` in range `1..N`:

1. If `'0'` is present → Skip the number
2. If number does NOT contain exactly two `3`s → Skip
3. If sum of digits is NOT divisible by 7 → Skip
4. If all conditions pass → Print the number and stop

---

##  How It Works

* Loop runs from `1` to `N`
* Each number is converted into a string for easy digit checking
* `.count()` is used to count occurrences of `3`
* A loop calculates digit sum
* `continue` skips invalid numbers
* `break` stops when the smallest valid number is found

---

## ▶ Here to Run

5. Enter a value for `N`

---

##  Example Output

### Input:

```
Enter N: 500
```

### Output:

```
133
```

### Explanation:

* No digit `0` ✔
* Exactly two `3`s ✔
* Digit sum = 1 + 3 + 3 = 7 ✔ (Divisible by 7)

---

##  Concepts Used

* String conversion of integers
* Looping (`for` loop)
* Conditional statements (`if`, `continue`, `break`)
* Counting characters using `.count()`
* Digit sum calculation
* Modulus operator `%`

---

## ⏱ Time Complexity

* **O(N × d)**
  Where `d` is the number of digits in each number.

Works efficiently for small to moderate values of `N`.

---

##  Learning Purpose

This project helps beginners understand:

* Number filtering using multiple conditions
* Digit manipulation using strings
* Efficient loop control
* Basic mathematical property checking

---

##  License

Free to use for educational purposes.
