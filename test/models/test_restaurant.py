from src.models.restaurant import Restaurant
from unittest import TestCase


class TestRestaurant(TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Restaurante ASC", "Comida Francesa")

    def test_describe_restaurant(self):
        number_served = 100
        expected_description = "Esse restaurante chama Restaurante ASC e serve Comida Francesa."
        expected_serving_info = "Esse restaurante está servindo 100 consumidores desde que está aberto."
        expected_output = (expected_description, expected_serving_info)
        output = self.restaurant.describe_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_open_restaurant(self):
        number_served = 0
        expected_output = "Restaurante ASC agora está aberto!"
        output = self.restaurant.open_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_open_restaurant_already_open(self):
        self.restaurant.open = True
        number_served = 10
        expected_output = "Restaurante ASC já está aberto!"
        output = self.restaurant.open_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_open_restaurant_validate_change_status(self):
        self.restaurant.open = False
        number_served = 10
        expected_output = "Restaurante ASC agora está aberto!"
        output = self.restaurant.open_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_open_restaurant_validate_number_server(self):
        self.restaurant.open = False
        number_served = 125
        expected_output = "Restaurante ASC agora está aberto!"
        self.restaurant.open_restaurant(number_served)
        self.assertEqual(self.restaurant.number_served, number_served)

    def test_open_restaurant_is_open(self):
        self.restaurant.open = False
        number_served = 150
        expected_output = "Restaurante ASC agora está aberto!"
        output = self.restaurant.open_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_close_restaurant(self):
        self.restaurant.open = True
        number_served = 0
        expected_output = "Restaurante ASC agora está fechado!"
        output = self.restaurant.close_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_close_restaurant_closed(self):
        self.restaurant.open = False
        number_served = 1000
        expected_output = "Restaurante ASC já está fechado!"
        output = self.restaurant.close_restaurant(number_served)
        self.assertEqual(output, expected_output)

    def test_close_restaurant_validate_status(self):
        self.restaurant.open = True
        number_served = 50
        expected_output = "Restaurante ASC agora está fechado!"
        output = self.restaurant.close_restaurant(number_served)
        self.assertEqual(output, expected_output)
        self.assertFalse(self.restaurant.open)

    def test_set_number_served(self):
        total_customers = 100
        expected_output = "Restaurante ASC já serviu 100 clientes até o momento!"
        output = self.restaurant.set_number_served(total_customers)
        self.assertEqual(output, expected_output)

    def test_set_number_served_close_restaurant(self):
        total_customers = 50
        expected_output = "Restaurante ASC já serviu 50 clientes até o momento!"
        self.restaurant.open = False
        output = self.restaurant.set_number_served(total_customers)
        self.assertEqual(output, expected_output)

    def test_increment_number_served(self):
        initial_number_served = self.restaurant.number_served
        increment = 100
        expected_number_served = initial_number_served + increment

        self.restaurant.increment_number_served(increment)
        self.assertEqual(self.restaurant.number_served, expected_number_served)

    def test_increment_number_served_close_restaurant(self):
        self.restaurant.open = False
        initial_number_served = self.restaurant.number_served
        increment = 100

        self.restaurant.increment_number_served(increment)
        self.assertEqual(self.restaurant.number_served, initial_number_served + increment)