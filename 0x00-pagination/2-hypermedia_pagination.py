#!/usr/bin/env python3
""" script that contain index_range function """
from typing import Dict, Tuple, Any
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ function should return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes to return in a
    list for those particular pagination parameters."""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """ function that disaplay the content based
        on the page and the page_size"""

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        list_dataset = self.dataset()

        rows = list_dataset[indexes[0]: indexes[1]]
        return rows

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """ returning a dictionary of pagination data"""
        new_dict: Dict[Any, Any] = {}
        data_list = self.get_page(page, page_size)

        new_dict['page_size'] = len(data_list)
        new_dict['page'] = page
        new_dict['data'] = data_list
        new_dict['total_pages'] = math.ceil(len(self.dataset()) / page_size)

        if len(data_list) == 0:
            new_dict['next_page'] = None
        else:
            new_dict['next_page'] = page + 1

        if (page == 1):
            new_dict['prev_page'] = None
        else:
            new_dict['prev_page'] = page - 1

        new_dict['total_pages'] = math.ceil(len(self.dataset()) / page_size)
        return new_dict
