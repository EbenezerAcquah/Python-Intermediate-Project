import json


FILE_NAME = "passwords.json"


def load_passwords():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_passwords():
    with open(FILE_NAME, "w") as file:
        json.dump(passwords, file, indent=4)


def add_password():
    website = input("Enter website/app name: ")
    username = input("Enter username/email: ")
    password = input("Enter password: ")

    password_details = {
        "website": website,
        "username": username,
        "password": password
    }

    passwords.append(password_details)
    save_passwords()

    print("Password details saved successfully!\n")


def view_passwords():
    if len(passwords) == 0:
        print("No passwords saved.\n")

    else:
        for password in passwords:
            print(f"Website: {password['website']}")
            print(f"Username: {password['username']}")
            print(f"Password: {password['password']}")
            print("-" * 30)


def search_password():
    website = input("Enter website to search: ")

    for password in passwords:
        if password["website"].lower() == website.lower():

            print(f"\nWebsite: {password['website']}")
            print(f"Username: {password['username']}")
            print(f"Password: {password['password']}\n")

            return

    print("Password details not found.\n")


def update_password():
    website = input("Enter website to update: ")

    for password in passwords:

        if password["website"].lower() == website.lower():

            password["username"] = input("Enter new username/email: ")
            password["password"] = input("Enter new password: ")

            save_passwords()

            print("Details updated successfully!\n")

            return

    print("Password details not found.\n")


def delete_password():
    website = input("Enter website to delete: ")

    for password in passwords:

        if password["website"].lower() == website.lower():

            passwords.remove(password)

            save_passwords()

            print("Password details deleted successfully!\n")

            return

    print("Password details not found.\n")


passwords = load_passwords()
