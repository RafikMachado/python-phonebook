Python Phonebook Manager: Object-Oriented Console App ☎️
Project Overview

This is a clean and simple command-line Phonebook Manager written in Python, designed for the Object-Oriented Programming project for Group 5.

The goal of this application is to manage contacts — storing First Name, Last Name, Phone Number, and Email — using Python classes and JSON for data persistence.

This project demonstrates OOP principles such as:

Encapsulation (Contact objects)

Data storage through a Phonebook class

Methods for CRUD operations

Input validation

File persistence using JSON

When the program starts, it automatically attempts to load previously saved contacts from contacts.json.

Getting Started: Installation & Setup 🛠️
1. Install Python

You need Python 3.8+ installed on your machine.

2. Download/Clone the Repository
git clone https://github.com/YOUR_USERNAME/python-phonebook.git
cd python-phonebook

3. Run the Application
python main.py


The program will automatically try to load contacts.json.

Key Features

This phonebook implements all required functions:

Add Contact
Validates for duplicate names and duplicate phone numbers.

Delete Contact
Remove by phone number (safe and unique) with confirmation.

Search Contact
Search by first name, last name, or partial phone number.

View All Contacts
Nicely formatted list of all contacts.
Supports sorting by first name or last name.

Save & Load Automatically
Uses JSON (contacts.json) to store contacts.

Execution Examples 🧪
Scenario 1: Add & List
Action	Input	Expected Output
Run Program	python main.py	[INFO] No contacts found. Starting with an empty phonebook.
Add Contact	Menu 1 → John Doe, 555-1234, john@gmail.com
	[SUCCESS] Contact 'John Doe' added.
View All	Menu 4	Shows John Doe
Scenario 2: Search & Delete
Action	Input	Expected Output
Search	Menu 3 → "Doe"	Displays John Doe
Delete	Menu 2 → 555-1234 → Confirm "Y"	[SUCCESS] Contact removed.
View All	Menu 4	Phonebook now empty
Scenario 3: Save & Reload
Action	Input	Expected Output
Add Contact	Jane Smith	[SUCCESS]
Save	Menu 5	[SUCCESS] Contacts saved.
Exit	Menu 0	Program ends
Restart	python main.py	[SUCCESS] Loaded 1 contact from contacts.json.
Repository Contents
python-phonebook/
│── phonebook/
│     ├── contact.py        # Contact class
│     ├── phonebook.py      # Phonebook logic
│── main.py                  # CLI menu
│── contacts.json            # Created at runtime
│── README.md                # Project documentation
│── .gitignore               # Ignores JSON files + pycache

Notes

JSON was chosen for readability and flexibility.

Duplicate checking is handled strictly by phone number, and optionally by name.

Sorting uses Python’s built-in sorted() with lambda keys.
