#!/usr/bin/env python3
"""script contain FIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """"""

    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                key, value = next(iter(self.cache_data))
                print(f"DISCARD: {key}")
                self.cache_data.pop(key)
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
