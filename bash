apt-get update -y
apt-get install python3 -y
apt-get install nmap -y
easy_install pip
apt-get install python3-pip -y
pip3 install --target=/usr/local/lib/python3.5/dist-packages python-nmap
chmod a+x testpython.py
python3 testpython.py

