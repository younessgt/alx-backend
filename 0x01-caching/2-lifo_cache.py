#!/usr/bin/env python3
"""script contain LIFOCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ class using put and get method to retrieve
    and put and item to cache using LIFO algo (in put method)"""
    list_add = []

    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
               key not in self.cache_data:
                print(f"DISCARD: {self.list_add[0]}")
                self.cache_data.pop(self.list_add[0])
            self.cache_data[key] = item
            self.list_add.clear()
            self.list_add.append(key)

    def get(self, key):
        """get an item by key"""
        if key is None or (key not in self.cache_data):
            return None
        return self.cache_data[key]
