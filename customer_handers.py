from uuid import uuid4
import hashlib
from lib.rest_handler import RestHandler
from mysql_data import find_user_by_login_name
from redis_data import TokenRedis


class UserLoginHandler(RestHandler):
    async def get(self):
        data = {}
        self.render_json(data=data)
        return

    async def post(self):
        json_data = self.request_body
        username = json_data.get("username")
        password = json_data.get("password")

        r = find_user_by_login_name(login_name=username)
        if r:
            if r.get("password_hash") == hashlib.md5(password.encode("utf8")).hexdigest():
                token_redis = TokenRedis()
                token = str(uuid4()).replace("-", "")
                token_redis.set_token(token=token, user_id=r.get("id"))
                data = {"token": token}
                self.render_json(data=data, message="登录成功")
                return
            else:
                message = "密码错误"
        else:
            message = "用户不存在"
        self.render_json(code=300, message=message)
        return
