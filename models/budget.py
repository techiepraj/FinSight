from datetime import datetime, timezone
from extensions import db


class Budget(db.Model):
    __tablename__ = "budgets"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    amount = db.Column(db.Numeric(12, 2), nullable=False)
    month = db.Column(db.Integer, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        db.UniqueConstraint("user_id", "category_id", "month", "year", name="uq_budget_user_cat_month"),
        db.CheckConstraint("amount > 0", name="ck_budget_amount_positive"),
        db.CheckConstraint("month BETWEEN 1 AND 12", name="ck_budget_month"),
    )

    user = db.relationship("User", backref=db.backref("budgets", cascade="all, delete-orphan", lazy=True))
    category = db.relationship("Category")