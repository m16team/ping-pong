import web
import signal

counter = 0
urls = (
    '/', 'index',
    '/get/counter', 'get_counter',
    '/set/counter', 'set_counter'
)


def handler_stop_signals(signum, frame):
    print("Get interrupt signal, let's exit")
    raise KeyboardInterrupt


class index:

    def GET(self):
        global counter
        counter = counter + 1
        return "<h1 style='color:blue'>Hello There!</h1><h2  style='color:red'>Counter: " + str(counter) + "</h2>"

class set_counter:

    def GET(self):
        global counter
        counter = counter + 1
        return str(counter)


class get_counter:

    def GET(self):
        return str(counter)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)
    app = web.application(urls, globals())
    app.run()

# from flask import Flask
# app = Flask(__name__)
#
# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"
#
# if __name__ == "__main__":
#     app.run(host='0.0.0.0')