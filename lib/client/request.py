import httplib
import sys
import json

class request():	

#this one does not work for sure. 
	def auth(self,hdata):
		h = {'Content-type': 'application/json', 'Accept': 'text/html'}
		url = "ec2-52-32-17-137.us-west-2.compute.amazonaws.com"
		c = httplib.HTTPConnection(url)
		c.request("POST","/auth",json.dumps(hdata),headers=h)
		response = c.getresponse()
		data = response.read()
		return data
	
	def ping(self,number):
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		url = "ec2-52-32-17-137.us-west-2.compute.amazonaws.com"
		c = httplib.HTTPConnection(url)
		uurl = "/list/"+str(number)
		c.request("GET",uurl)
		response = c.getresponse()
		data = response.read()
		return json.loads(data)
		
		
		
		"""
		if data = true
			return true
		else
			return false (from there you will return to loginpage) 
		"""


"""
This one works for sure! 

	def auther(self,*args):
		c = httplib.HTTPConnection("ec2-52-32-17-137.us-west-2.compute.amazonaws.com")
		c.request("GET", "/list/0")
		response = c.getresponse()
		print response.status, response.reason
		data = response.read()
		print data
"""


"""
#301 error
import httplib
conn = httplib.HTTPConnection("www.twitter.com")
conn.request("GET", "/Tasigurl_")
r1 = conn.getresponse()
print r1.status, r1.reason

#works
import httplib
c = httplib.HTTPSConnection("ccc.de")
c.request("GET", "/en/")
response = c.getresponse()
print response.status, response.reason
data = response.read()
print data

>>> import requests
>>> r = requests.post('http://httpbin.org/post', json={"key": "value"})
>>> r.status_code
200
>>> r.json()
{'args': {},
 'data': '{"key": "value"}',
 'files': {},
 'form': {},
 'headers': {'Accept': '*/*',
             'Accept-Encoding': 'gzip, deflate',
             'Connection': 'close',
             'Content-Length': '16',
             'Content-Type': 'application/json',
             'Host': 'httpbin.org',
             'User-Agent': 'python-requests/2.4.3 CPython/3.4.0',
             'X-Request-Id': 'xx-xx-xx'},
 'json': {'key': 'value'},
 'origin': 'x.x.x.x',
 'url': 'http://httpbin.org/post'}

{

'auth':'<auth string here>'
}



import json
import urllib2

data = {'ids': [12, 3, 4, 5, 6]}

req = urllib2.Request('http://example.com/api/posts/create')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

import json
import requests
data = {'temperature':'24.3'}
data_json = json.dumps(data)
payload = {'json_payload': data_json, 'apikey': 'YOUR_API_KEY_HERE'}
r = requests.get('http://myserver/emoncms2/api/post', data=payload)

"""



