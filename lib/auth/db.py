from pymongo import MongoClient
def hashed(hsh):
	db = MongoClient("localhost",27017).data
	coll = db.voters
	v = coll.find_one({"hash":hsh})
	return v
def list():
	db = MongoClient("localhost",27017).data
	coll = db.voters
	res = []
	for u in coll.find():
		res.append({
			"fname":u["fname"],
			"lname":u["lname"],
			"hash":u["hash"]
		})
	return res
def test():
	return "From DB Hello"
