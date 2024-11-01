#!/usr/bin/env python3
"""LIFO caching system module"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache defines a caching system using the LIFO (Last-In-First-Out) algorithm.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.last_key = None  # Keep track of the last inserted key

    def put(self, key, item):
        """
        Add an item in the cache.
        
        Args:
            key: Key for the item.
            item: Item to be added.
        
        If key or item is None, the method does nothing.
        If adding the item exceeds the max size of the cache, it removes the last item added.
        """
        if key is None or item is None:
            return

        # Add or update the item in the cache
        self.cache_data[key] = item
        if key in self.cache_data:
            self.last_key = key

        # Check if we need to discard an item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            if self.last_key:
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")

            # Update the last key after discarding
            self.last_key = key

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        
        Args:
            key: Key of the item to retrieve.
        
        Returns:
            The item if it exists in the cache; otherwise, None.
        """
        return self.cache_data.get(key, None)
