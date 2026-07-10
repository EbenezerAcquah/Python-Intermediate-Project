#List to store all contacts
contacts = []

#Function to add a new contact 
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")

#Store the contact information in a dictionary
    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

#Add he dictionary to the contacts list
    contacts.append(contact)
    print("Contact added successfully.\n")

# Function to display all saved contacts
def view_contacts():
    if len(contacts) == 0:
        print("No contacts available.\n")

 # Loop through each contact and display its details       
    else:
        for contact in contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print("-" * 25)


# Function to search for a contact by name
def search_contact():
    name = input("Enter name to search: ")

    for contact in contacts:
# Compare names without considering uppercase/lowercase
        if contact["name"].lower() == name.lower():
            print(f"\nName: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}\n")
            return

    print("Contact not found.\n")


def update_contact():
    name = input("Enter name to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new phone number: ")
            contact["email"] = input("Enter new email: ")
            print("Contact updated successfully.\n")
            return

    print("Contact not found.\n")       # If no matching contact is found 

# Function to delete a contact
def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)                  # Remove the contact from the list
            print("Contact deleted successfully.\n")
            return

    print("Contact not found.\n")    # If the contact is not found

while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option: ")
# Call the appropriate function based on the user's choice
    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")