
---

# PY200_T1 – Mean, Median, Mode (First Principles)

## 📌 Project Description

This program calculates the **Mean**, **Median**, and **Mode** of a given set of numbers using **first principles** in Python.

### 🔒 Constraints

* ❌ No user-defined functions (`def`)
* ❌ No inbuilt statistics functions (`statistics.mean()`, etc.)
* ✅ Manual implementation of logic
* ✅ Manual sorting using **Bubble Sort**

---

## 📥 Input Format

```
Enter number of elements: 5
Enter elements:
1
2
2
3
4
```

* First input: Number of elements (`n`)
* Next `n` inputs: Integer elements (one per line)

---

## 🧮 How It Works

### 1️⃣ Mean (Average)

* Sum all elements manually using a loop
* Divide total by number of elements

Formula:

```
Mean = (Sum of all elements) / n
```

---

### 2️⃣ Median

* Copy array into a new list
* Sort manually using **Bubble Sort**
* If `n` is odd → middle element
* If `n` is even → average of two middle elements

---

### 3️⃣ Mode

* Uses sorted array
* Counts frequency of each element manually using a `while` loop
* Returns element with highest frequency
* If multiple values have same highest frequency → smallest value is returned

---

## 📤 Output Example

```
Sorted Data: [1, 2, 2, 3, 4]
Mean = 2.4
Median = 2
Mode = 2 (frequency = 2)
```

---

## 📚 Concepts Used

* Lists
* For loops
* While loops
* Conditional statements
* Manual sorting (Bubble Sort)
* Frequency counting
* Basic arithmetic operations

---

## 🎯 Learning Objective

This task strengthens understanding of:

* Algorithm design from scratch
* Sorting techniques
* Statistical calculations without built-in libraries
* Loop control and logic building

---

## 🏷 File Name Suggestion

```
PY200_T1_Mean_Median_Mode.py
```

---

If you want, I can also format this README for:

* 🔹 GitHub submission
* 🔹 College lab record
* 🔹 Viva preparation notes
* 🔹 With flowchart explanation
