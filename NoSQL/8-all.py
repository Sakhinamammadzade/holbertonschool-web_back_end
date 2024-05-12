#!/usr/bin/env python3
"""
List Docs int the Collection
"""
import pymongo


def list_all(mongo_collection):
    """
    List Docs
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
