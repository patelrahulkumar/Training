# Chessboard with Numbers

# Step 1: Take input
N = int(input("Enter N: "))

# Step 2: Loop through rows
for row in range(N):

    # Step 3: Loop through columns
    for col in range(N):

        # Rule 1: Diagonal
        if row == col:
            print("X", end=" ")

        # Rule 2: Even position
        elif (row + col) % 2 == 0:
            print(1, end=" ")

        # Rule 3: Odd position
        else:
            print(0, end=" ")

    # New line after each row
    print()