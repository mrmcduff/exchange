from exchange import Exchange
from order import Order, OrderType, make_order
import time


def main():
    exchange = Exchange(book_cache_size=3)

    # Simulate some orders
    exchange.create_order(OrderType.BUY, 78, 30)
    exchange.create_order(OrderType.BUY, 100.0, 10)
    exchange.create_order(OrderType.BUY, 110.0, 20)
    exchange.create_order(OrderType.BUY, 90.0, 5)

    exchange.create_order(OrderType.SELL, 101.0, 5)
    exchange.create_order(OrderType.SELL, 125.0, 6)
    exchange.create_order(OrderType.SELL, 109.0, 5)
    exchange.create_order(OrderType.SELL, 121.0, 3)

    exchange.create_order(OrderType.BUY, 99.95, 15)
    exchange.show_books()

    print("Trying to match order")
    exchange.execute_orders()

    # # Run the exchange simulation
    # while True:
    #     # Implement main loop logic here
    #     pass


if __name__ == "__main__":
    main()
