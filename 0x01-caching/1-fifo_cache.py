#!/usr/bin/env python3
"""script contain FIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class using put and get method to retrieve
    and put and item to cache using FIFO algo (in put method)"""

    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
                   key not in self.cache_data:
                keys = [key for key in self.cache_data.keys()]
                print(f"DISCARD: {keys[0]}")
                self.cache_data.pop(keys[0])
            self.cache_data[key] = item

    def get(self, key):
        """get an item by key"""
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
