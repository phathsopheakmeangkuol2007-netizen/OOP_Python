class Order:
    def __init__(self, order_id, total):
        self.order_id = order_id
        self.total = total
    def get_total(self):
        return self.total

class DiscountedOrder(Order):
    def __init__(self, order_id, total):
        super().__init__(order_id, total)
    def get_total(self):
        return self.total * 0.9

d = DiscountedOrder("ORD001", 1200)
print(f"Order ID: {d.order_id}")
print(f"Original Total: {d.total}")
print(f"Discount Total: {d.get_total()}")

