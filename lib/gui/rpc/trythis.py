import Savoir
import json
rpcuser = "multichainrpc"
rpcpass = "GmpMy3KKcQZ4yyYews9jahxjpDMLqSCRzwhkAwTthg2X"
rpchost = "192.168.1.102"
rpcport = "4396"
chain = "exodus"

api = Savoir.Savoir(rpcuser,rpcpass,rpchost,rpcport,chain)
print(json.dumps(api.getinfo(),sort_keys=True,indent=4)) 
#api.getinfo()
