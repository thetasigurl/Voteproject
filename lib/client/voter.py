
#this is the voting modual. 
#all local calls to multichain will be done here
#and called from the votepage. simple enough.
import json
from jsonrpc import ServiceProxy, JSONRPCException

class chaincommands():
	def __init__(self):
		self.connstr = "http://jenn:password@127.0.0.1:8332"
	
	def getNewWallet(self):
		client = ServiceProxy(self.connstr)
		newWallet = client.getnewaddress()
		return newWallet
	
	def test(self):
		client = ServiceProxy(self.connstr)
		newWallet = client.getinfo()
		return newWallet
	
	def getVotesFromWallet(self,addr): #dont need... just good for testing
		client = ServiceProxy(self.connstr)
		transcArray = client.getaddressbalances(addr)
		return transcArray[0]["qty"]
	
	#takes address within wallet and issues a coin to address. return value is the txid
	#issue more gives coins - issue creates a new "currency" 
	def	issuecoin(self,address,qty):
		try:
			client = ServiceProxy(self.connstr)
			isucoin = client.issuemore(address,"coin",qty)
			print isucoin
			return isucoin
		except JSONRPCException as e:
			print e.error
			return None
	def send(self,giver,reciever,qty):
		client = ServiceProxy(self.connstr)
		res = client.sendassetfrom(giver,reciever,"coin",qty)
		return res
