import hug

import history.controllers.health as health_ctrl
import history.controllers.history as history_ctrl


@hug.extend_api('/health')
def health():
    return [health_ctrl]


@hug.extend_api('/history')
def history():
    return [history_ctrl]
