from jsonrpc import ServiceProxy
def getNewWallet(rpc):
	client = ServiceProxy(rpc)
	newWallet = client.getnewaddress()
	return newWallet
def getVotesFromWallet(rpc,addr):
	client = ServiceProxy(rpc)
	transcArray = client.getaddressbalances(addr)
	return transcArray[0]["qty"]