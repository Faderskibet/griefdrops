from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    """Simple webpage to be pinged by UptimeRobot."""
    return "The PUBG Bot is running and ready for deployment!"

def run():
    """Starts the Flask server."""
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 8080))

def keep_alive():
    """Runs the Flask server in a separate thread."""
    t = Thread(target=run)
    t.start()
