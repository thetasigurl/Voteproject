import sys
import csv
import json
import hashlib
from pymongo import MongoClient
"""
Element 0 is First Name
Element 1 is Last Name
Element 2 is email
"""
def main():
	print(sys.argv)
	db = MongoClient("localhost",27017).data
	collection = db.users
	voterCollection = db["voters"]
	if(len(sys.argv) < 2):
		raise Exception("Not enoug args")
	else:
		f = open(sys.argv[1],"r")
		try:
			read = csv.reader(f)
			for r in read:
				sh = hashlib.sha256()
				sh.update(r[0])
				sh.update(r[1])
				sh.update(r[2])
				rec = {
					"fname":r[0],
					"lname":r[1],
					"email":r[2],
					"hash":sh.hexdigest()
				}
				collection.insert_one(rec)
		finally:
			f.close()
main()
	
