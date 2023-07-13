from src.models.ice_cream_stand import IceCreamStand
from unittest import TestCase

class TestIceCreamStand(TestCase):

    def setUp(self):
        self.flavors_list = ['Pistache', 'Amarula', 'Maracuja']
        self.ice_cream_stand = IceCreamStand("Sorveteria ASC", "Sorveteria", self.flavors_list)

    def test_flavors_available_with_flavors(self):
        expected_output = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n\t-Pistache\n\t-Amarula\n\t-Maracuja"
        self.assertEqual(self.ice_cream_stand.flavors_available(), expected_output)

    def test_flavors_available_without_flavors(self):
        self.ice_cream_stand.flavors = []
        expected_output = "Estamos sem estoque atualmente!"
        self.assertEqual(self.ice_cream_stand.flavors_available(), expected_output)

    def test_find_flavor(self):
        flavor = 'Amarula'
        expected_output = f"Temos no momento {flavor}!"
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), expected_output)

    def test_find_flavor_available(self):
        flavor = 'Pistache'
        expected_output = f"Temos no momento {flavor}!"
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), expected_output)

    def test_find_flavor_unavailable(self):
        flavor = 'Chocolate'
        expected_output = f"Não temos no momento {flavor}!"
        self.assertEqual(self.ice_cream_stand.find_flavor(flavor), expected_output)

    def test_find_flavor_no_input(self):
        expected_output = "Por favor, informe um sabor."
        self.assertEqual(self.ice_cream_stand.find_flavor(None), expected_output)

    def test_add_flavor(self):
        flavor = 'Manga'
        expected_output = f"{flavor} adicionado ao estoque!"
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), expected_output)

    def test_add_flavor_existing(self):
        flavor = 'Amarula'
        expected_output = "Sabor já disponível!"
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), expected_output)

    def test_add_flavor_new(self):
        flavor = 'Passas ao rum'
        expected_output = "Passas ao rum adicionado ao estoque!"
        self.assertEqual(self.ice_cream_stand.add_flavor(flavor), expected_output)
        self.assertIn(flavor, self.ice_cream_stand.flavors)

    def test_add_flavor_no_input(self):
        expected_output = "Por favor, informe um sabor."
        self.assertEqual(self.ice_cream_stand.add_flavor(None), expected_output)