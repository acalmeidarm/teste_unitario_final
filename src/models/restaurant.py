class Restaurant:
    """Model de restaurante simples."""

    # Removido o .title() do restaurant_name
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        self.open = False

    def describe_restaurant(self, number_served):
        """Retorna uma descrição simples da instância do restaurante."""
        # Corrigido para retornar os valores ao invés de imprimir
        # Corrigido para retornar o nome do restaurante e para retornar o número informado de clientes atendidos
        description = f"Esse restaurante chama {self.restaurant_name} e serve {self.cuisine_type}."
        serving_info = f"Esse restaurante está servindo {number_served} consumidores desde que está aberto."
        return description, serving_info

    def open_restaurant(self, number_served):
        """Retorna uma mensagem indicando que o restaurante está aberto para negócios."""
        if not self.open:
            self.open = True
            self.number_served = number_served
            return f"{self.restaurant_name} agora está aberto!"
        else:
            return f"{self.restaurant_name} já está aberto!"

    def close_restaurant(self, number_served):
        """Retorna uma mensagem indicando que o restaurante está fechado para negócios."""
        if self.open:
            self.open = False
            self.number_served = number_served
            return f"{self.restaurant_name} agora está fechado!"
        else:
            return f"{self.restaurant_name} já está fechado!"


    def set_number_served(self, total_customers):
        """Define o número total de pessoas atendidas por este restaurante até o momento."""
        #  Alterado a lógica para o total de pessoas e a mensagem que vai retornar
        self.number_served = total_customers
        return f"{self.restaurant_name} já serviu {self.number_served} clientes até o momento!"

    def increment_number_served(self, more_customers):
        """Aumenta número total de clientes atendidos por este restaurante."""
        #  Alterado a lógica para aumentar o numero de pessoas e a mensagem que vai retornar
        self.number_served = more_customers
        return f"{self.restaurant_name} já atendeu {self.number_served} clientes novos!"