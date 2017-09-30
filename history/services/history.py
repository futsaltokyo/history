from pony.orm import db_session

from history.libs.meetup import Client as MeetupClient
from history.models import Event


class Service:

    def __init__(self):
        pass

    @db_session
    def dump(self):
        client = MeetupClient()
        for e in client.past_events():
            Event.from_dict(e)  # create
