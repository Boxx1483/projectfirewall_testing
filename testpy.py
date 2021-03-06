import socket, nmap, os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
# This script will test our network



# Global_Constants
ipclass = ip[0:2]


def main():
    if ipclass == '10':
        menu_inside()

    elif ipclass == '19':
        menu_outside()

    else:
        print('You are not connected correctly')
        exit()


def print_menu():
    print('-' * 25)
    print('1. Test FW')
    print('2. Test Webserver')
    print('3. Test Work Station')
    print('4. To exit program')
    print('-' * 25)
    return

def menu_inside():
    #clearing screen when reloading menu
    print('Inside Menu')
    os.system("clear")

    #calling function that prints the menu
    print_menu()

    #asking for user input menu option
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
    #clearing screen when reloading menu
    os.system("clear")

    #printing the menu options
    print('Outside Menu')
    print_menu()

    #asking for user input menu option
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
    devicename = str(input('Enter IP of Firewall:'))
    nm = nmap.PortScanner()
    nm.scan(devicename, '1-123')
    print(nm.all_hosts())

    for host in nm.all_hosts():
        print('-' * 25)
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('-' * 10)
            print('Protocol : %s' % proto)
            lport = nm[host][proto].keys()
            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    if ping_check(devicename):
        print(devicename, 'Is up')
    else:
        print(devicename, 'Is down')
    input()

def testweb_in():
    hostname = str(input('Enter IP of Webserver:'))
    if ping_check(hostname):
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')
    input()


def testws_in():
    hostname = str(input('Enter IP of Webserver:'))
    if ping_check(hostname):
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')
    input()


def testfw_out():
    devicename = str(input('Enter IP of Firewall:'))
    nm = nmap.PortScanner()
    nm.scan(devicename, '1-512')
    print(nm.all_hosts())

    for host in nm.all_hosts():
        print('-' * 25)
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())
        for proto in nm[host].all_protocols():
            print('-' * 10)
            print('Protocol : %s' % proto)

            lport = nm[host][proto].keys()
            for port in lport:
                print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

    if ping_check(devicename):
        print(devicename, 'Is up')
    else:
        print(devicename, 'Is down')
    input()


def ping_check(host_or_ip):
    response = os.system("ping " + host_or_ip + " -c 1 > /dev/null 2>&1")
    return response == 0


def testweb_out():
    hostname = str(input('Enter IP of Webserver:'))
    if ping_check(hostname):
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')
    input()


def testws_out():
    hostname = str(input('Enter IP of Webserver:'))
    if ping_check(hostname):
        print(hostname, 'Is up')
    else:
        print(hostname, 'Is down')
    input()


main()

