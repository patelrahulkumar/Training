password = input("Enter password: ")

# Length Check
if len(password) < 8 or len(password) > 16:
    print("Password must be between 8 and 16 characters")

else:
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    has_space = False

    for ch in password:
        if ch == " ":
            has_space = True
        elif ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif not ch.isalnum():
            has_special = True

    if has_space:
        print("Password should not contain spaces")

    elif has_digit and has_upper and has_lower and has_special:
        print("STRONG Password ✅")

    elif (
        (has_digit and has_upper and has_lower) or
        (has_digit and has_upper and has_special) or
        (has_digit and has_lower and has_special) or
        (has_upper and has_lower and has_special)
    ):
        print("MEDIUM Password ⚠️")

    else:
        print("WEAK Password ❌")