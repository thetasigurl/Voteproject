
#this is the voting modual. 
#all local calls to multichain will be done here
#and called from the votepage. simple enough.

from jsonrpc.proxy import JSONRPCProxy

class chaincommands():
	connstr = "http://jenn:password@127.0.0.1:2776"
	def getNewWallet(self):
		client = JSONRPCProxy.from_url(connstr)
		newWallet = client.getnewaddress()
		return newWallet
	
	def test(self):
		client = JSONRPCProxy.from_url("http://127.0.0.1:2776")
		newWallet = client.getinfo()
		return newWallet
	
	def getVotesFromWallet(self,addr): #dont need good for testing
		client = JSONRPCProxy.from_url(connstr)
		transcArray = client.getaddressbalances(addr)
		return transcArray[0]["qty"]
	
	#takes address within wallet and issues a coin to address. return value is the txid
	def	issuecoin(self,address,qty):
		client = JSONRPCProxy.from_url(connstr)
		isucoin = client.issue(address,"coin",qty)
		return isucoin

	def send(self,giver,reciever,qty):
		client = JSONRPCProxy.from_url(connstr)
		res = client.sendassetfrom(giver,reciever,"coin",qty)
		return res

"""
test@172.31.21.118:2777 -daemon

import argparse
import chain
parser = argparse.ArgumentParser()
connstr = "http://jenn:password@127.0.0.1:2776"
su (enter root password)

cd /tmp
wget http://www.multichain.com/download/multichain-1.0-alpha-19.tar.gz
tar -xvzf multichain-1.0-alpha-19.tar.gz
cd multichain-1.0-alpha-19
mv multichaind multichain-cli multichain-util /usr/local/bin (to make easily accessible on the command line)

exit (to return to your regular user)

genisis node: 
 test@172.31.21.118:2777

to use in command line: mv multichaind multichain-cli multichain-util /usr/local/bin
"""
