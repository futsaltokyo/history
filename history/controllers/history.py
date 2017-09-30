from time import time as timestamp

import hug


@hug.get('/')
def stats():
    return {
        'events': {
            'total': 0
        },
        'members': {
            'total': 0
        },
        'meta': {
            'last_indexed': int(timestamp())
        }
    }
