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

import pymysql

def conexionsql(dispositivos_lista):
    class ConexionDB:
        def open(self):
            conexion=pymysql.connect(user='root',
                                        password='cisco',
                                        host='localhost', 
                                        database='final',
                                        )
                                        
            return conexion

        def Selectd(self):
            con = self.open()
            cur = con.cursor()
            cur.execute("SELECT * FROM Dispositivos")
            self.consulta=cur.fetchall()
            con.close()
            return self.consulta

        def Selecti(self):
            con = self.open()
            cur = con.cursor()
            cur.execute("SELECT * FROM Interfaces")
            self.consulta=cur.fetchall()
            con.close()
            return self.consulta

    #for each in dispositivos_lista:
        def Insertd(self):
            con = self.open()
            cur = con.cursor()
            for each in range(len(dispositivos_lista)):
                sql = f"INSERT INTO Dispositivos (Nombre, Tipo) VALUES ('{dispositivos_lista[each].nombre}', '{dispositivos_lista[each].tipo}')"
                cur.execute(sql)
                self.consulta=cur.fetchall()
            con.commit()
            con.close()
            return self.consulta
            
    #for each1 in dispositivos_lista:
        #for int in dispositivos_lista[each1].Vecino:

        def Inserti(self):
                con = self.open()
                cur = con.cursor()
                for each1 in range(len(dispositivos_lista)):
                    for int in range(len(dispositivos_lista[each1].vecino)):
                        sql = f"INSERT INTO Interfaces (Dispositivo, Interfaz, Vecino_conectado, IP_vecino) VALUES ('{dispositivos_lista[each1].nombre}', '{dispositivos_lista[each1].vecino[int].nombre}', '{dispositivos_lista[each1].vecino[int].interfaz}', '{dispositivos_lista[each1].vecino[int].ip}')"
                        cur.execute(sql)
                        self.consulta=cur.fetchall()
                con.commit()
                con.close()
                return self.consulta

    p = ConexionDB()
    p.Insertd()
    p.Inserti()
    data = p.Selectd()
    data1 = p.Selecti()
    print(data)
    print(data1)
conexionsql()