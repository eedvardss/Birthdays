import os
import json
import csv

# Retrieves the current user's name from the environment or defaults to "default_user"
user_name = os.getenv("USERNAME") or "default_user"

class Person:
    """
    Represents a person with attributes for name, birth date, nameday, phone number, tier, and a sent flag.

    Attributes:
        name (str): The person's name.
        birth_month (int): The month of birth.
        birth_day (int): The day of birth.
        phone_number (str): The person's phone number.
        nameday_month (int): The month of the nameday.
        nameday_day (int): The day of the nameday.
        tier (str): The category or level of the person.
        sent (str): A flag indicating whether a message has been sent.
    """

    def __init__(self, name, birth_month, birth_day, phone_number, nameday_month, nameday_day, tier, sent):
        """
        Initializes a new instance of the Person class with the given details.
        """
        self.name = name
        self.birth_month = birth_month
        self.birth_day = birth_day
        self.phone_number = phone_number
        self.nameday_month = nameday_month
        self.nameday_day = nameday_day
        self.tier = tier
        self.sent = sent

    def is_birthday_or_nameday(self, today):
        """
        Checks whether the current date matches the person's birthday or nameday.

        Parameters:
            today (datetime.date): The current date to check against.

        Returns:
            bool: True if today is either the birthday or nameday of the person, False otherwise.
        """
        return (today.month == self.birth_month and today.day == self.birth_day) or \
               (today.month == self.nameday_month and today.day == self.nameday_day)

def add_person():
    """
    Prompts the user for person details, reads nameday from a file, and returns a dictionary representing the person.

    Returns:
        dict: A dictionary containing the person's details.
    """
    name = input("Name: ")
    sent = "no"

    # Reads the nameday from a predefined CSV file based on the given name
    with open(f'C:/Users/{user_name}/Documents/data/varda_dienas.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            names = row[1].lower().replace("\"", "").split(", ")
            if name.lower() in names:
                name_date = row[0]
                break
        else:
            name_date = None

    if name_date:
        nameday_day, nameday_month = map(int, name_date.split('.'))
    else:
        nameday_day = nameday_month = None

    phone_number = input("Phone Number (8 digits): ")
    while len(phone_number) != 8 or not phone_number.isdigit():
        print("Invalid phone number. Please enter exactly 8 digits.")
        phone_number = input("Phone Number (8 digits): ")

    birth_month = int(input("Birth Month (1-12): "))
    while birth_month < 1 or birth_month > 12:
        print("Invalid month. Please enter a number between 1 and 12.")
        birth_month = int(input("Birth Month (1-12): "))

    birth_day = int(input("Birth Day (1-31): "))
    while birth_day < 1 or birth_day > 31:
        print("Invalid day. Please enter a number between 1 and 31.")
        birth_day = int(input("Birth Day (1-31): "))

    tier = input("Tier: ")  

    return Person(name, birth_month, birth_day, phone_number, nameday_month, nameday_day, tier, sent).__dict__

def edit_person(people):
    """
    Edits details of a person identified by phone number in the provided list of people.

    Parameters:
        people (list): A list of dictionaries representing people.

    Returns:
        list: The updated list of people after editing.
    """
    phone_number = input("Enter the phone number of the person to edit: ").strip()
    print(f"Looking for phone number: {phone_number}")

    found = False
    for person in people:
        print(f"Comparing with: {person['phone_number']}")
        if person['phone_number'].strip() == phone_number:
            found = True
            detail = input("Enter the detail to edit (name, Birthday month, Birthday day, Nameday month, Nameday day): ").strip()
            if detail in person:
                new_value = input(f"Enter the new {detail}: ").strip()
                if detail in ['birth_month', 'birth_day', 'nameday_month', 'nameday_day']:
                    person[detail] = int(new_value)
                else:
                    person[detail] = new_value
                print(f"Updated {detail} for {person['name']}.")
                break
            else:
                print(f"Invalid detail: {detail}")

    if not found:
        print(f"No person found with phone number {phone_number}")
    return people

def delete_person(phone_number, people):
    """
    Deletes a person identified by phone number from the provided list of people.

    Parameters:
        phone_number (str): The phone number of the person to delete.
        people (list): The list of people from which to delete.

    Returns:
        list: The updated list of people after deletion.
    """
    for i, person in enumerate(people):
        if person['phone_number'] == phone_number:
            del people[i]
            print(f"Deleted person with phone number {phone_number}")
            break
    else:
        print(f"No person found with phone number {phone_number}")

def main():
    """
    Main function to run the interactive program allowing the user to add, edit, or delete a person.
    """
    while True:
        print("\n1. Add a new person")
        print("2. Edit an existing person")
        print("3. Delete a person")
        print("4. Exit")
        choice = input("Enter your choice: ")

        path = f'C:/Users/{user_name}/Documents/data/people.json'
        if os.path.exists(path):
            with open(path, 'r') as file:
                existing_people = json.load(file)
        else:
            existing_people = []

        if choice == '1':
            number_of_people = 0
            while number_of_people <= 0:
                try:
                    number_of_people = int(input("How many people you want to add? "))
                    if number_of_people <= 0:
                        print("Please enter a number greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            for _ in range(number_of_people):
                new_person = add_person()
                existing_people.append(new_person)
            with open(path, "w") as json_file:
                json.dump(existing_people, json_file, indent=2)
        elif choice == '2':
            existing_people = edit_person(existing_people)
            with open(path, "w") as json_file:
                json.dump(existing_people, json_file, indent=2)
        elif choice == '3':
            phone_number = input("Enter the phone number of the person to delete: ")
            delete_person(phone_number, existing_people)
            with open(path, 'w') as file:
                json.dump(existing_people, file, indent=2)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()