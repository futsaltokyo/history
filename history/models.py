from datetime import datetime
from decimal import Decimal

import pony.orm

DB = pony.orm.Database()


def timestamp2datetime(ts_ms):
    return datetime.fromtimestamp(ts_ms / 1000)


class BaseModel():

    _TYPE_MAP = {}

    @classmethod
    def from_dict(cls, dct):
        new_dct = {}
        for key, (fn_typecast, key_to_find) in cls._TYPE_MAP.items():
            try:
                if isinstance(key_to_find, list):
                    exp = ''.join(['[{}]'.format(key) for key in key_to_find])
                    val = ('{' + exp + '}').format(dct)
                else:
                    val = dct[key_to_find or key]
                val = fn_typecast(val)
                new_dct[key] = val
            except (KeyError, ValueError):
                continue
        return cls(**new_dct)

    @classmethod
    def from_kwargs(cls, **kwargs):
        return BaseModel.from_dict(kwargs)


class Event(DB.Entity, BaseModel):
    _table_ = 'events'
    id = pony.orm.PrimaryKey(int)
    name = pony.orm.Required(str)
    created = pony.orm.Required(datetime, sql_type='TIMESTAMP')
    started = pony.orm.Required(datetime, sql_type='TIMESTAMP')
    duration = pony.orm.Required(int)
    rsvp_limit = pony.orm.Optional(int)
    fee = pony.orm.Optional(Decimal, precision=10, scale=4, default=0)
    currency = pony.orm.Optional(str, default='JPY')
    venue_id = pony.orm.Optional(int)

    _TYPE_MAP = {
        'id': (int, None),
        'name': (str, None),
        'created': (timestamp2datetime, None),
        'started': (timestamp2datetime, 'time'),
        'duration': (int, None),
        'rsvp_limit': (int, None),
        'fee': (Decimal, ['fee', 'amount']),
        'currency': (str, ['fee', 'currency']),
        'venue_id': (int, ['venue', 'id']),
    }


class Attendee(DB.Entity, BaseModel):
    _table_ = 'attendees'
    event_id = pony.orm.Required(int)
    member_id = pony.orm.Required(int, index=True)
    pony.orm.PrimaryKey(event_id, member_id)


class Member(DB.Entity, BaseModel):
    _table_ = 'members'
    id = pony.orm.PrimaryKey(int)
    name = pony.orm.Required(str)
    image_url = pony.orm.Optional(str)

    _TYPE_MAP = {
        'id': (int, ['member', 'id']),
        'name': (str, ['member', 'name']),
        'image_url': (str, 'thumb_link')
    }
