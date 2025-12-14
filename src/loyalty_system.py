from datetime import datetime, timedelta
from src.customer import Customer


class LoyaltySystem:
    POINT_VALUE = 0.05

    MULTIPLIERS = {"STANDARD": 1.0, "PREMIUM": 1.5, "VIP": 2.0}

    def __init__(self):
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def find_customer(self, name: str) -> Customer:
        for customer in self.customers:
            if customer.name == name:
                return customer
        raise ValueError("Cliente inexistente")

    def remove_customers_with_zero_points(self):
        self.customers = [c for c in self.customers if c.points > 0]

    def register_purchase(self, name: str, value: float, bonus=0):
        if value <= 0:
            return

        customer = self.find_customer(name)
        multiplier = self.MULTIPLIERS[customer.customer_type]

        points = value * multiplier + bonus
        customer.points += points

        customer.history.append({"points": points, "date": datetime.now()})

    def get_points(self, name: str) -> float:
        return self.find_customer(name).points

    def redeem_points(self, name: str, points: float) -> float:
        customer = self.find_customer(name)

        if points > customer.points:
            raise ValueError("Saldo insuficiente")

        customer.points -= points
        return points * self.POINT_VALUE

    def expire_old_points(self, days: int):
        limit = datetime.now() - timedelta(days=days)

        for customer in self.customers:
            valid_history = []
            expired_points = 0

            for h in customer.history:
                if h["date"] < limit:
                    expired_points += h["points"]
                else:
                    valid_history.append(h)

            customer.history = valid_history
            customer.points = max(0, customer.points - expired_points)

    def filter_customers_above_points(self, limit: float):
        return [c for c in self.customers if c.points > limit]

    def sort_customers_by_points(self):
        return sorted(self.customers, key=lambda c: c.points, reverse=True)

    def total_points(self):
        return sum(c.points for c in self.customers)
