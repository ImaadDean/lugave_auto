from models.payment import Payment

def payment_serializer(payment) -> dict:
    return {
        "id": str(payment["_id"]),
        "sale_id": payment["sale_id"],
        "amount_paid": payment["amount_paid"],
        "payment_date": payment.get("payment_date"),
        "customer_id": payment["customer_id"],
        "car_id": payment["car_id"],
        "balance_after_payment": payment.get("balance_after_payment")
    }

def payments_serializer(payments) -> list:
    return [payment_serializer(payment) for payment in payments]