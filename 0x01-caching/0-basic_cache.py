#!/usr/bin/env python3
"""Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system"""

    # def __init__(self):
    #     """ Initiliaze
    #     """
    #     self.cache_data = {}

    def put(self, key, item):
        """adds new item to cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """retrieves item from cache"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
