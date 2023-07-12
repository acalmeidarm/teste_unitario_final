from src.models.restaurant import Restaurant


class IceCreamStand(Restaurant):
    """Um tipo especializado de restaurante."""

    def __init__(self, restaurant_name, cuisine_type, flavors_list):
        """
        Inicialize os atributos da classe pai.
        Em seguida, inicialize os atributos específicos de uma sorveteria.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors_list

    def flavors_available(self):
        """Percorra a lista de sabores disponíveis e imprima."""
        """corrigido para Retornar os sabores disponíveis e não imprimir e adicionado validação 
        para verificar se o nome foi passado."""

        if self.flavors:
            message = "\nNo momento temos os seguintes sabores de sorvete disponíveis:\n"
            flavors_list = "\n".join(f"\t-{flavor}" for flavor in self.flavors)
            return message + flavors_list
        else:
            return "Estamos sem estoque atualmente!"

    def find_flavor(self, flavor):
        """Verifica se o sabor informado está disponível."""
        """corrigido para Retornar os sabores disponíveis e não imprimir e adicionado validação 
        para verificar se o nome foi passado."""
        if not flavor:
            return "Por favor, informe um sabor."

        if self.flavors:
            if flavor in self.flavors:
                return f"Temos no momento {flavor}!"
            else:
                return f"Não temos no momento {flavor}!"
        else:
            return "Estamos sem estoque atualmente!"

    def add_flavor(self, flavor):
        """Adiciona o sabor informado ao estoque."""
        if not flavor:
            return "Por favor, informe um sabor."

        if self.flavors:
            if flavor in self.flavors:
                return "Sabor já disponível!"
            else:
                self.flavors.append(flavor)
                return f"{flavor} adicionado ao estoque!"
        else:
            return "Estamos sem estoque atualmente!"