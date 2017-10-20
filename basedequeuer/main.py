from signal import signal, SIGTERM, SIGHUP, SIGABRT

import click
import yaml

from .basedequeuer import Dequeuer
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


@click.command()
@click.option('--max-messages', default=0)
def main(max_messages):
    with open(settings.CONFIG_FILE_PATH) as config_file:
        cfg = yaml.load(config_file)

    d = Dequeuer(cfg, settings.QUEUE_NAME)
    bind_signals(d)

    try:
        run(d, max_messages)
    except KeyboardInterrupt:
        d.alive = False
