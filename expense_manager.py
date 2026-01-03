from datetime import datetime
from expense import Expense
from storage import load_data, save_data


class ExpenseManager:
    def __init__(self):
        self.data = load_data()
        self.expenses = [
            Expense.from_dict(e) for e in self.data["expenses"]
        ]

    def _next_id(self):
        self.data["last_id"] += 1
        return self.data["last_id"]

    def _persist(self):
        self.data["expenses"] = [e.to_dict() for e in self.expenses]
        save_data(self.data)

    def add(self, category, description, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        expense = Expense(
            id=self._next_id(),
            date=datetime.now().strftime("%Y-%m-%d"),
            category=category,
            description=description,
            amount=amount
        )
        self.expenses.append(expense)
        self._persist()
        return expense.id

    def list(self):
        return self.expenses

    def delete(self, expense_id):
        for e in self.expenses:
            if e.id == expense_id:
                self.expenses.remove(e)
                self._persist()
                return True
        return False

    def summary(self):
        total = sum(e.amount for e in self.expenses)
        return total, self.expenses

    def list_by_category(self):
        category_map = {}
        total_amount = sum(e.amount for e in self.expenses)

        for e in self.expenses:
            category_map.setdefault(e.category, []).append(e)

        result = {}
        for category, items in category_map.items():
            cat_total = sum(i.amount for i in items)
            percentage = (cat_total / total_amount) * 100 if total_amount else 0
            result[category] = {
                "total": cat_total,
                "percentage": round(percentage),
                "items": items
            }

        return result
