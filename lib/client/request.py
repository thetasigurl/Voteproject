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


"""


import httplib
c = httplib.HTTPConnection("ec2-52-32-17-137.us-west-2.compute.amazonaws.com")
c.request("GET", "/list/20")
response = c.getresponse()
print response.status, response.reason
data = response.read()
print data

