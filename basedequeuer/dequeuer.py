import json
import os

from cached_property import cached_property

from powerlibs.aws.sqs.dequeue_to_api import DequeueToAPI

from . import settings


class Dequeuer(DequeueToAPI):
    def __init__(self, cfg, queue_name, cherry_pick=False):
        self.token = settings.TOKEN
        self.cherry_pick = cherry_pick

        super().__init__(
            cfg,
            queue_name,
            thread_pool_size=settings.THREAD_POOL_SIZE,
            aws_region=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
        )

    def notify(self, topic, payload, queue=None):
        queue = queue or self.queue

        attributes = {
            'topic': {
                'StringValue': topic,
                'DataType': 'String',
            }
        }
        encoded_payload = json.dumps(payload)

        queue.send_message(
            MessageAttributes=attributes,
            MessageBody=encoded_payload
        )

    @cached_property
    def requests_headers(self):
        return {
            'Authorization': 'token {}'.format(self.token)
        }

    def receive_messages(self):
        max_num_of_messages = int(os.environ.get('SQS_RECEIVE_MESSAGES', 1))
        return super().receive_messages(max_num_of_messages)

    def do_handle_message(self, message, topic, payload):
        if self.cherry_pick:
            d = input('delete? ')
            if d in ('s', 'y', 'd', 'x'):
                message.delete()
                return

        super().do_handle_message(message, topic, payload)
