from app import app
from extensions import db
from models import Category

EXPENSE = ["Food", "Groceries", "Transportation", "Rent", "Utilities", "Shopping",
           "Entertainment", "Healthcare", "Education", "Travel", "Subscriptions",
           "Personal", "Other"]
INCOME = ["Salary", "Freelance", "Business", "Scholarship", "Investment Income", "Other"]

with app.app_context():
    db.create_all()  # creates any missing tables

    if Category.query.filter_by(is_default=True).count() == 0:
        for name in EXPENSE:
            db.session.add(Category(name=name, type="expense", is_default=True))
        for name in INCOME:
            db.session.add(Category(name=name, type="income", is_default=True))
        db.session.commit()
        print("Default categories added.")
    else:
        print("Default categories already exist.")