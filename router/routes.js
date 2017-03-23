var express = requre("express");
var router = express.Router();
var voter = require("./voterlib.js");
var mids = require("./middlewares.js");
router.get("/",(req,res)=> {
	res.status(200).send("ROUTER IS LIVE");
});
router.post("/api/voter",mids.newVoter,(req,res) => {
	voter.newVoter(req.body.email,req.body.hash, (err,org) => {
		if(err) return res.status(500).send(err);
		if(!org) return res.status(403).send();
		res.status(200).send(org);
	});
});
router.put("/api/voter",mids.voterQuery,(req,res) => {
	voter.voterHasVoted(req.query.v,(err,org) => {
		if(err) return res.status(500).send(err);
		if(!org) return res.status(403).send();
		res.status(200).send(org);
	});
});
router.get("/api/voter",mids.voterQuery,(req,res) => {
        voter.getVoter(req.query.v,(err,org) => {
                if(err) return res.status(500).send(err);
                if(!org) return res.status(403).send();
                res.status(200).send(org);
        });
});

module.exports = router;
