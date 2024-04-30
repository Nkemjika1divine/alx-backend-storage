#!/usr/bin/env python3
"""get_page function"""

import requests
import redis

client = redis.Redis()


def get_page(url: str) -> str:
    """This script obtains the HTML content of a URL and returns it."""
    result = requests.get(url).text
    if not client.get("count:{}".format(url)):
        client.set("count:{}".format(url), 1)
        client.setex("result:{}".format(url), 10, result)
    else:
        client.incr("count:{}".format(url), 1)
    return result
