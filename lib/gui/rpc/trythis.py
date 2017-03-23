import json
import Savoir
rpcuser = "multichainrpc"
rpcpass = "CWssZg4tGBdeeCKgEJW6Z2dw9RBrQMnKWV4yuWjtVSrj"
rpchost = "localhost"
rpcport = "9266"
chain = "john"

api = Savoir.Savoir(rpcuser,rpcpass,rpchost,rpcport,chain)
print(json.dumps(api.getinfo(),sort_keys=True,indent=4)) 
#api.getinfo()
