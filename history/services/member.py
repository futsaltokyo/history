from pony.orm import db_session, count

from history.models import Member


class Service:

    def __init__(self):
        pass

    @db_session
    def member_by_id(member_id):
        return Member[member_id]

    @db_session
    def total_members(self):
        return count(m for m in Member)
