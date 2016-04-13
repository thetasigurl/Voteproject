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

		
