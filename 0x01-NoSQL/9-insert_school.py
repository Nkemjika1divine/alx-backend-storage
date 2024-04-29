#!/usr/bin/env python3
""" function insert_school """


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection using kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
