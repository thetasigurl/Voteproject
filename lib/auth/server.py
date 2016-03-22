from flask import Flask
import flask
import db
app = Flask(__name__)
class InvalidUsage(Exception):
    status_code = 400
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
@app.errorhandler(InvalidAPIUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

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
	body = request.json
	if(!body.hash):
		return 
	resp = db.hashed(body.hash)
	return flask.jsonify(**resp)
if __name__ == "__main__":
	app.run()
