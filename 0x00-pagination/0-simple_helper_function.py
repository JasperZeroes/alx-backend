#!/usr/bin/env python3
"""Simple helper function"""


def index_range(page: int, page_size: int):
    """Generate list index range based on pagination params"""
    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size
    return (startIndex, endIndex)
