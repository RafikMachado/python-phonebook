class Contact:
    def __init__(self, first, last, phone, email):
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "first": self.first,
            "last": self.last,
            "phone": self.phone,
            "email": self.email
        }

    @staticmethod
    def from_dict(d):
        return Contact(d["first"], d["last"], d["phone"], d["email"])

    def __str__(self):
        return f"{self.first} {self.last} | {self.phone} | {self.email}"
