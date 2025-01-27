import pandas as pd
from order import Order, OrderType

type OrderList = list[Order]


class OrderBook:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.buy_orders = pd.DataFrame(columns=["id", "price", "quantity", "timestamp"])
        self.buy_orders.set_index("id")
        self.sell_orders = pd.DataFrame(
            columns=["id", "price", "quantity", "timestamp"]
        )
        self.sell_orders.set_index("id")
        self.quick_buy = []
        self.quick_sell = []

    def show_book(self, order_type: OrderType) -> None:
        if order_type == OrderType.BUY:
            print(self.buy_orders)
        else:
            print(self.sell_orders)

    def check_clear_cache(self) -> None:
        if len(self.quick_buy) > self.cache_size:
            self.clear_cache(OrderType.BUY)
        if len(self.quick_sell) > self.cache_size:
            self.clear_cache(OrderType.SELL)
        return

    def clear_cache(self, order_type: OrderType):
        if order_type == OrderType.BUY:
            self.buy_orders = self.concat_and_sort(
                self.quick_buy, self.buy_orders, order_type
            )
            self.quick_buy = []
        else:
            self.sell_orders = self.concat_and_sort(
                self.quick_sell, self.sell_orders, order_type
            )
            self.quick_sell = []
        return

    def concat_and_sort(
        self, order_list: OrderList, df: pd.DataFrame, order_type: OrderType
    ) -> pd.DataFrame:
        new_rows = list(
            map(
                lambda order: [
                    order.order_id,
                    order.price,
                    order.quantity,
                    order.timestamp,
                ],
                order_list,
            )
        )
        new_df = pd.DataFrame(new_rows, columns=df.columns)
        updated_df = pd.concat([df, new_df], ignore_index=True)
        updated_df = updated_df.sort_values(
            by=["price", "timestamp"], ascending=[order_type == OrderType.SELL, True]
        )
        return updated_df

    def add_order(self, order: Order):
        if order.order_type == OrderType.BUY:
            self.quick_buy.append(order)
        else:
            self.quick_sell.append(order)

        self.check_clear_cache()
        return

    def match_orders(self):
        # It is assumed that the order books remain in sorted condition
        if len(self.buy_orders) == 0 or len(self.sell_orders) == 0:
            print(
                f"Missing order type: {len(self.buy_orders)} buy orders and {len(self.sell_orders)} sell orders on the book."
            )
            return

        if self.buy_orders.iloc[0].at["price"] < self.sell_orders.iloc[0].at["price"]:
            print(
                f"No matching orders - highest bid is {self.buy_orders.iloc[0].at['price']}, lowest ask is {self.sell_orders.iloc[0].at['price']}"
            )
            return

        matchable = True

        while matchable and len(self.buy_orders) > 0 and len(self.sell_orders) > 0:
            matchable = (
                self.buy_orders.iloc[0].at["price"]
                > self.sell_orders.iloc[0].at["price"]
            )
            if not matchable:
                break
            match_buy = self.buy_orders.iloc[0]
            match_sell = self.sell_orders.iloc[0]
            traded_quantity = min(match_buy.at["quantity"], match_sell.at["quantity"])
            self.buy_orders.iloc[0, self.buy_orders.columns.get_loc("quantity")] = (
                match_buy.at["quantity"] - traded_quantity
            )
            self.sell_orders.iloc[0, self.sell_orders.columns.get_loc("quantity")] = (
                match_sell.at["quantity"] - traded_quantity
            )

            if self.sell_orders.iloc[0].at["quantity"] == 0:
                print(f"completed sell order {self.sell_orders.iloc[0].at['id']}")
                self.sell_orders = self.sell_orders[self.sell_orders["quantity"] > 0]
                print("sell book updated to")
                self.show_book(OrderType.SELL)

            if self.buy_orders.iloc[0].at["quantity"] == 0:
                print(f"completed buy order {self.buy_orders.iloc[0].at['id']}")
                self.buy_orders = self.buy_orders[self.buy_orders["quantity"] > 0]
                print("buy book updated to")
                self.show_book(OrderType.BUY)

        return
