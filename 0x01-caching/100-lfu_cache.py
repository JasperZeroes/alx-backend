#!/usr/bin/env python3
"""LFU caching system module"""

from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """
    LFUCache defines a caching system with LFU (Least Frequently Used) algorithm,
    discarding the least frequently used item, with LRU as a tiebreaker if necessary.
    """

    def __init__(self):
        """Initialize the cache and frequency tracking"""
        super().__init__()
        self.frequency = {}  # Frequency of accesses for each key
        self.usage_order = []  # Access order of keys for LRU tracking within same frequency

    def put(self, key, item):
        """
        Add an item in the cache.
        
        Args:
            key: Key for the item.
            item: Item to be added.
        
        If key or item is None, the method does nothing.
        If adding the item exceeds the max size of the cache, it removes the least frequently used item.
        """
        if key is None or item is None:
            return

        # If key exists, update the item and its frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            # Refresh position in usage order
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # If the cache is at max capacity, discard the LFU (and LRU if necessary)
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key
                min_freq = min(self.frequency.values())
                candidates = [k for k in self.usage_order if self.frequency[k] == min_freq]
                lfu_key = candidates[0]  # The first in usage order is the LRU among the LFU
                self.usage_order.remove(lfu_key)
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key}")

            # Add new item to the cache and set frequency to 1
            self.cache_data[key] = item
            self.frequency[key] = 1
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
            # Increment frequency and refresh usage order
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache_data[key]
        return None
