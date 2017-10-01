import json
import os
import urllib.parse

import requests

import history.libs.exceptions as exceptions


class Client:

    REQUIRED_FIELDS_EVENT = {
        'id': int,
        'name': str,
        'created': int,
        'duration': int,
        'time': int,
        'venue.id': int,
        'fee': dict,
        'rsvp_limit': int
    }

    REQUIRED_FIELDS_RSVP = {
        'member': dict
    }

    def __init__(self, api_key=None, group_name=None):
        self.api_key = api_key or os.getenv('MEETUP_API_KEY')
        self.group_name = group_name or os.getenv('MEETUP_GROUP_NAME')
        self.base_url = 'https://api.meetup.com/'

    def _req(self, path, method='get', data=None, params=None):
        req = getattr(requests, method)
        if not data:
            data = {}

        if not params:
            params = {}

        params.update({
            'sign': True,
            'key': self.api_key
        })

        url = urllib.parse.urljoin(self.base_url, path)
        resp = req(url, data=json.dumps(data), params=params)

        if 200 <= resp.status_code < 400:
            return resp.json()
        else:
            raise exceptions.MeetupAPIException(resp.text)

    def past_events(self, required_fields=None):
        return self.events(
            required_fields=required_fields,
            event_status='past'
        )

    def events(self, required_fields=None, event_status=None):

        url = '/{.group_name}/events'.format(self)

        params = {'desc': True}

        if not required_fields:
            required_fields = self.REQUIRED_FIELDS_EVENT.keys()
        params['only'] = ','.join(required_fields)

        if event_status:
            params['status'] = event_status

        return self._req(url, params=params)

    def event_rsvp(self, event_id, required_fields=None):

        url = '/{0.group_name}/events/{1}/rsvps'.format(self, event_id)

        params = {}

        if not required_fields:
            required_fields = self.REQUIRED_FIELDS_RSVP.keys()
        params['only'] = ','.join(required_fields)

        return self._req(url, params=params)
