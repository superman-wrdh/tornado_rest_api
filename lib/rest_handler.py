import json
import traceback
import tornado


class RestHandler(tornado.web.RequestHandler):

    def initialize(self):
        super(RestHandler, self).initialize()

    def set_default_headers(self):
        # 允许跨域
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        # self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Methods', 'POST,GET,DELETE,PUT,OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'authorization, Authorization, Content-Type, Access-Control-Allow-Origin, Access-Control-Allow-Headers, X-Requested-By, Access-Control-Allow-Methods')

    def options(self):
        # 允许跨域
        self.set_status(204)
        self.finish()

    @property
    def request_body(self):
        try:
            json_body = json.loads(self.request.body)
            return json_body
        except Exception as e:
            return {}

    def render_json(self, data=None, code=200, message=''):
        result = {
            'data': data if data else {},
            'code': code,
            'message': message
        }
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(result, ensure_ascii=False))
        return

    def write_error(self, status_code, **kwargs):

        self.set_header('Content-Type', 'application/json')
        if self.settings.get("serve_traceback") and "exc_info" in kwargs:
            # in debug mode, try to send a traceback
            lines = []
            for line in traceback.format_exception(*kwargs["exc_info"]):
                lines.append(line)
            self.finish(json.dumps({
                'error': {
                    'code': status_code,
                    'message': self._reason,
                    'traceback': lines,
                }
            }))
        else:
            self.finish(json.dumps({
                'error': {
                    'code': status_code,
                    'message': self._reason,
                }
            }))


