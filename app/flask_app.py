import time
import socket
from flask import Flask
    
app = Flask(__name__)
start = time.time()
		
def elapsed():
    running = time.time() - start
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%0.2d:%0.2d" %(hours, minutes, seconds)

@app.route("/")
def hello():
    return "Hello, This Flask app is running on server: %s (uptime: %s)" %(socket.gethostname(),elapsed())

if __name__ == "__main__":
    app.run(debug=True)
