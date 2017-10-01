import hug


@hug.get('/')
@hug.cli()
def check():
    return {
        'status': 'ok'
    }
