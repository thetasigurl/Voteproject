var express = require("express");
var router = express.Router();
var voter = require("./voterlib.js");
var mids = require("./middlewares.js");
var mc = require("multichain-node")({
	port: process.env.MCPORT,
	host: "localhost",
	user: "multichainrpc",
	pass: process.env.MCPASS
})
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
router.get("/ping",(req,res) => {
	mc.getInfo((err, info) => {
	    if(err) return res.status(500).send(err);
	    return res.status(200).send(info);
	});
});
router.post("/api/chain",mids.nodeQuery,(req,res) => {
	mc.grant({
		addresses: req.query.a,
		permissions: "votecoin.issue"
	},(err,org) => {
		if(err) return res.status(500).send(err);
	    return res.status(200).send(org);
	});
});

module.exports = router;
