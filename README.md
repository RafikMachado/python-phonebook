Here’s a polished rewrite of your project description, keeping it clear, professional, and engaging:

---

# Python Phonebook Manager: Object-Oriented Console App ☎️

## Project Overview

This is a simple and intuitive command-line **Phonebook Manager** built in Python, created as an **Object-Oriented Programming** project for Group 5.

The app allows you to manage contacts by storing **First Name, Last Name, Phone Number, and Email**, using Python classes and **JSON** for persistent storage.

### Key Object-Oriented Concepts Demonstrated

* **Encapsulation** via `Contact` objects
* **Data management** through the `Phonebook` class
* **CRUD operations** using dedicated methods
* **Input validation** to ensure data integrity
* **File persistence** with JSON for automatic saving and loading

On startup, the program automatically loads any existing contacts from `contacts.json`.

---

## Getting Started: Installation & Setup 🛠️

### 1. Install Python

Ensure **Python 3.8+** is installed on your system.

### 2. Download or Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/python-phonebook.git
cd python-phonebook
```

### 3. Run the Application

```bash
python main.py
```

The program will attempt to automatically load `contacts.json` if it exists.

---

## Key Features

This phonebook includes all essential functions:

* **Add Contact**

  * Prevents duplicate names and phone numbers

* **Delete Contact**

  * Remove by unique phone number with confirmation

* **Search Contact**

  * Search by first name, last name, or partial phone number

* **View All Contacts**

  * Nicely formatted list with optional sorting by first or last name

* **Automatic Save & Load**

  * Contacts are stored in `contacts.json` using JSON format

---

## Execution Examples 🧪

### Scenario 1: Add & List

| Action      | Input                                                                | Expected Output                                               |
| ----------- | -------------------------------------------------------------------- | ------------------------------------------------------------- |
| Run Program | `python main.py`                                                     | `[INFO] No contacts found. Starting with an empty phonebook.` |
| Add Contact | Menu 1 → John Doe, 555-1234, [john@gmail.com](mailto:john@gmail.com) | `[SUCCESS] Contact 'John Doe' added.`                         |
| View All    | Menu 4                                                               | Displays John Doe                                             |

### Scenario 2: Search & Delete

| Action   | Input                           | Expected Output              |
| -------- | ------------------------------- | ---------------------------- |
| Search   | Menu 3 → "Doe"                  | Displays John Doe            |
| Delete   | Menu 2 → 555-1234 → Confirm "Y" | `[SUCCESS] Contact removed.` |
| View All | Menu 4                          | Phonebook now empty          |

### Scenario 3: Save & Reload

| Action      | Input            | Expected Output                                  |
| ----------- | ---------------- | ------------------------------------------------ |
| Add Contact | Jane Smith       | `[SUCCESS] Contact added.`                       |
| Save        | Menu 5           | `[SUCCESS] Contacts saved.`                      |
| Exit        | Menu 0           | Program ends                                     |
| Restart     | `python main.py` | `[SUCCESS] Loaded 1 contact from contacts.json.` |

---

## Repository Structure

```
python-phonebook/
│── phonebook/
│     ├── contact.py        # Contact class
│     ├── phonebook.py      # Phonebook logic
│── main.py                  # CLI menu
│── contacts.json            # Created at runtime
│── README.md                # Project documentation
│── .gitignore               # Ignores JSON files and __pycache__
```

---

## Notes

* **JSON** was chosen for readability and flexibility.
* Duplicate checking is **strictly by phone number**, optionally by name.
* Sorting is handled with Python’s `sorted()` function using `lambda` keys.

---



