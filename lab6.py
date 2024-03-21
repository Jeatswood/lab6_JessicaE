def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password


def main():
    while True:
        print("\nMenu:")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Error: Password must be exactly 8 digits and contain only numeric characters.")
                continue
            encoded = encode(password)
            print("Encoded password:", encoded)

        elif choice == "2":
            encoded_password = input("Enter an encoded password: ")
            if len(encoded_password) != 8 or not encoded_password.isdigit():
                print("Error: Encoded password must be exactly 8 digits and contain only numeric characters.")
                continue
            decoded = decode(encoded_password)
            print(f"The encoded password is", encoded, "and the original password is:", decoded)

        elif choice == "3":
            break

        else:
            print("Error: Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
