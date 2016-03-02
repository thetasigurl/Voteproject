import pyjsonrpc

class Handler(pyjsonrpc.HttpRequestHandler):
	@pyjsonrpc.rpcmethod
	def add(self,a,b):
		return a + b

server = pyjsonrpc.ThreadingHttpServer(
	server_address = ("localhost",8080),
	RequestHandlerClass = Handler
)
server.serve_forever()
