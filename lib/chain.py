from jsonrpc import ServiceProxy
#client = ServiceProxy("http://jenn:password@127.0.0.1:2776")
def getNewWallet():
	client = ServiceProxy("http://jenn:password@127.0.0.1:2776")
	newWallet = client.getNewAddress()
	return newWallet
