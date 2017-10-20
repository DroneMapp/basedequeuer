from functools import partial
import os.path


class BasePlugin:
    def __init__(self, dequeuer):
        self.dequeuer = dequeuer
        self.config = dequeuer.config
        self.load_requests_methods()

    def load_requests_methods(self):
        dequeuer = self.dequeuer

        self.get = partial(dequeuer.request_methods['get'], headers=dequeuer.requests_headers)
        self.patch = partial(dequeuer.request_methods['patch'], headers=dequeuer.requests_headers)
        self.put = partial(dequeuer.request_methods['put'], headers=dequeuer.requests_headers)
        self.post = partial(dequeuer.request_methods['post'], headers=dequeuer.requests_headers)
        self.delete = partial(dequeuer.request_methods['delete'], headers=dequeuer.requests_headers)

    def get_url(self, path, payload={}):
        base_url = self.config['base_url']
        return os.path.join(base_url, path).format(payload=payload)
