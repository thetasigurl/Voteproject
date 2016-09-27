import Savoir
import json
rpcuser = "jenn"
rpcpass = "password"
rpchost = "52.27.214.233"
rpcport = "2776"
chain = "test"

api = Savoir.Savoir(rpcuser,rpcpass,rpchost,rpcport,chain)
print(json.dumps(api.getinfo(),sort_keys=True,indent=4)) 
