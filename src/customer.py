from datetime import datetime


class Customer:
    def __init__(self, name: str, customer_type="STANDARD", points=0):
        if not name:
            raise ValueError("Nome do cliente é obrigatório")

        self.name = name
        self.customer_type = customer_type
        self.points = float(points)
        self.history = []
        self.created_at = datetime.now()
