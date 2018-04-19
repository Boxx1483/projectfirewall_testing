#This script will test our network
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()
#This script will test our network

#imports
import subprocess
import socket
import socketserver

#Global_Constants
ipclass = socket.


def main():
  if ipclass is True:
    menu_inside()

  elif ipclass is False:
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

def testweb_in():
    
def testws_in():

def testfw_out():

def testweb_out():

def testws_out():



main()





