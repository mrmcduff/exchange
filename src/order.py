from dataclasses import dataclass
from enum import Enum
from uuid import uuid4 as uid
from utils import current_millis


class OrderType(Enum):
    BUY = 1
    SELL = 2


@dataclass
class Order:
    order_id: str
    order_type: OrderType
    price: float
    quantity: int
    timestamp: int


def make_order(order_type: OrderType, price: float, quantity: int) -> Order:
    return Order(
        order_id=uid(),
        order_type=order_type,
        price=price,
        quantity=quantity,
        timestamp=current_millis(),
    )
