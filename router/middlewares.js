const Joi = require("joi");
module.exports = {
	newVoter: (req,res,next) => {
		Joi.validate(req.body,
		{	
			email: Joi.string().required(),
			hash: Joi.string().required()
		},(err, value) =>{ 
			if(err) return res.status(400).send(err);
			next();
		});	
	},
	voterQuery:(req,res,next) => {
		Joi.validate(req.query,
		{
			v: Joi.string().required()
		}, (err,value) => {
			if(err) return res.status(400).send(err);
			next();
		});
	}
}
