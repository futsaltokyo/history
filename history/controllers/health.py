import hug


@hug.get('/')
def check():
    return {
        'status': 'ok'
    }
