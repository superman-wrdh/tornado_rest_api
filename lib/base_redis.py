import redis


class BaseRedis(object):
    instance = "MAIN"
    key = None

    def __init__(self, *args, **kwargs):
        self._redis_name_map = {
            "MAIN": 0,
            "SLAVE": 1
        }
        self._redis_instance = {}
        super(BaseRedis, self).__init__()

    def _get_instance(self):
        instance = self._redis_instance.get(self.instance)
        if not instance:
            instance = redis.StrictRedis(
                host="",
                db=0,
                port=6379,
                socket_connect_timeout=100,
                socket_timeout=100,
                socket_keepalive=True,
            )
            self._redis_instance = {self.instance: instance}
        return instance

    @property
    def get_redis(self):
        return self._get_instance()

