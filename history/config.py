import os


def db_settings():
    return {
        'provider': 'postgres',
        'host': os.getenv('DB_HOST', '127.0.0.1'),
        'port': int(os.getenv('DB_PORT', 5432)),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'database': os.getenv('DB_NAME', 'history')
    }


def redis_settings():
    return {
        'host': os.getenv('REDIS_HOST', '127.0.0.1'),
        'port': int(os.getenv('REDIS_PORT', 6379)),
        'user': os.getenv('REDIS_USER'),
        'password': os.getenv('REDIS_PASSWORD')
    }
