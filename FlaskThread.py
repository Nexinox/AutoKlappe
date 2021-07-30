import QueueThread
import flask


class FlaskThread(QueueThread):
    host = "0.0.0.0"
    port = 8080
    app: flask.Flask = None

    def __init__(self, app: flask.Flask, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port
        self.app = app

    def run(self) -> None:
        self.app.run(host=self.host, port=self.port)
