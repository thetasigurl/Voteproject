#! /bin/bash
git clone https://github.com/bmjames/python-jsonrpc.git
mv python-jsonrpc rpclib
cd rpclib
python setup.py install
cd -
wget http://www.multichain.com/download/multichain-1.0-alpha-18.tar.gz
tar -xvzf *.tar.gz
cd multichain-1.0-alpha-18
mv multichaind multichain-cli multichain-util /usr/local/bin
multichaind test@52.27.214.233:2777 -daemon -rpcuser="jenn" -rpcpassword="password"
echo "Multichain done"
python ../lib/client/voteproject.py
exit