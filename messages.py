import json
import os

# Retrieve the current user's name from the environment or default to "default_user"
user_name = os.getenv("USERNAME") or "default_user"

def add_message(message, tier):
    """
    Adds a message to a specified tier file in JSON format.

    Args:
        message (str): The message to add.
        tier (int): The tier number indicating which file to append the message to.

    The function opens the corresponding JSON file for the specified tier, reads the existing
    data, appends the new message, and writes back to the file. If the file does not exist,
    it creates a new one.
    """
    filename = f"C:/Users/{user_name}/Documents/data/tier{tier}.json"
    data = {"messages": []}
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        pass
    data["messages"].append(message)
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def delete_message(tier, message=None):
    """
    Deletes a message from a specified tier file or all messages if no specific message is provided.

    Args:
        tier (int): The tier number indicating which file to delete the message from.
        message (str, optional): The message to delete. If not specified, all messages in the file are deleted.

    The function reads from the specified tier JSON file, removes the specified message or all
    messages if none is specified, and writes the updated data back to the file.
    """
    filename = f"tier{tier}.json"
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        if message:
            data["messages"].remove(message)
        else:
            data["messages"].clear()
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except (FileNotFoundError, ValueError):
        pass

def get_input():
    """
    Interactively prompts the user to add or delete messages within specified tiers.

    This function guides the user through adding or deleting messages, asking for necessary
    details like the tier number and the message content. Based on user input, it calls
    either `add_message` or `delete_message`.
    """
    action = input("Do you want to add or delete a message? (add/delete): ")
    tier = 0
    while tier < 1 or tier > 5:
        try:
            tier = int(input("Enter the tier (1-5): "))
            if tier < 1 or tier > 5:
                print("Between 1 and 5.")
        except ValueError:
            print("Numbers only.")
    if action == "add":
        message = input("Enter the message: ")
        add_message(message, tier)
    elif action == "delete":
        delete_all = input("Do you want to delete all messages? (yes/no): ")
        if delete_all == "yes":
            delete_message(tier)
        else:
            message = input("Enter the message to delete: ")
            delete_message(tier, message)

get_input()
