import json
import os
from .contact import Contact

DATAFILE = "contacts.json"

class Phonebook:
    def __init__(self):
        self.contacts = []
        self.load()

    def load(self):
        if not os.path.exists(DATAFILE):
            print("[INFO] No contacts found. Starting with an empty phonebook.")
            return

        try:
            with open(DATAFILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.contacts = [Contact.from_dict(c) for c in data]
            print(f"[SUCCESS] Loaded {len(self.contacts)} contact(s).")
        except:
            print("[ERROR] Could not load contacts.json.")

    def save(self):
        with open(DATAFILE, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)
        print("[SUCCESS] Contacts saved.")

    def add(self, first, last, phone, email):
        for c in self.contacts:
            if c.phone == phone:
                print("[ERROR] Phone number already exists.")
                return False
        new = Contact(first, last, phone, email)
        self.contacts.append(new)
        print(f"[SUCCESS] Contact '{first} {last}' added.")
        return True

    def remove(self, phone):
        for c in self.contacts:
            if c.phone == phone:
                confirm = input(f"Delete {c.first} {c.last}? (Y/N): ").lower()
                if confirm == "y":
                    self.contacts.remove(c)
                    print("[SUCCESS] Contact removed.")
                else:
                    print("[INFO] Cancelled.")
                return
        print("[ERROR] Contact not found.")

    def search(self, term):
        results = [
            c for c in self.contacts
            if term.lower() in c.first.lower()
            or term.lower() in c.last.lower()
            or term in c.phone
        ]
        if not results:
            print("[INFO] No matches found.")
            return
        for c in results:
            print(c)

    def list_all(self):
        if not self.contacts:
            print("(no contacts)")
            return
        print("\n--- All Contacts ---")
        for c in sorted(self.contacts, key=lambda x: (x.first, x.last)):
            print(c)
