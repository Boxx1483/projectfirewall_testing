import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
#This script will test our network

#imports
import subprocess
import socketserver
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
#This script will test our network

#imports
import subprocess
import socketserver
import os

#Global_Constants
ipclass = ip[0:2]
print (ipclass)

def main():
  if ipclass == '10':
    menu_inside()

  elif ipclass == '19':
    menu_outside()

  else:
      print('You are not connected correctly')
      exit()



def menu_inside():
    print('Inside Menu')
    print('-'*25)
    print('1. Test FW')
    print('2. Test Webserver')
    print('3. Test Work Station')
    print('4. To exit program')
    print('-'*25)
    user_inside = str(input('Enter your choice:'))
    if user_inside == '1':
        testfw_in()

    elif user_inside == '2':
        testweb_in()

    elif user_inside == '3':
        testws_in()

    elif user_inside == '4':
        exit()
    else:
        print('kys')
        menu_inside()

def menu_outside():
    print('Outside Menu')
    print('-' * 25)
    print('1. Test FW')
    print('2. Test Webserver')
    print('3. Test Work Station')
    print('4. To exit program')
    print('-' * 25)
    user_inside = str(input('Enter your choice:'))
    if user_inside == '1':
        testfw_out()

    elif user_inside == '2':
        testweb_out()

    elif user_inside == '3':
        testws_out()

    elif user_inside == '4':
        exit()
    else:
        print('kys')
    menu_outside()

def testfw_in():
    hostname = str(input('Enter IP of FW:'))
    respone = os.system("ping -c 1" + hostname)
    if respone == 0:
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')

def testweb_in():
    hostname = str(input('Enter IP of webserver:'))
    respone = os.system("ping -c 1" + hostname)
    if respone == 0:
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')

def testws_in():
    hostname = str(input('Enter IP of Workstation:'))
    respone = os.system("ping -c 1" + hostname)
    if respone == 0:
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')

def testfw_out():
    hostname = str(input('Enter IP of FW'))
    respone = os.system("ping -c 1" + hostname)
    if respone == 0:
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')
def testweb_out():
    hostname = str(input('Enter IP of webserver'))
    respone = os.system("ping -c 1" + hostname)
    if respone == 0:
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')

def testws_out():
    hostname = str(input('Enter IP of webserver'))
    respone = os.system("ping -c 1" + hostname)
    if respone == 0:
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')


main()




#Global_Constants
ipclass = ip[0:2]
print (ipclass)

def main():
  if ipclass == '10':
    menu_inside()

  elif ipclass == '19':
    menu_outside()

  else:
      print('You are not connected correctly')
      exit()



def menu_inside():
    print('Inside Menu')
    print('-'*25)
    print('1. Test FW')
    print('2. Test Webserver')
    print('3. Test Work Station')
    print('4. To exit program')
    print('-'*25)
    user_inside = str(input('Enter your choice:'))
    if user_inside == '1':
        testfw_in()

    elif user_inside == '2':
        testweb_in()

    elif user_inside == '3':
        testws_in()

    elif user_inside == '4':
        exit()
    else:
        print('kys')
        menu_inside()

def menu_outside():
    print('Outside Menu')
    print('-' * 25)
    print('1. Test FW')
    print('2. Test Webserver')
    print('3. Test Work Station')
    print('4. To exit program')
    print('-' * 25)
    user_inside = str(input('Enter your choice:'))
    if user_inside == '1':
        testfw_out()

    elif user_inside == '2':
        testweb_out()

    elif user_inside == '3':
        testws_out()

    elif user_inside == '4':
        exit()
    else:
        print('kys')
    menu_outside()

def testfw_in():
    print('')
    try:
        ping = subprocess.call(["ping", "10.140.66.64","-c","1"])
    except Exception as error:
        print(error)


def testweb_in():
    print('')

def testws_in():
    print('')

def testfw_out():
    try:
        subprocess.call(["ping", "192.168.1.10","-c","1"])
    except Exception as error:
        print(error)

def testweb_out():
    print('')
def testws_out():
    print('')


main()



