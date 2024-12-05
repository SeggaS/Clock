import os
from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"<h1>Поточний час: {current_time}</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port)        
