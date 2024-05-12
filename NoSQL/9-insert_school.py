#!/usr/bin/env python3
"""
Insert Docs int the Collection
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert Docs
    """
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
