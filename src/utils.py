import numpy as np


def current_millis() -> int:
    return np.datetime64("now", "ms").view("int64")
