#! /bin/bash

#Varibles

ip='104.131.131.93' #genisis node IP addess: Digital Ocean instance

user='' #username
pass='' #password is dynamically genorated eachtime you connect to genisis node

rpcp='6304' #RPC port for entire project
netp='6305' #RPC network pork for entire project
cmd=''
cwd=$(pwd)


#Multichain Explorer Dependencies -- for later use by Voteproject.py, results.page

sudo apt-get install sqlite3 libsqlite3-dev
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo pip install --upgrade pip
sudo pip install pycrypto
sudo apt-get install zip unzip


#Multichain Installation

cd ~/Downloads 
wget http://www.multichain.com/download/multichain-1.0-alpha-29.tar.gz #Gets Mchain v.29 from website - In downloads folder
tar -xvzf *.tar.gz #unpack
mkdir -p ~/mchain29 #create Multichain directory -p checks to see if dir is created

mv multichain-1.0-alpha-29 ~/mchain29 #moves extracted mchain29 file to /mchain29 dir - an effort to keep all extracted files together
cd ~/mchain29/multichain-1.0-alpha-29 #To the mchain29 directory
mv multichaind multichain-cli multichain-util ~/mchain29 #moves the important files needed for execution into a more convieniant location
cd ~/mchain29

cmd='multichaind voteproject@'$ip':'$netp #building the command to establish/create/connect to voteproject network
echo $cmd #displays built command for trouble shooting
eval $cmd #executes the built command 

user= grep -e "user" -F ~/.multichain/voteproject/multichain.conf | sed -e 's/rpcuser=//g'
pass= grep -e "pass" -F ~/.multichain/voteproject/multichain.conf | sed -e 's/rpcpassword=//g'

#create config.ini in cwd/lib/client 
#updated information

echo "Multichain installation Complete" 

#Multichain Explorer Installation

cd ~/Downloads #going to Downloads to get the .zip
wget https://github.com/MultiChain/multichain-explorer/archive/master.zip #Gets latest multichain explorer
unzip *.zip #unzip files
mv multichain-explorer master ~/chain29

cd ~/mchain29
cd multichain-explorer
echo "python setup.py install --user"
python setup.py install --user
 
cd ~/.multichain/voteproject/ #navigates to multichain execution instances to get creds
sudo echo "rpcport=" $rpcp >> multichain.conf #This sets the default-rpc-port value to'RPCP' and adds it to multichain.conf

cd cwd
cp -n mchainexp.conf.templete voteproject.conf #creates a new instance of multichain conf file specific to the voteproject blockchain (-n = no clobber.overwrite if)
mv -n voteproject.conf ~/mchain29/multichain-explorer #creates a new explorer conf file and pushes it to multichain explorer dir (-n = no clobber.overwrite if)

echo "Multichain Explorer installation complete"

#Multichain Explorer launch
cd ~/mchain29/multichain-explorer
python -m Mce.abe --config voteproject.conf --commit-bytes 100000 --no-serve #loads all previous transactions

python -m Mce.abe --config voteproject.conf #runs multichain explorer

echo "Multichain Explore launch complete"


#Voteproject start
cd cwd
echo "Voteproject installation complete"
echo "Starting Voteproject"  #...and Profit!
python lib/client/voteproject.py #moves to the lead voteproject directory for use

echo 'Tschüss!'
exit #Tschüss!

#Consider using symlinks for a better implementation:
#cd /usr/local/bin && sudo ln -s <directory> .





