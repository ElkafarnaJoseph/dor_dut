import time
import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, world!'


@app.route('/time')
def get_time():
  now = time.gmtime()
  timestring = time.strftime("%Y-%m-%d %H:%M:%S", now)
  return render_template("time.html", timestring=timestring)

@app.route("/random")
def pick_number():
  n = random.randint(1, 10)
  return render_template("random.html", number=n)

@app.route('/student')
def student_name():
  return 'Hello, this was created by student: El-Kafarna Joseph, KND-22'


if __name__ == "__main__":
    app.run()