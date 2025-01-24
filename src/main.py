from exchange import Exchange
from order import Order, OrderType, make_order
import time


def main():
    exchange = Exchange()

    # Simulate some orders
    exchange.place_order(Order("1", OrderType.BUY, 100.0, 10, time.time()))
    exchange.place_order(Order("2", OrderType.BUY, 110.0, 20, time.time()))
    exchange.place_order(Order("3", OrderType.BUY, 90.0, 5, time.time()))

    exchange.place_order(Order("2", OrderType.SELL, 101.0, 5, time.time()))
    exchange.place_order(make_order(OrderType.BUY, 99.95, 15, time.time()))
    exchange.show_books()

    # # Run the exchange simulation
    # while True:
    #     # Implement main loop logic here
    #     pass


if __name__ == "__main__":
    main()
