'''
PROYECTO INTEGRADOR
Gilberto Hernández Quintero 
Guillermo González González 
Odette Estefanía Almaguer Domínguez 
Astrid Sofía Pérez Aguirre
José Alberto Aguilar García 
Juan Claudio Fernández Torres 
Roberto Darío Ruiz Pacheco
'''

from netmiko import *

dispsips = ['10.0.50.1', '10.0.50.2', '10.0.70.2', '10.0.80.1', '10.0.80.2']

Dispositivos = {
    'host': '',
    'username': 'final',
    'password': 'final',
    'device_type': 'cisco_ios'
}
commandl = ['line vty 0 15', 'logging synchronous', 'exec-timeout 30', 'password final', 'access-class 1 in', 'exit']
command = ['line console 0', 'password final', 'logging synchronous', 'exec-timeout 30', 'exit']
servidores = ['logging 10.0.30.9', 'ntp server 10.0.30.9', 'service password-encryption', 'service timestamps log datetime msec', 'ip ssh authentication-retries 2', 'ip ssh time-out 80', 'login block-for 40 attempts 3 within 40']
commandadmin = ['enable secret final','banner motd # PROHIBIDO EL ACCESO A PERSONAL NO AUTORIZADO #','no ip domain-lookup','access-list 1 permit 10.0.20.0 0.0.0.255','access-list 1 deny any']
commandNAT = ['ip nat inside source static 10.0.30.10 148.239.63.111', 'ip nat inside source static 10.0.30.9 148.239.63.112', 'access-list 2 permit 10.0.0.0 0.0.255.255', 'ip nat pool NAT1 148.239.63.114 148.239.63.116 netmask 255.255.255.0', 'ip nat inside source list 2 pool NAT1']

for each in dispsips:
    Dispositivos['host'] = each
    net_connect = ConnectHandler(**Dispositivos)

    output = net_connect.send_command('show ip interface brief', use_textfsm=True)
    if Dispositivos['host'] == '10.0.70.2':
        net_connect.send_config_set(commandNAT)
        for i in range(len(output)):
            if i == 1:
                commandsNAT1 = ['interface ' + str(output[i]['intf']), 'description Interfaz de un router con ip: ' + str(Dispositivos['host']), 'no shutdown', 'ip address 148.239.62.113 255.255.255.254', 'ip nat outside']
                net_connect.send_config_set(commandsNAT1)
            else:
                commandsNAT = ['interface ' + str(output[i]['intf']), 'description Interfaz de un router con ip: ' + str(Dispositivos['host']), 'ip nat inside']
                net_connect.send_config_set(commandsNAT)

    for i in range(len(output)):
        commands = ['interface ' + str(output[i]['intf']), 'description Interfaz de un router con ip: ' + str(Dispositivos['host'])]
        net_connect.send_config_set(commands)
    
    net_connect.config_mode()
    net_connect.send_config_set(command)
    net_connect.send_config_set(commandadmin)
    net_connect.send_config_set(commandl)
    net_connect.send_config_set(servidores)
        
net_connect.disconnect()



