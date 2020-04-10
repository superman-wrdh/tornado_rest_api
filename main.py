import logging
import tornado.ioloop
import tornado.web
from lib.rest_handler import RestHandler
from customer_handers import UserLoginHandler


class MainHandler(RestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/v1/user/login", UserLoginHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    logging.info("server start http://127.0.0.1:8888")
    print("server start http://127.0.0.1:8888")
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
