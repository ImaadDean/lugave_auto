from models.sale import Sale

def sale_serializer(sale) -> dict:
    return {
        "id": str(sale["_id"]),
        "car_id": sale["car_id"],
        "customer_id": sale["customer_id"],
        "sale_date": sale.get("sale_date"),
        "sale_price": sale.get("sale_price"),
        "total_price": sale.get("total_price"),
        "sale_status": sale.get("sale_status"),
        "payment_type": sale.get("payment_type")
    }

def sales_serializer(sales) -> list:
    return [sale_serializer(sale) for sale in sales]