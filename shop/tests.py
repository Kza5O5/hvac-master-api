from django.test import TestCase
from .models import Car

class CarTest(TestCase):
    def test_car_create(self):
        car = Car.objects.create(name="BMW", price="10000")
        self.assertEqual(car.name, "BMW")