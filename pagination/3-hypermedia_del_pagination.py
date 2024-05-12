#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returning dict
        """
        dataset_len = len(self.dataset())
        assert 0 <= index < dataset_len

        indexed_dataset = self.indexed_dataset()
        page_dict = {}

        i = index
        while (len(page_dict) < page_size and i < dataset_len):
            if i in indexed_dataset:
                page_dict[i] = indexed_dataset[i]
            i += 1

        page = list(page_dict.values())
        vals = len(page)
        keys = page_dict.keys()

        return {
                'index': index,
                'next_index': max(keys) + 1,
                'page_size': vals,
                'data': page
        }
