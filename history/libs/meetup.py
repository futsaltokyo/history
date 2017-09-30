import json
import os
import urllib.parse

import requests

import history.libs.exceptions as exceptions


class Client:

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
            raise exceptions.MeetupAPIException()

    def past_events(self):
        return self.events(event_status='past')

    def events(self, event_status=None):

        url = '/{.group_name}/events'.format(self)

        if event_status:
            params = {
                'status': 'past'
            }
        else:
            params = None

        return self._req(url, params=params)
