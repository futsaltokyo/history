import os

import hug

from history.models import DB
from history.controllers import health
from history.controllers import history


def db_settings():
    return {
        'provider': 'postgres',
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': int(os.getenv('DB_PORT', 5432)),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME', 'history')
    }


DB.bind(**db_settings())
DB.generate_mapping(create_tables=False)


@hug.extend_api('/health')
def health_endpoints():
    return [health]


@hug.extend_api('/history')
def history_endpoints():
    return [history]
