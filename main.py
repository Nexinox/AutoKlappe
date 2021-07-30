import RPi.GPIO as GPIO
import time
import flask
import threading

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def blink(times):
    for i in range(times):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.5)


@app.route('/', methods=['GET'])
def base():
    t = threading.Thread(name="blinkerThread", target=blink, args=(5,))
    t.start()
    return "Flashing"


#if __name__ == '__main__':
    #t = threading.Thread(name="flaskThread", target=app.run, args=('0.0.0.0', 8080))


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


app.run(host="0.0.0.0", port=8080)