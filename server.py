import hug

from history.models import DB
from history.controllers import health
from history.controllers import history

DB.bind(provider='postgres', database='history')
DB.generate_mapping(create_tables=False)


@hug.extend_api('/health')
def health_endpoints():
    return [health]


@hug.extend_api('/history')
def history_endpoints():
    return [history]


if __name__ == '__main__':
    history.stats.interface.cli()
