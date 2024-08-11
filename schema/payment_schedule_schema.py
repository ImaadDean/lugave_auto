from models.payment_schedule import PaymentSchedule

def payment_schedule_serializer(schedule) -> dict:
    return {
        "id": str(schedule["_id"]),
        "sale_id": schedule["sale_id"],
        "total_amount": schedule.get("total_amount"),
        "amount_paid": schedule.get("amount_paid"),
        "remaining_balance": schedule.get("remaining_balance"),
        "next_due_date": schedule.get("next_due_date"),
        "installment_amount": schedule.get("installment_amount")
    }

def payment_schedules_serializer(schedules) -> list:
    return [payment_schedule_serializer(schedule) for schedule in schedules]