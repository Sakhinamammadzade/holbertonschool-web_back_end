#!/usr/bin/env python3
"""
Pagination: Simple Task
"""
from typing import Tuple, List
import csv
import math

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Getting page
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        indexes = index_range(page, page_size)
        s, e = indexes[0], indexes[1]

        try:
            return self.dataset()[s:e]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returning dictionary with info about page
        """
        data = self.get_page(page=page, page_size=page_size)
        total_len = len(self.dataset())
        total_pages = math.ceil(total_len / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
            }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    index_range - calculates a start index and an end index
    @page: number of page
    @page_size: size of page
    Return: tuple of size two containing a start index and an end index
    """
    return ((page - 1) * page_size, page * page_size)
