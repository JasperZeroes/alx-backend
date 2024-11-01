#!/usr/bin/env python3
"""FIFO caching system module"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    FIFOCache defines a caching system using the FIFO (First-In-First-Out) algorithm.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.order = []  # List to keep track of the insertion order of keys

    def put(self, key, item):
        """
        Add an item in the cache.
        
        Args:
            key: Key for the item.
            item: Item to be added.
        
        If key or item is None, the method does nothing.
        If adding the item exceeds the max size of the cache, it removes the oldest item.
        """
        if key is None or item is None:
            return

        # Add or update the item in the cache
        if key not in self.cache_data:
            self.order.append(key)
        self.cache_data[key] = item

        # Check if we need to discard an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO - discard the first inserted item
            oldest_key = self.order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        
        Args:
            key: Key of the item to retrieve.
        
        Returns:
            The item if it exists in the cache; otherwise, None.
        """
        return self.cache_data.get(key, None)
