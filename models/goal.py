from datetime import datetime, timezone
from extensions import db


class FinancialGoal(db.Model):
    __tablename__ = "financial_goals"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    name = db.Column(db.String(100), nullable=False)
    target_amount = db.Column(db.Numeric(12, 2), nullable=False)
    current_amount = db.Column(db.Numeric(12, 2), nullable=False, default=0)
    deadline = db.Column(db.Date, nullable=True)
    created_at = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        db.CheckConstraint("target_amount > 0", name="ck_goal_target_positive"),
        db.CheckConstraint("current_amount >= 0", name="ck_goal_current_nonneg"),
    )

    user = db.relationship("User", backref=db.backref("goals", cascade="all, delete-orphan", lazy=True))
    