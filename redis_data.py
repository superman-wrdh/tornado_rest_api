from lib.base_redis import BaseRedis


class TokenRedis(BaseRedis):
    def __init__(self):
        self.instance = "MAIN"
        self.key = "user_token:{}"
        super(TokenRedis, self).__init__()

    def set_token(self, token, user_id):
        key = self.key.format(token)
        _redis = self.get_redis
        _redis.set(key, user_id)
        _redis.expire(key, 3600 * 2)

    def expire_token(self, token):
        key = self.key.format(token)
        self.get_redis.expire(key)

    def get_user_id_by_token(self, token):
        key = self.key.format(token)
        _redis = self.get_redis
        r = _redis.get(key)
        if not r:
            return None
        r = r.decode("utf8")
        return r

    def delete_token(self, token):
        key = self.key.format(token)
        _redis = self.get_redis
        return _redis.delete(key)
