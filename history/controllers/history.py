from time import time as timestamp

import hug

from history.services.history import Service as HistoryService
from history.services.event import Service as EventService


@hug.get('/')
def stats():
    return {
        'events': {
            'total': EventService().total_events()
        },
        'members': {
            'total': 0
        },
        'meta': {
            'last_indexed': int(timestamp())
        }
    }


@hug.get('/latest')
def latest():

    HistoryService().dump()

    return {'status': 'ok'}
