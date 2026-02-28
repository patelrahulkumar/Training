# TaskPY200_T2: Check if number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print("Your entered number {} was positive.".format(num))

elif num < 0:
    print("Your entered number {} was negative, however positive value of your number is {}."
          .format(num, abs(num)))

else:
    print("Your entered number {} was zero.".format(num))