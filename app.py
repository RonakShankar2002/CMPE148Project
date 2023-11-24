from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(_name_)
socketio = SocketIO(app, cors_allowed_origins=“*”)


@socketio.on(“message”)
def sendMessage(message):
	send(message, broadcast=True)
	# send() function will emit a message event by default


@app.route(“/”)
def message():
  return render_template(“message.html”)


if _name_ == “_main_”:
  app.run(debug=True)
