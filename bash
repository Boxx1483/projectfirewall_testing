apt-get update -y
apt-get install python3 -y
apt-get install nmap -y
apt-get install git -y
easy_install pip
sudo apt-get install python3-pip -y
pip3 install --target=/usr/local/lib/python3.5/dist-packages python-nmap
git clone https://github.com/Boxx1483/projectfirewall_testing.git
cd projectfirewall_testing
chmod a+x testpython.py
python3 testpython.py

