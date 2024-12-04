from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def show_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"<h1>Текущее время: {current_time}</h1>"

if __name__ == "__main__":
    app.run(debug=True)
