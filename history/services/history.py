import time

from pony.orm import db_session
from redis import Redis
from rq import Queue

from history.libs.meetup import Client as MeetupClient
from history.models import Event, Attendee, Member, DB
from history.config import db_settings, redis_settings


class Service:

    def __init__(self):
        pass

    def queue_dump(self):
        rds = Redis(**redis_settings())
        q = Queue(connection=rds)
        q.enqueue(self.dump, MeetupClient(), db_settings())

    @db_session
    def dump(self, client, db_config):
        DB.bind(**db_config)
        DB.generate_mapping()
        for event_dict in client.past_events():
            event = Event.from_dict(event_dict)
            time.sleep(MeetupClient.THROTTLE_WAIT_TIME_SEC)
            for rsvp_dict in client.event_rsvp(event.id):
                member_id = rsvp_dict['member']['id']
                if not Member.exists(id=member_id):
                    Member.from_dict(rsvp_dict)
                Attendee(event_id=event.id, member_id=member_id)
