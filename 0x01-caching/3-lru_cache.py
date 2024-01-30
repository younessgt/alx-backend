#!/usr/bin/env python3
"""script contain LRUCache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ class using put and get method to retrieve
    and put and item to cache using LRU algo (in put method)"""
    list_least_most = []

    def __init__(self):
        """ constructor method"""
        super().__init__()

    def put(self, key, item):
        """add an item to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS and \
               key not in self.cache_data:
                # lru_key is the least recently used key
                lru_key = self.list_least_most.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item
            self.update_cache_order(key)

    def get(self, key):
        """get an item from the cache by key"""

        if key in self.cache_data:
            self.update_cache_order(key)
            return self.cache_data[key]

    def update_cache_order(self, key):
        """ update the access order of items in the cache"""
        if key in self.list_least_most:
            self.list_least_most.remove(key)
        self.list_least_most.append(key)
