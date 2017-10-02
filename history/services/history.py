import time
from pony.orm import db_session

from history.libs.meetup import Client as MeetupClient
from history.models import Event, Attendee, Member


class Service:

    def __init__(self):
        pass

    @db_session
    def dump(self):
        client = MeetupClient()
        for event_dict in client.past_events():
            event = Event.from_dict(event_dict)
            time.sleep(MeetupClient.THROTTLE_WAIT_TIME_SEC)
            for rsvp_dict in client.event_rsvp(event.id):
                member_id = rsvp_dict['member']['id']
                if not Member.exists(id=member_id):
                    Member.from_dict(rsvp_dict)
                Attendee(event_id=event.id, member_id=member_id)
