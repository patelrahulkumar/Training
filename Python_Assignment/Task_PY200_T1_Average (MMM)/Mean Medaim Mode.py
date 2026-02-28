# Task PY200_T1: Mean, Median, Mode (First Principles)
# Constraints: No user-defined functions (def), no inbuilt statistics functions

# Input format example:
# Enter number of elements: 5
# Enter elements: 1 2 2 3 4

n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")
for i in range(n):
    val = int(input())
    arr.append(val)

# -------------------------
# MEAN (Average)
# -------------------------
total = 0
for i in range(n):
    total += arr[i]
mean = total / n

# -------------------------
# MEDIAN
# We need sorted array. We'll sort manually using Bubble Sort (first principle)
# -------------------------
sorted_arr = []
for i in range(n):
    sorted_arr.append(arr[i])

# Bubble sort
for i in range(n - 1):
    for j in range(n - 1 - i):
        if sorted_arr[j] > sorted_arr[j + 1]:
            temp = sorted_arr[j]
            sorted_arr[j] = sorted_arr[j + 1]
            sorted_arr[j + 1] = temp

# Median calculation
if n % 2 == 1:
    median = sorted_arr[n // 2]
else:
    mid1 = sorted_arr[(n // 2) - 1]
    mid2 = sorted_arr[n // 2]
    median = (mid1 + mid2) / 2

# -------------------------
# MODE
# Find value with highest frequency (manual counting)
# If multiple have same frequency, this code returns the smallest one (after sorting helps)
# -------------------------
mode = sorted_arr[0]
max_count = 1

i = 0
while i < n:
    current = sorted_arr[i]
    count = 0

    while i < n and sorted_arr[i] == current:
        count += 1
        i += 1

    if count > max_count:
        max_count = count
        mode = current

# Output
print("\nSorted Data:", sorted_arr)
print("Mean =", mean)
print("Median =", median)
print("Mode =", mode, "(frequency =", max_count, ")")