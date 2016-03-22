from flask import Flask
import flask
import db
app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello this is Flask Auth!"
@app.route("/list/<inn>")
def ls(inn):
	lss = db.list()
	index = int(inn)
	
	if not index:
		return flask.jsonify(**lss[0])
	else:
		return flask.jsonify(**lss[index])
@app.route("/auth",methods=["GET"])
def auth():
	content = request.json
	#res = db.hashed(hss)
	return flask.jsonify(**content)
if __name__ == "__main__":
	app.run()
