const fs = require("fs")
let main = ()=>{ 
if(!env(".env")) throw new Exception("NO ENVIRONMENT VAR")
const http = require("http"),
express = require("express"),
cookieParser = require('cookie-parser'),
bodyParser = require('body-parser'),
morgan = require('morgan'),
//envs = require('dotenv').config(),
session = require('express-session'),
Celebrate = require('celebrate');
var mongoose = require("mongoose");
console.log(process.env.MONGODB)
mongoose.connect(process.env.MONGODB,(err) => {
	if(err) throw err;
	console.log("CONNECTION SUCCESS");
});
var app = express();
app.set('port',process.env.PORT || 5000);
app.use(morgan('dev'));
app.use(cookieParser());
app.use(bodyParser.json());
app.use('/',[require('./routes.js')]);
http.createServer(app).listen(app.get('port'), () => {
	console.log("Server started in port: ", app.get('port'))
});
}

let env = (filepath) => {
	try {
        var data        = fs.readFileSync(filepath);
        var content     = data.toString().trim();
        var lines       = content.split('\n');

        for (var i=0; i<lines.length; i++) {
          var key_value_array = lines[i].split("=");
          var key             = key_value_array[0].trim();
          var value           = key_value_array[1].trim();
          process.env[key]    = value;
        }
      } catch (e) {
	throw e;
	return false;
      }
      return true;
}
main();
