# TaskPY200_T6: Find the Smallest Number With Digit Constraints

N = int(input("Enter N: "))

answer = -1  # default: if we don't find any valid number

for x in range(1, N + 1):
    s = str(x)  # number ko string bana diya for easy digit checks

    # Condition 1: x must NOT contain digit 0
    if '0' in s:
        continue

    # Condition 2: x must contain exactly two 3s
    if s.count('3') != 2:
        continue

    # Condition 3: sum of digits must be divisible by 7
    digit_sum = 0
    for ch in s:
        digit_sum += int(ch)

    if digit_sum % 7 != 0:
        continue

    # agar sab conditions pass ho gayi
    answer = x
    break  # smallest mil gaya, so stop

print(answer)