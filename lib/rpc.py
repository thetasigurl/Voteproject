from jsonrpc import ServiceProxy

client = ServiceProxy("http://jenn:password@127.0.0.1:2776")
print client.getaddresses()
