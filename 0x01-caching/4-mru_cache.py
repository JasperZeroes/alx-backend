#!/usr/bin/env python3
"""MRU caching system module"""

from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """
    MRUCache defines a caching system using the MRU (Most Recently Used) algorithm.
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.usage_order = []  # List to keep track of access order of keys

    def put(self, key, item):
        """
        Add an item in the cache.
        
        Args:
            key: Key for the item.
            item: Item to be added.
        
        If key or item is None, the method does nothing.
        If adding the item exceeds the max size of the cache, it removes the most recently used item.
        """
        if key is None or item is None:
            return

        # If the key exists, update the item and mark it as most recently used
        if key in self.cache_data:
            self.cache_data[key] = item
            # Update usage by removing and re-adding to end of usage_order
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is at max capacity, discard the most recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop()  # Remove the most recently used key
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

            # Add the new item to the cache and mark as most recently used
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Retrieve an item by key from the cache.
        
        Args:
            key: Key of the item to retrieve.
        
        Returns:
            The item if it exists in the cache; otherwise, None.
        """
        if key in self.cache_data:
            # Update the usage order to mark this key as most recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
