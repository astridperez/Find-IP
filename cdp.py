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

from netmiko import ConnectHandler

class Dispositivo():
    def __init__(self,nombre,tipo,ip,list_vecinos:list):
        self.nombre = nombre
        self.tipo = tipo
        self.ip = ip
        self.vecino = list_vecinos
        self.__version = None

    def __str__(self):
        cadena_vecinos = ''
        for k in range(len(self.vecino)):
            cadena_vecinos = cadena_vecinos + self.vecino[k].interfaz + ' ' + self.vecino[k].nombre + ' ' + self.vecino[k].ip + '\n'
        return self.nombre + ' ' + self.tipo + ' ' + self.ip + ' \n' + 'VECINOS: \n' + cadena_vecinos


class Vecino(Dispositivo):
    def __init__(self,nombre,interfaz,ip):
        self.interfaz = interfaz
        self.nombre = nombre
        self.ip = ip

    def __str__(self):
        return '\nVecino : \n' + self.interfaz + ' ' + self.nombre + ' ' + self.ip 


#si usa ip default-gateway virtual (hsrp) descubrirá doble dicho router
def cdp(start_username,start_password,start_host):

    device = {
                'device_type': 'cisco_ios',
                'host': '',
                'username': '',
                'password': ''
                }


    dispositivos_lista = [] #lista de objetos Dispositivo para return

    known_ips = [] #lista de ips descubiertas por cdp

    #asignando datos al arreglo y diccionario para conexión
    known_ips.append(start_host) 
    device['username'] = start_username
    device['password'] = start_password


    #Repetimos el proceso por cada ip que conozca y se vaya agregando
    for i in known_ips:  
        
        device['host'] = i #cambiamos la ip de device{} en cada ciclo 
        ips_disp = []
        vecinos_agregar = []

        net_connect = ConnectHandler(**device)

        #sacamos outputs de cada show
        output = net_connect.send_command('show cdp neighbors detail',use_textfsm=True)
        output1 = net_connect.send_command('show ip interface brief', use_textfsm=True)
        output2 = net_connect.send_command('show running-config | include hostname')
        output3 = net_connect.send_command('show ip interface brief', use_textfsm=True)
        net_connect.disconnect()

        #ciclos para sacar el hostname sin los primeros caracteres "hostname"
        hostname = ""
        for f in range(len(output2)):
            while f >= 9 and f <= len(output2):
                hostname = hostname + output2[f]
                break

        #print(output3) #mostrar output3 
        cont_int = (len(output3))

        if cont_int >= 10:
            output3 = "Switch"
        else:
            output3 = "Router"
        deviceType = output3 #deviceType será Router o Switch


        for x in output: #almacenar output 0 (cdp) en known_ips y known_dest
            if x['management_ip'] not in known_ips:
                if start_host[0:3] in x['management_ip'][0:3]:
                    known_ips.append(x['management_ip'])

            vecinos_agregar.append(Vecino(x['destination_host'][0:2],x['local_port'],x['management_ip'])) #----___________________________-------------------------



        for each in output1: #almacenar output1 (ips interfaces activas) en ips_disp
            if each['status'] == 'up':
                ips_disp.append(each['ipaddr'])


        dispositivos_lista.append(Dispositivo(hostname,deviceType,i,vecinos_agregar))


        #ELIMINAR DUPLICADOS
    nueva_lista = []
    lista_nombres= []
    

    for cada in range(len(dispositivos_lista)):
        for cado in range(len(dispositivos_lista)):
            if cada == cado:
                break
            if dispositivos_lista[cada].nombre != dispositivos_lista[cado].nombre:
                if dispositivos_lista[cado].nombre not in lista_nombres:
                    lista_nombres.append(dispositivos_lista[cado].nombre)
                    nueva_lista.append(dispositivos_lista[cado])

    return (nueva_lista)