'''
Astrid Sofía Pérez Aguirre
Gilberto Hernández Quintero 
Guillermo González González 
Odette Estefanía Almaguer Domínguez 
'''

from tkinter import *
from tkinter import ttk
import tkinter as tk 
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from cdp import *

list_dev = []
ssh = []
ip_escogida = []

def ventana2():
    #ssh es la lista con ip, password, user 
    print(ssh)
    usuario = ssh.pop()    
    contraseña = ssh.pop()
    ip = ssh.pop()

    print(usuario)

    dispositivos_lista = cdp(usuario, contraseña, ip)
    dis = []
    con = []
    

    for i in range(len(dispositivos_lista)):
        for x in range(len(dispositivos_lista[i].vecino)):
            dis.append(dispositivos_lista[i].nombre)
            con.append(dispositivos_lista[i].vecino[x].nombre)
    def visualizar():

        df = pd.DataFrame(list(zip(dis, con)), columns = ['Dispositivo', 'Vecinos'])
        print(df)
        #df = df['Vecinos'].replace('.final.', '-', inplace=True)
        G = nx.from_pandas_edgelist(df, 'Dispositivo', 'Vecinos')
        #pos = nx.spring_layout(G)
        nx.draw_networkx(G, with_labels=True, node_size=1000, node_color="skyblue", node_shape="o", alpha=0.5, linewidths=10, font_size=15, 
                font_color="black", font_weight="bold", width=3, edge_color="grey")
        ax = plt.subplot()
        ax.set_facecolor("#f2fcff")
        ax.set_alpha(0.7)
        plt.title(label = 'Topología de red', fontsize=20, backgroundcolor ="skyblue", color = 'white' )
        plt.show()

    root2 = tk.Tk()
    root2.title("Topología")
    root2.configure(bg='#202324')
    Label(root2, text= " D I S P O S I T I V O S   E N   L A   R E D ",  font=('Arial 16'), fg = '#FFFFFF', background= '#1b1c1c').pack(side=tk.TOP, padx=5, pady=5)
    Label(root2, text= "", font=('Arial 4'), background= '#202324').pack(side=tk.TOP, padx=5, pady=5)
    button= tk.Button(root2, text= "Ver topología", background= '#202324',  fg = '#FFFFFF')
    #button['command'] = visualizar
    button.pack()
    var_dis = tk.StringVar()
    Label(root2, text= "", font=('Arial 4'), background= '#202324').pack(side=tk.TOP, padx=5, pady=5)
    dis_l = Label(root2,text ="Dispositivo a modificar:", bg= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
    Entry(root2,width="30", textvariable= var_dis, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)
    ip_escogida.append(var_dis.get())

    def ventana3():
        print(ip_escogida)

        for i in list_dev:
            if i.nombre == dis:
                print(i.nombre)

        if __name__ == '__main__':
            root = tk.Tk()
            root.title("Configuraciones")
            root.geometry("400x700")
            root.configure(bg='#202324')

            Label(root, text= "CONFIGURACIONES", font=('Arial 20'), fg = '#FFFFFF', background= '#1b1c1c').pack(side=tk.TOP, padx=5, pady=5)

            conf1_str = tk.StringVar()
            conf1_l = Label(root,text ="Banner Motd:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf1_e= Entry(root,width="30", textvariable= conf1_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf2_str = tk.StringVar()
            conf2_l = Label(root,text ="Cambiar hostname:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf2_e= Entry(root,width="30", textvariable= conf2_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf3_str = tk.StringVar()
            conf3_l = Label(root,text ="Cambiar contraseña:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf3_e= Entry(root,width="30", textvariable= conf3_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf4_str = tk.StringVar()
            conf4_l = Label(root,text ="Activar/desactivar password encryption:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
    
            opcion = IntVar() 

            Radiobutton(root, text="Activar",value=1, background = "#202324", foreground= '#FFFFFF').pack()
            Radiobutton(root, text="Desactivar", value=2, background = "#202324", fg = '#FFFFFF').pack()

            conf5_str = tk.StringVar()
            conf5_l = Label(root,text ="Activar/desactivar ip domain lookup:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            Radiobutton(root, text="Activar",value=1, background = "#202324", foreground= '#FFFFFF').pack()
            Radiobutton(root, text="Desactivar", value=2, background = "#202324", fg = '#FFFFFF').pack()

            conf6_str = tk.StringVar()
            conf6_l = Label(root,text ="Descripcion de interfaces:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf6_e= Entry(root,width="30", textvariable= conf6_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf7_str = tk.StringVar()
            conf7_l = Label(root,text ="Cambiar NTP Server:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf7_e= Entry(root,width="30", textvariable= conf7_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf8_str = tk.StringVar()
            conf8_l = Label(root,text ="Cambiar contraseña de consola:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf8_e= Entry(root,width="30", textvariable= conf8_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf9_str = tk.StringVar()
            conf9_l = Label(root,text ="Agregar usuario SSH:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf9_e= Entry(root,width="30", textvariable= conf9_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            conf10_str = tk.StringVar()
            conf10_l = Label(root,text ="Cambiar servidor syslog:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
            conf10_e= Entry(root,width="30", textvariable= conf10_str, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

            
            def ver_datos():
                print(conf1_str.get())
                print(conf2_str.get())
                print(conf3_str.get())
                print(conf4_str.get())
                print(conf5_str.get())
                print(conf6_str.get())
                print(conf7_str.get())
                print(conf8_str.get())
                print(conf9_str.get())
                print(conf10_str.get())
    
            b2 = Button(root, text="Guardar configuraciones", command=ver_datos, background= '#202324',  fg = '#FFFFFF')
            b2.pack(side=tk.BOTTOM, padx=5, pady=5)
    
    bconf = Button(root2, text="Configuraciones", command = ventana3, background= '#202324',  fg = '#FFFFFF')
    bconf.pack(side=tk.BOTTOM, padx=5, pady=5)

#VENTANA 1
root = tk.Tk()
root.title("Find-IP")
root.configure(bg='#202324')
root.geometry('400x320')

Label(root, text= "   I N I C I O   ", font=('Arial 20'), fg = '#FFFFFF', background= '#1b1c1c').pack(side=tk.TOP, padx=5, pady=5)

var_user = tk.StringVar()
usuario_l = Label(root,text ="Usuario:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
tusuario= Entry(root,width="30", textvariable= var_user, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

var_contra = tk.StringVar()
contra_l = Label(root,text ="Contraseña:", background= '#202324', fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
tcontra= Entry(root,width="30", textvariable= var_contra, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

var_ip = tk.StringVar()
ip_l = Label(root,text ="IP:", background= '#202324',  fg = '#FFFFFF').pack(side=tk.TOP, padx=5, pady=5)
tip= Entry(root,width="30", textvariable= var_ip, bg = '#323536', fg = '#000000').pack(side=tk.TOP, padx=5, pady=5)

def ver_datos():
    ssh.append(var_ip.get())
    ssh.append(var_contra.get()) 
    ssh.append(var_user.get())

b1 = tk.Button(root, text='Buscar', command = ventana2, background= '#202324',  fg = '#FFFFFF')
b1.pack(side=tk.BOTTOM, padx=5, pady=5)
b2 = Button(root, text="Enviar datos", command=ver_datos, background= '#202324',  fg = '#FFFFFF')
b2.pack(side=tk.BOTTOM, padx=5, pady=5)

#guardarDispositivos():
#guardarInterfaces():
#list = cdp()
root.mainloop()

