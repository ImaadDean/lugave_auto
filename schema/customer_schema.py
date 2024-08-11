from models.customer import Customer

def customer_serializer(customer) -> dict:
    return {
        "id": str(customer["_id"]),
        "first_name": customer["first_name"],
        "last_name": customer["last_name"],
        "telephone": customer.get("telephone"),
        "address": customer.get("address"),
    }

def customers_serializer(customers) -> list:
    return [customer_serializer(customer) for customer in customers]