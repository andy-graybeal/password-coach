import getpass
from random import choice

def is_long_enough(password):
    return len(password) >= 15


def has_too_many_repeats(password):
    # Example rule: three or more identical characters in a row
    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True
    return False


def is_common_password(password, filename="fifty_common_passwords.txt"):
    with open(filename, encoding="utf-8") as file:
        return any(password == line.strip() for line in file)



def check_password():
    password = getpass.getpass("Enter a password to check: ")

    long_enough = is_long_enough(password)
    too_many_repeats = has_too_many_repeats(password)
    common_password = is_common_password(password)

    if long_enough and not too_many_repeats and not common_password:
        print("This password passes all three checks.")
    else:
        if not long_enough:
            print("\nProblem: The password has fewer than 15 characters.")

        if too_many_repeats:
            print("\nProblem: The password has three identical characters in a row.")

        if common_password:
            print("\nProblem: The password is on the common-password list.")



def main():
    while True:
        print("\nPassword Coach")
        print("1. Check a password")
        # print("2. Read the FAQ")
        # print("3. Get a recommended passphrase")
        print("4. Quit")

        choice = input("Choose 1–4: ")

        if choice == "1":
            check_password()
       # elif choice == "2":
       #     show_faq()
       # elif choice == "3":
       #     generate_passphrase()
        elif choice == "4" or choice == "q":
            print("Goodbye!")
            break
        else:
            print("Please enter 1, 3, or 4.")


main()