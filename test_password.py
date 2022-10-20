import strong_password

def main():
    password = input("Input your password: ")
    result = strong_password.check_password(password)

    msg = f"Your password is {result}" if isinstance(result, str) \
        else "User data invalid"
    print(msg)

if __name__ == "__main__":
    main()
