#!/usr/bin/env python3
"""
Pagination: intro
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range - calculates a start index and an end index
    @page: number of page
    @page_size: size of page
    Return: tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
