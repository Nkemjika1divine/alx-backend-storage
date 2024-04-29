#!/usr/bin/env python3
""" function update_topics """


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document using name"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
