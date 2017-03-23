const http = require("http"),
express = require("express"),
cookieParser = require('cookie-parser'),
bodyParser = require('body-parser'),
morgan = require('morgan'),
envs = require('dotenv').config(),
session = require('express-session'),
Celebrate = require('celebrate');
var mongoose = require("mongoose");
mongoose.connect(process.env.MONGODB,(err) => {
	if(err) throw err;
	console.log("CONNECTION SUCCESS");
});
var app = express();
app.set('port',process.env.PORT || 5000);
app.use(morgan('dev'));
app.use(cookieParser());
app.use(bodyParser.json());
app.use('/',[require('./routes')]);
http.createServer(app).listen(app.get('port'), () => {
	console.log("Server started in port: ", app.get('port'))
});
