#hasher modual for client
import sys
import hashlib

class hasher():	

	def hash(self,argv):	
		
		print "arg1:", argv[0]
		print "arg2:", argv[1]
		print "arg3:", argv[2] 
		
		#hashing the argv	
		sh = hashlib.sha256()
		sh.update(argv[0])
		sh.update(argv[1])
		sh.update(argv[2])
		hc = sh.hexdigest() #this is the full final has...stored
		print ('final hash value:' + hc)
		 
		#this is the collected_hash varrible. This is what will be passed. 
		return hc #should this be argv or hc
		
		#print('This is the user collection hash : ' + hc)
		
"""
This is for testing 

def hasher(argv):
		hsr = Hasher() #calls class Hasher
		
		print('pasted class Hasher')
		r = hsr.hash(argv)
		print r
		#print('This is the user collection hash: ' + hsr.hash(argv))
		
		


if __name__ == "__main__":
	
	fname = raw_input('Please enter your First Name: ')
	fname = fname.replace(' ', '') #replaces all white space with no space
	fname = fname.lower()
	fname = fname.title()
   
	lname = raw_input('Please enter your Last Name: ')
	lname = lname.replace(' ', '') #replaces all white space with no space
	lname = lname.lower()#lowers all letters
	lname = lname.title()#capitalizes the first letter
	
	email = raw_input('Please enter your SHSU Email: ')
	email = email.replace(' ', '') #replaces all white space with no space
	email = email.lower()
	email = email.title()
	
	argv = (fname,lname,email)
	hasher(argv)
	

future works
	def deleteinfo(self,fname)
		#data = (infopassed)
		#deletes info when passed though
		#data = none
		#del data
		#reset_selective data
		return data


class Showhash():			
	def showhash(self,argv,hc):
		print "arg1:", argv[0]
		print "arg2:", argv[1]
		print "arg3:", argv[2] 
		print('This is the user collection hash:' + hc) 

	'''
	 def delspace(self,argv):
        #Delete spaces
        argv[0] = argv[0].replace(' ', '')
        argv[1] = argv[1].replace(' ', '')
        argv[2] = argv[2].replace(' ', '')
        return argv
	
	def lowercase(self,argv)
		#lowercase entire string
		argv[0] = argv[0].lower
		argv[1] = argv[0].lower
		argv[2] = argv[0].lower
		return argv
		
	 def capitalize(self):
        #Make first char capital (if letter); make other letters lower
        argv[0] = argv[0].capitalize()
        argv[1] = argv[1].capitalize()
        argv[2] = argv[2].capitalize()
        return argv
       ''' 


def hash
	if(len(sys.argv) < 2):
		raise Exception("Not enoug args")
	else:
		f = open(sys.argv[1],"r")
		try:
			read = csv.reader(f) #dont need to do this
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
"""			
			
