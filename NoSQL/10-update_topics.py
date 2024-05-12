#!/usr/bin/env python3
"""
Change Docs int the Collection
"""
import pymongo


def update_topics(mongo_collection, name, topics):
    """
    Update Docs
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
