# Whatsapp Birthday and Nameday messenger
#### Video Demo:  <https://youtu.be/YL7r0Hn-G5Q>
#### Description:
Very often I struggle with remembering to send a "Happy birthday" message to my friends on their birthdays or namedays. Sometimes when I do remember their birthday, I put off sending message for later, which leads me to forget again. With this in mind, I thought that this would be the time to put a stop to that, by creating a program that does that for me. This program sends a random message from 5 different lists based on the persons tier level (1) which I had chosen previously. Every time I startup my computer, the application gets started.

# How the application works?:

I have 4 python files. -people.py, messages.py, sendmessage.py, project.py

***People.py*** In this codes's terminal, I have the option to add;edit;delete a person from my dictionary. When creating a person it asks for Name, Phone number, Birthday month, Birthday day and Tier level # (1).It then compares the name to all of the names inside varda_dienas.csv, and checks if it matches any  of the names, if it does it also adds a nameday date to the person. This person is then added to Documents/data/people.json file, I chose to place the json files there as this folder is easily acessible and does not take place on desktop or some other random folder, for users to work, they'd have to add a data folder to Documents. The edit function allows to edit any of the already added persons, and the delete function allows to delete persons.

***Messages.py*** This code allows to add or delete messages to any of tiers through 1-5.

***Sendmessage.py*** This is the part of the code, where the actual message sending via WhatsApp happen. By using Selenium libaries, I can easily automate tasks on any of browsers. For my program, I have chosen to work with chrome, as it is the most basic. I have put the program in headless mode to not disrupt the user. When a message needs to be sent it starts WhatsApp class and launches WhatsApp Web via Chrome, it then automatically logs in the users whatsapp(3), which is possible to the Users saved Data folder in Chromes local folders. It then uses search_contact to find the person having birthday/nameday by searching their phone number in the search bar, it then selects the messagebox, and sends a one of the messages randomly for the persons tier level. When this is done, the program stops. It is started on the next launch again.

***Project.py*** This is the main part of the code, which starts by checking today's date using datetime library. Loads the people.json in, and checks if any of the birthday/nameday dates matches today's date. If it does, and the status of the person is sent: "no", it does ***Sendmessage.py*** and then changes sent:"no", to sent:"yes", so it does not try to send again.

I would like to mention, that for the program to be portable, I made the program automatically get users desktop name using os library with this line "user_name = os.getenv("USERNAME") or "default_user"", so it can automatically input it here. /Users/{user_name}/AppData/ or any other place it is needed.


* 1) I implemented tier levels, because I do not want to send the same type of message, for example, to my grandparents as to my school friends. Logically they will differ in how I write to them. Sometimes I need to send more formal greetings, or maybe something silly, that's why I implemented tiers 1-5.

* 2) Headless mode is an argument to make the browser not visible, thus making the application work in the background without interrupting the user.

* 3) User must sync/login in WhatsApp Web once, before using the program for the first time, to save user data.

# Usage:
1) Place my given data folder inside their pc's Documents folder
2) Adds persons and messages via terminal
3) Places my compiled .exe file inside startup folder. It can be done, by pressing Win+R and typing "shell:startup", and just drag in the exe file there. This will make it start every time computer is launched.
4) That's it!
