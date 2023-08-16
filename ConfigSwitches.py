from netmiko import *

dispsips = ['10.0.1.4', '10.0.1.5', '10.0.1.6', '10.0.1.7']

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

for each in dispsips:
	Dispositivos['host'] = each
	net_connect = ConnectHandler(**Dispositivos)
	net_connect.config_mode()
	net_connect.send_config_set(command)
	net_connect.send_config_set(commandadmin)
	net_connect.send_config_set(commandl)
	net_connect.send_config_set(servidores)

	output = net_connect.send_command('show ip interface brief', use_textfsm=True)
	for i in range(len(output)):
		commands = ['interface ' + str(output[i]['intf']), 'description Interfaz de un switch con ip: ' + str(Dispositivos['host'])]
		net_connect.send_config_set(commands)
		if i >= 2 and i <= 5:
			net_connect.send_command('switchport trunk allowed vlan 10,20,30,40,50')
		if (i >= 6 and i <= 25) or i == 27:
			if i >= 22 and i <= 25:
				seguridadserver = ['interface ' + str(output[i]['intf']), 'switchport mode access','switchport port-security','switchport port-security maximum 5','switchport port-security mac-address sticky','switchport nonegotiate','spanning-tree portfast','spanning-tree bpduguard enable']
				net_connect.send_config_set(seguridadserver)
				continue
			seguridad = ['interface ' + str(output[i]['intf']), 'switchport mode access','switchport port-security','switchport port-security maximum 5','switchport nonegotiate','spanning-tree portfast','spanning-tree bpduguard enable']
			net_connect.send_config_set(seguridad)
			
	net_connect.disconnect()
