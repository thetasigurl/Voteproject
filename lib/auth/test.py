import db

def main():
	r = db.hashed("01b8e80ed0d7172d6728339f5e634226ed12ebfb60b0e7bfb309541cddf4906b")
	print(r)
	print(type(r))
	d = {
		"lname": r["lname"],
		"hash": r["hash"]
	}
	print(d)
	print(type(d))
main()
