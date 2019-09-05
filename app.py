from flask import Flask
from redis import Redis, RedisError
import os
import socket


# Connect to Redis
redis=Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")

def hello():
    try:
    # Increment counter on web page access / refresh
        visits = redis.incr("counter")
    except RedisError:
    # If redis database is not connected below message will appear on the web page    
        visits = "<i>Can not connect to Redis, counter disabled</i>"


    html = "<body bgcolor={bg_color}>" \
           "<h3> {name} ! </h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}" \
           "</body>"

    # Environment properties
    # bg_color -> Background color of webpage
    # name -> User defined text that will come on the web page
    
    # "hostname" extracted from system where application runs
    # "visits" keeps track of counter to display number of times page is accessed
    return html.format(bg_color=os.getenv("BGCOLOR","Green"),name=os.getenv("NAME","Hello Docker world"), hostname=socket.gethostname(),visits=visits)

# "port" on which application can be accessed. Make sure on local machine this port 9000 is available
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
