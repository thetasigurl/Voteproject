import pyjsonrpc

client = pyjsonrpc.HttpClient(
	url="http://localhost:2776",
	username="jenn",
	password="password"
);
print client.call("getadddresses");
