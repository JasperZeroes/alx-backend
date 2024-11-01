#!/usr/bin/env python3
"""LRU caching system module"""

from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    LRUCache defines a caching system using the LRU (Least Recently Used) algorithm.
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
        If adding the item exceeds the max size of the cache, it removes the least recently used item.
        """
        if key is None or item is None:
            return

        # If the key exists, update the item and its usage
        if key in self.cache_data:
            self.cache_data[key] = item
            # Move this key to the end to mark it as recently used
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is at max capacity, remove the least recently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.usage_order.pop(0)  # Remove the least recently used key
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new item to the cache and update the usage order
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
            # Update the usage order: move the accessed key to the end
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
