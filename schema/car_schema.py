from models.car import Car

def car_serializer(car) -> dict:
    return {
        "id": str(car["_id"]),
        "maker": car["maker"],
        "model": car["model"],
        "No_Plate": car["No_Plate"],
        "price": car["price"],
        "date": car.get("date"),
        "Added_by": car.get("Added_by"),
        "status": car.get("status"),
        "year": car.get("year")
    }

def cars_serializer(cars) -> list:
    return [car_serializer(car) for car in cars]