
#this is the voting modual. 
#all local calls to multichain will be done here
#and called from the votepage. simple enough.
import json
from jsonrpc import ServiceProxy

class chaincommands():
	def __init__(self):
		self.connstr = "http://jenn:password@127.0.0.1:2776"
	
	def getNewWallet(self):
		client = ServiceProxy(rpc)
		newWallet = client.getnewaddress()
		return newWallet
	
	def test(self):
		client = ServiceProxy(rpc)
		newWallet = client.getinfo()
		return newWallet
	
	def getVotesFromWallet(self,addr): #dont need... just good for testing
		client = ServiceProxy(rpc)
		transcArray = client.getaddressbalances(addr)
		return transcArray[0]["qty"]
	
	#takes address within wallet and issues a coin to address. return value is the txid
	def	issuecoin(self,address,qty):
		client = ServiceProxy(rpc)
		isucoin = client.issue(address,"coin",qty)
		return isucoin

	def send(self,giver,reciever,qty):
		client = ServiceProxy(rpc)
		res = client.sendassetfrom(giver,reciever,"coin",qty)
		return res
