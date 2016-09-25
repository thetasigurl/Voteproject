import Savoir
rpcuser = "jenn"
rpcpass = "password"
rpchost = "localhost"
rpcport = "2776"
chain = "test"

api = Savoir.Savoir(rpcuser,rpcpass,rpchost,rpcport,chain)
print(api.getinfo()) 
