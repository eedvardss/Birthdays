import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

user_name = os.getenv("USERNAME") or "default_user"

class Whatsapp:
    """
    A class to interact with WhatsApp Web using Selenium WebDriver.

    This class provides methods to initialize a WebDriver session, search for contacts, and send messages
    using WhatsApp Web.

    Attributes:
        driver (webdriver.Chrome): A Chrome WebDriver instance to interact with the WhatsApp Web interface.
        wait (WebDriverWait): An explicit wait to handle dynamic loading elements in the web page.
    """

    def __init__(self):
        """
        Initializes the Chrome WebDriver with specific options to access WhatsApp Web.

        The WebDriver is configured to run in headless mode with a custom user data directory.
        It navigates to the WhatsApp Web page and waits until the main UI is loaded.
        """
        options = Options()
        options.add_argument(f"--user-data-dir=C:/Users/{user_name}/AppData/Local/Google/Chrome/User Data")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--ingore-certificate-errors")
        options.add_argument("--allow-running-insecure-content")
        print("Initializing WebDriver...")
        self.driver = webdriver.Chrome(options=options)
        try:
            self.driver.get("https://web.whatsapp.com/")
            print("Navigating to WhatsApp Web...")
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="side"]')))
            print("WhatsApp Web loaded successfully.")
        except Exception as e:
            print("Error opening the browser:", e)

    def search_contact(self, phone_number):
        """
        Searches for a contact on WhatsApp Web using the provided phone number.

        Args:
            phone_number (str): The phone number of the contact to be searched.
        """
        try:
            print(f"Attempting to search for contact: {phone_number}")
            search_box = self.driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]')
            search_box.clear()
            search_box.send_keys(phone_number)
            search_box.send_keys(Keys.ENTER)
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@class="_33LGR"]')))
            print("Contact search completed.")
        except Exception as e:
            print(f"Error during contact search: {e}")

    def send_message(self, message):
        """
        Sends a message to the currently selected contact on WhatsApp Web.

        Args:
            message (str): The message text to be sent.
        """
        print(f"Preparing to send message: {message}")
        try:
            message_box_path = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            message_box = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((By.XPATH, message_box_path)))
            print("Message box found. Sending message...")
            message_box.send_keys(message + Keys.ENTER)
            time.sleep(15)
            print("Message sent successfully.")
        except Exception as e:
            print(f"Error sending message: {e}")

whatsapp = Whatsapp()
