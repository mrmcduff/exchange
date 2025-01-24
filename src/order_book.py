import pandas as pd
from order import Order, OrderType


class OrderBook:
    def __init__(self):
        self.buy_orders = pd.DataFrame(columns=["price", "quantity", "timestamp"])
        self.sell_orders = pd.DataFrame(columns=["price", "quantity", "timestamp"])

    def show_book(self, order_type: OrderType):
        if order_type == OrderType.BUY:
            print(self.buy_orders)
        else:
            print(self.sell_orders)

    def add_order(self, order: Order):
        if order.order_type == OrderType.BUY:
            self.buy_orders.loc[len(self.buy_orders)] = {
                "price": order.price,
                "quantity": order.quantity,
                "timestamp": order.timestamp,
            }
            self.buy_orders = self.buy_orders.sort_values(
                by=["price", "timestamp"], ascending=[False, True]
            )
        else:
            self.sell_orders.loc[len(self.sell_orders)] = {
                "price": order.price,
                "quantity": order.quantity,
                "timestamp": order.timestamp,
            }
            self.sell_orders = self.sell_orders.sort_values(
                by=["price", "timestamp"], ascending=[True, True]
            )

    def match_orders(self):
        # Implement order matching logic here
        pass
