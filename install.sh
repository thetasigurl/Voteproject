#! /bin/bash

ip=''
oopt= ' -daemon -rpcuser="jenn" -rpcpassword="password"'
cmd=''
while getopts "i:" OPTION
do
	case $OPTION in
		i)
			echo"IP is $OPTARG"
			ip = $OPTARG
			;;
	esac
done

git clone https://github.com/bmjames/python-jsonrpc.git
mv python-jsonrpc rpclib
cd rpclib
python setup.py install
cd -
wget http://www.multichain.com/download/multichain-1.0-alpha-29.tar.gz
tar -xvzf *.tar.gz
mv multichain-1.0-alpha-29 mchain29
cd mchain29
mv multichaind multichain-cli multichain-util /usr/local/bin
cmd='multichaind '$ip' '$oopt
echo $cmd
eval $cmd
echo "Multichain done"
python ../lib/client/voteproject.py
exit

#Consider using symlinks for a better implementation:
#cd /usr/local/bin && sudo ln -s <directory> .
