"""Copyright (c) 2016 by Federico Cardoso <federico.cardoso@dxmarkets.com>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of copyright holders nor the names of its
   contributors may be used to endorse or promote products derived
   from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
``AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL COPYRIGHT HOLDERS OR CONTRIBUTORS
BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE."""
import requests
import json
from base64 import b64encode
import logging

log = logging.getLogger('Savoir')


class Savoir():
    __id_count = 0

    def __init__(self,
        rpcuser,
        rpcpasswd,
        rpchost,
        rpcport,
        chainname,
        rpc_call=None
    ):
        self.__rpcuser = rpcuser
        self.__rpcpasswd = rpcpasswd
        self.__rpchost = rpchost
        self.__rpcport = rpcport
        self.__chainname = chainname
        self.__auth_header = ' '.join(
            ['Basic', b64encode(':'.join([rpcuser, rpcpasswd]).encode()).decode()]
        )
        self.__headers = {'Host': self.__rpchost,
            'User-Agent': 'Savoir v0.1',
            'Authorization': self.__auth_header,
            'Content-type': 'application/json'
            }
        self.__rpc_call = rpc_call

    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            # Python internal stuff
            raise AttributeError
        if self.__rpc_call is not None:
            name = "%s.%s" % (self.__rpc_call, name)
        return Savoir(self.__rpcuser,
            self.__rpcpasswd,
            self.__rpchost,
            self.__rpcport,
            self.__chainname,
            name)

    def __call__(self, *args):
        Savoir.__id_count += 1
        postdata = {'chain_name': self.__chainname,
            'version': '1.1',
            'params': args,
            'method': self.__rpc_call,
            'id': Savoir.__id_count}
        url = ''.join(['http://', self.__rpchost, ':', self.__rpcport])
        encoded = json.dumps(postdata)
        log.info("Request: %s" % encoded)
        r = requests.post(url, data=encoded, headers=self.__headers)
        if r.status_code == 200:
            log.info("Response: %s" % r.json())
            return r.json()['result']
        else:
            print("Error! Status code: %s" % r.status_code)
            print("Text: %s" % r.text)
            print("Json: %s" % r.json())
            return r.json()
