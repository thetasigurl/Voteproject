const m = require("mongoose")
var voterModel = m.Schema({
	email:String,
	hash:String,
	hasVoted: {type: Boolean, default: false}
});
var candidateModel = m.Schema({
	name: String,
	wallet:String
});
module.exports = {
	voter: m.model("Voter",voterModel),
	candidate: m.model("Candidate",candidateModel)
}
