grep -e "user" -F ~/.multichain/john/multichain.conf | sed -e 's/rpcuser=//g'

 grep -e "pass" -F ~/.multichain/john/multichain.conf | sed -e 's/rpcpassword=//g'
