var models = require("./models.js");

module.exports = {

	voterExists: (h,callback) => {
		models.voter.findOne({hash: h}, (err,record) => {
			if(err) return callback(err);
			if(!record) return callback (null,false);
			return callback (null,true);
		});
	},
	newVoter: (email,hash,callback) => {
		module.exports.voterExists(hash,(err,ex) => {
			if(err) return callback(err);
			if(ex) return callback("USER ALREADY EXISTS");
			var v = new models.voter();
			v.email = email;
			v.hash = hash;
			v.save((err) => {
				if(err) return callback(err);
				return callback(null,hash);
			});
		});
	}
	voterHasVoted:(h,callback) => {
		module.exports.voterExists(h,(err,ex) => {
                        if(err) return callback(err);
                        if(!ex) return callback("USER DOES NOT EXIST");
                	models.voter.findOne({hash:h},(eerr,record) => {
				if(eerr) return callback(eerr);
				record.hasVoted = true;
				record.save((orr) => {
					if(orr) return callback(orr);
					return callback(null,h);
				});
			});
		});
	},
	getVoter:(h,callback) => {
		module.exports.voterExists(h,(err,ex) => {
                        if(err) return callback(err);
                        if(!ex) return callback("USER DOES NOT EXIST");
                        models.voter.findOne({hash:h},(eerr,record) => {
                                if(eerr) return callback(eerr);
                        	return callback(null,record);
			});
                });
	}
}
