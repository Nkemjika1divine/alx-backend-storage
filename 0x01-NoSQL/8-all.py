#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """a Python function that lists all documents in a collection"""
    return mongo_collection.find()
