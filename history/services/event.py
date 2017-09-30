from pony.orm import db_session, count

from history.models import Event


class Service:

    def __init__(self):
        pass

    @db_session
    def event_by_id(event_id):
        return Event[event_id]

    @db_session
    def total_events(self):
        return count(e for e in Event)
