#! /bin/bash
ip=''
rpcport=0
oopt=' -daemon'
user=''
password=''
host=''

while getopts "i:p:" OPTION
do
	case $OPTION in
		i)
			echo "IP is $OPTARG"
			ip=$OPTARG
			;;
		p)
			echo "RPC PORT is $OPTARG"
			rpcport=$OPTARG
			;;"
	esac
done

cmd='multichaind '$ip' '$oopt
echo $cmd
eval $cmd
echo "Multichain has started"

python lib/client/voteproject.py
exit

#Consider using symlinks for a better implementation:
#cd /usr/local/bin && sudo ln -s <directory> .
