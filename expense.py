class Expense:
    def __init__(self, id, date, category, description, amount):
        self.id = id
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "category": self.category,
            "description": self.description,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["id"],
            data["date"],
            data["category"],
            data["description"],
            data["amount"]
        )
