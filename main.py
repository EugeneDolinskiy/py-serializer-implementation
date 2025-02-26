from car.models import Car
from car.serializers import CarSerializer

import json


def serialize_car_object(car: Car) -> bytes:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data).encode("utf-8")


def deserialize_car_object(json: bytes) -> Car:
    json_str = json.decode("utf-8")
    data = json.loads(json_str)

    return Car(**data)
