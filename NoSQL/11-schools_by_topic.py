#!/usr/bin/env python3
"""
Find Docs in the Collection by match
"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Find Docs
    """
    return [collection for collection in mongo_collection.find(
        {"topics": topic}
        )]
