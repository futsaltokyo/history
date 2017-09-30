import hug

import history.controllers.health
import history.controllers.history



@hug.extend_api('/health')
def health():
    return [history.controllers.health]


@hug.extend_api('/history')
def history():
    return [history.controllers.history]
