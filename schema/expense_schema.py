from models.expense import Expense

def expense_serializer(expense) -> dict:
    return {
        "id": str(expense["_id"]),
        "Car_id": expense["Car_id"],
        "amount": expense["amount"],
        "date": expense.get("date"),
        "category": expense.get("category"),
        "description": expense.get("description")
    }

def expenses_serializer(expenses) -> list:
    return [expense_serializer(expense) for expense in expenses]