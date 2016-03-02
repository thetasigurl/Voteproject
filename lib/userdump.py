from pymongo import MongoClient
def main():
	db = MongoClient("localhost",27017).data
	coll = db.voters
	for u in coll.find():
		print(u)
main()
