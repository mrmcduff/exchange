from order_book import OrderBook
from order import Order, OrderType


class Exchange:
    def __init__(self):
        self.order_book = OrderBook()

    def show_books(self):
        print("Buy book")
        self.order_book.show_book(order_type=OrderType.BUY)
        print("Sell book")
        self.order_book.show_book(order_type=OrderType.SELL)

    def place_order(self, order: Order):
        self.order_book.add_order(order)
        self.order_book.match_orders()

    def get_current_price(self):
        # Implement logic to determine current price
        pass
