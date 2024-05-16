import datetime
import json
import random
from sendmessage import whatsapp
import os

#Global variable for today's date
today = datetime.date.today()
user_name = os.getenv("USERNAME") or "default_user"

def load_people_data():
    """
    Loads people data from a JSON file located in the user's Documents directory.

    Returns:
        list: A list of dictionaries, each representing a person's data.
    """
    with open(f'C:/Users/{user_name}/Documents/data/people.json', 'r') as file:
        return json.load(file)

def send_greeting(people):
    """
    Sends greetings to people whose birthday or nameday is today.

    Iterates through a list of people, checks if today matches their birthday or nameday,
    and sends a greeting message if a message has not already been sent.

    Args:
        people (list): A list of dictionaries, each representing a person's data.
    """
    for person in people:
        if (today.month == person['birth_month'] and today.day == person['birth_day']) or \
           (today.month == person['nameday_month'] and today.day == person['nameday_day']):
            
            if person['sent'] == 'yes':
                continue

            tier_number = str(person["tier"]).replace("tier", "")
            with open(f'C:/Users/{user_name}/Documents/data/tier{tier_number}.json', 'r') as file:
                tier_data = json.load(file)
                messages = tier_data["messages"]

            if messages:
                message = random.choice(messages)
                whatsapp.search_contact(person['phone_number'])
                whatsapp.send_message(message)
                person['sent'] = 'yes'
                update_sent_status(people)
            else:
                print(f"No messages found for tier {person['tier']}")
        else:
            print(f"Today is not {person['name']}'s birthday or nameday")

def update_sent_status(people):
    """
    Updates the 'sent' status of people in the JSON file after sending messages.

    Args:
        people (list): A list of dictionaries, each representing a person's data.
    """
    with open(f'C:/Users/{user_name}/Documents/data/people.json', 'w') as file:
        json.dump(people, file)

def main():
    """
    Main function that loads people data and sends greetings if applicable.
    """
    people = load_people_data()
    send_greeting(people)

if __name__ == '__main__':
    main()
