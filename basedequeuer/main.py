from signal import signal, SIGTERM, SIGHUP, SIGABRT

import yaml

from .dequeuer import Dequeuer
from . import settings


def bind_signals(dequeuer):
    def stop_dequeuer(signum, stack_frame):
        dequeuer.alive = False

    for s in SIGABRT, SIGTERM, SIGHUP:
        signal(s, stop_dequeuer)


def run(dequeuer, max_messages):
    counter = 0
    while dequeuer.alive:
        if not dequeuer.alive:
            break

        n = dequeuer.process_messages()
        counter += n

        if max_messages and counter >= max_messages:
            break


def main(max_messages=0, custom_dequeuer=None):
    with open(settings.CONFIG_FILE_PATH) as config_file:
        cfg = yaml.load(config_file)

    try:
        d = custom_dequeuer(cfg, settings.QUEUE_NAME)
    except TypeError:
        d = Dequeuer(cfg, settings.QUEUE_NAME)
    bind_signals(d)

    try:
        run(d, max_messages)
    except KeyboardInterrupt:
        d.alive = False
