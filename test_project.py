import pytest
import os
import json
from messages import add_message, delete_message
from datetime import date
from people import Person, edit_person, delete_person

TEST_DIRECTORY = "./test_data"  # Directory to store test data files
TEST_FILE_PREFIX = "tier"  # Prefix for test data files

# Pytest fixture for setting up the environment before each test and cleaning up afterwards
@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Create the test directory
    os.makedirs(TEST_DIRECTORY, exist_ok=True)
    # Set an environment variable for the test
    os.environ["USERNAME"] = "test_user"
    yield  # This is where the testing happens
    # Cleanup: remove created files and directory after each test
    for filename in os.listdir(TEST_DIRECTORY):
        os.remove(os.path.join(TEST_DIRECTORY, filename))
    os.rmdir(TEST_DIRECTORY)
    os.unsetenv("USERNAME")  # Unset the environment variable

# Test the add_message function
def test_add_message():
    test_message = "Hello, this is a test."
    test_tier = 1
    add_message(test_message, test_tier)  # Add a test message
    expected_file_path = f"{TEST_DIRECTORY}/tier{test_tier}.json"
    assert os.path.exists(expected_file_path), "File was not created"  # Check if the file is created
    with open(expected_file_path, 'r') as file:
        data = json.load(file)
    assert test_message in data["messages"], "Message was not added"  # Check if the message is in the file

# Test the delete_message function
def test_delete_message():
    test_message = "Message to delete"
    test_tier = 2
    add_message(test_message, test_tier)  # Add a message to be deleted

    delete_message(test_tier, test_message)  # Delete the message
    expected_file_path = f"{TEST_DIRECTORY}/tier{test_tier}.json"
    with open(expected_file_path, 'r') as file:
        data = json.load(file)
    assert test_message not in data["messages"], "Message was not deleted"  # Check if the message was deleted

# Test deleting all messages
def test_delete_all_messages():
    messages = ["First message", "Second message", "Third message"]
    test_tier = 3
    for message in messages:
        add_message(message, test_tier)  # Add multiple messages

    delete_message(test_tier)  # Delete all messages in the tier
    expected_file_path = f"{TEST_DIRECTORY}/tier{test_tier}.json"
    with open(expected_file_path, 'r') as file:
        data = json.load(file)
    assert not data["messages"], "Not all messages were deleted"  # Check if all messages were deleted

# Test checking for birthdays or namedays
def test_is_birthday_or_nameday():
    person = Person('John Doe', 12, 25, '12345678', 6, 15, 'A', 'no')
    # Check different dates for birthday and nameday
    assert person.is_birthday_or_nameday(date(2023, 12, 25)) == True
    assert person.is_birthday_or_nameday(date(2023, 6, 15)) == True
    assert person.is_birthday_or_nameday(date(2023, 1, 1)) == False

# Test editing a person's details
def test_edit_person():
    people = [{'name': 'John Doe', 'birth_month': 12, 'birth_day': 25, 'phone_number': '12345678', 'nameday_month': 6, 'nameday_day': 15, 'tier': 'A', 'sent': 'no'}]

    edited_people = edit_person(people, '12345678', 'birth_month', 11)  # Edit person's birth month
    assert edited_people[0]['birth_month'] == 11  # Check if the birth month was updated

# Test deleting a person
def test_delete_person():
    people = [{'name': 'John Doe', 'phone_number': '12345678'}]
    updated_people = delete_person('12345678', people)  # Delete the person
    assert len(updated_people) == 0  # Check if the person list is empty after deletion

