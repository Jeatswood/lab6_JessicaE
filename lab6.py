
# encode password "00009962” will become “33332295” after encoding
def encode(password):
    encoded_password = ""
    for digit in password:
        # math for each digit to encode
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def main():
    while True:
        # print menu
        print("\nMenu:")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        # input an option
        choice = input("\nPlease enter an option:")
        # prints encoded password
        if choice == "1":
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Error: Password must be exactly 8 digits and contain only numeric characters.")
                continue
            encoded = encode(password)
            print("Encoded password:", encoded)
        # prints encoded password and decoded password
        elif choice == "2":
            decoded = decode(encoded_password)
            print(f"The encoded password is", encoded, "and the original password is:", decoded)
        # exits the program
        elif choice == "3":
            break
        else:
            print("Error: Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
