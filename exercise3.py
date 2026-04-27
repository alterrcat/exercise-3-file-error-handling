try:
    username = input("Enter username: ")
    if not username.strip():
        raise ValueError("Username cannot be empty.")

    age = int(input("Enter age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("User saved successfully.")

except ValueError as e:
    print(f"Invalid input: {e}")

try:
    print("\nSaved Users:")
    with open("users.txt", "r") as file:
        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("No users found.")

print("\nSystem complete.")