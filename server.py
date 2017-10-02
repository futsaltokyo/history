import hug

from history.models import DB
from history.config import db_settings
from history.controllers import health
from history.controllers import history


DB.bind(**db_settings())
DB.generate_mapping(create_tables=False)


@hug.extend_api('/health')
def health_endpoints():
    return [health]


@hug.extend_api('/history')
def history_endpoints():
    return [history]
