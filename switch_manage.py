from netmiko import ConnectHandler
import os
import subprocess
import datetime

b=False

while b==False:
    ip = input("Enter the IP to connect to: ")
    a=subprocess.getstatusoutput('ping '+ip)

    if a[0]==0:
        print('Host is Up.......')
        print("Establishing Connection.....")
        b=True
    else:
        print('Host down....')
        b=False

user = input("Username: ")
passw = input("Password: ")

device = ConnectHandler(device_type='cisco_ios', ip=ip, username=user, password=passw)
print(device)
choice=""

while choice != '4':
    print('''
1. Get interfaces           6.Config Trunk
2. Backup Config            7.Add Vlan
3. Config access port       
4. Exit                     
5. Change hostname          
''')
    choice = input("Enter your selection: ")

    def getinterfaces():
        global device
        output = device.send_command('sh ip int brief')
        print(output)

# function to backup configuration with device hostname and timestamp

    def backupconf():
        global device
        a=datetime.datetime.now()
        a=a.strftime('%Y%m%d%H%M')
        b=device.send_command('sh run | i hostname')
        b=b.split(" ")
        c=b[1]
        output = device.send_command('sh run')
        fopen = open('C:\\users\\lon\\documents\\'+c+a+'.txt', 'w+')
        fopen.write(output)
        fopen.close()

# function to create access port on provided port

    def switchintconf(inter):
        global device
        output=device.send_config_set("int "+inter)
        print(output)
        commands=['int '+inter,"switchport mode access",'switchport access vlan 10','switchport voice vlan 200','spanning-tree portfast','spanning-tree bpduguard enable','switchport port-security','switchport port-security mac-address sticky','switchport port-security maximum 2', 'no shut']
        output=device.send_config_set(commands)
        print(output)

# function to change hostname and return change

    def hostchang():
        global device
        hname=input('Enter the name of your device: ')
        nresult=device.send_config_set('hostname '+hname)
        '''b = device.send_command_expect('sh run | i hostname')
        b = b.split(" ")
        c = b[1]
        print('Your new hostname is: '+c)'''

# function to make trunk port on provided interface

    def switchtrunk():
        global device
        intf=input('Enter interface to configure as trunk: ')
        device.send_config_set('int '+intf)
        commands=['switchport mode trunk','switchport trunk encap dot1q','switchport trunk allow vlan all','spanning-tree portfast','switchport noneg']
        device.send_config_set(commands)
        output=device.send_command('sh run int '+intf)
        print('Your new interface configuration')
        print(output)

# function to create a new VLAN

    def vlanadd():
        global device
        num=input("Enter VLAN number: ")
        nam=input("Enter VLAN name: ")
        commands=['vlan '+num,'name '+nam,"no shutdown",'exit']
        device.send_config_set(commands)
        output=device.send_command('sh vlan')
        print(output)

# loop to determine which function to run from selection provided

    if choice == '1':
        getinterfaces()
    elif choice == '2':
        backupconf()
    elif choice == '3':
        inter=input("Enter interface to configure as Access port: ")
        switchintconf(inter)
    elif choice == '4':
        print("GOODBYE")
        device.disconnect()
    elif choice == '5':
        hostchang()
    elif choice == '6':
        switchtrunk()
    elif choice== '7':
        vlanadd()
    else:
        print("Enter a valid option")
