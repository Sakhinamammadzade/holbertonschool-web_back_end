#!/usr/bin/env python3
"""complex types- function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """complex multiple"""
    def anonim(x: float) -> float:
        """idk"""
        return x * multiplier

    return anonim
