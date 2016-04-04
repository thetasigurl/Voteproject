
#this is the voting modual. 
#all local calls to multichain will be done here
#and called from the votepage. simple enough.

from jsonrpc import ServiceProxy

class chaincommands():
	def getNewWallet(rpc):
		client = ServiceProxy(rpc)
		newWallet = client.getnewaddress()
		return newWallet
	def getVotesFromWallet(rpc,addr):
		client = ServiceProxy(rpc)
		transcArray = client.getaddressbalances(addr)
		return transcArray[0]["qty"]
