from time import time as timestamp

import hug

from history.services.history import Service as HistoryService
from history.services.event import Service as EventService
from history.services.member import Service as MemberService


@hug.get('/stats')
@hug.cli()
def stats():
    return {
        'events': {
            'total': EventService().total_events()
        },
        'members': {
            'total': MemberService().total_members()
        },
        'meta': {
            'last_indexed': int(timestamp())
        }
    }


@hug.get('/export')
@hug.cli()
def export():
    try:
        HistoryService().dump()
    except Exception as e:
        return {'status': 'error', 'message': e}
    else:
        return {'status': 'ok'}
