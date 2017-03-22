import Savoir
import json
rpcuser = "jenn"
rpcpass = "password"
rpchost = "192.168.1.102"
rpcport = "9266"
chain = "john"

api = Savoir.Savoir(rpcuser,rpcpass,rpchost,rpcport,chain)
print(json.dumps(api.getinfo(),sort_keys=True,indent=4)) 
#api.getinfo()
