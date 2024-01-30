#!/usr/bin/env python3
"""script contain BasicCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """"""

    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
