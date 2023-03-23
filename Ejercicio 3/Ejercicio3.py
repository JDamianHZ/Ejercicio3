from tkinter import *
from tkinter import ttk
from tkinter import ttk
import tkinter as ttk
from tkinter import font



raiz=Tk()




mainFrame= ttk.Frame(raiz,width=600, height=200,bg="black") #widget transparete hasta especificar
mainFrame.grid()

sub2_Frame= ttk.Frame(mainFrame,bg="gray40",width=600, height=200) #widget transparete hasta especificar
sub2_Frame.grid(column=0, row=0,sticky=(W,E,N,S))

sub3_Frame= ttk.Frame(mainFrame,bg="black") #widget transparete hasta especificar
sub3_Frame.grid(column=0, row=1,sticky=(W,E,N,S))

sub6_Frame= ttk.Frame(sub3_Frame, width=690, height=240, bg="gray2") #widget transparete hasta especificar
sub6_Frame.grid(column=0, row=4,sticky=(W,E,N,S),padx= 20, pady= 10)

sub4_Frame= ttk.Frame(sub6_Frame, bg="gray2") #widget transparete hasta especificar
sub4_Frame.grid(column=0, row=0,padx= 20, pady= 10,sticky=(W,E,N,S))


sub7_Frame= ttk.Frame(sub6_Frame, bg="gray2") #widget transparete hasta especificar
sub7_Frame.grid(column=0, row=1,padx= 20, pady= 10,sticky=(W,E,N,S))

sub5_Frame= ttk.Frame(sub6_Frame, bg="gray2") #widget transparete hasta especificar
sub5_Frame.grid(column=1, row=0,sticky=(W,E,N,S),padx= 20, pady= 10,rowspan=2)

#frame 1
imagen2 = PhotoImage(file="menu.png")
etqImagen=ttk.Label(sub2_Frame,bg="gray2", bd=0)
etqImagen.grid(column=0,row=0,sticky=(W))
etqImagen['image']=imagen2

timg=ttk.Label(sub2_Frame,text="SPAI 4.0",font=("Arial",12,"bold"),foreground="white",bg="gray40").grid(column=1,row=0)

#----- frame izquierdo------

imagen = PhotoImage(file="primero.png")
imagen_redimencionada=imagen.subsample(2,2)
etqImagen=ttk.Label(sub4_Frame,bg="gray2")
etqImagen.grid(column=0,row=0,sticky=(W))
etqImagen['image']=imagen


imagen3 = PhotoImage(file="segundo.png")
etqImagen=ttk.Label(sub4_Frame,bg="gray2")
etqImagen.grid(column=1,row=0,sticky=(W))
etqImagen['image']=imagen3


#izquierdo abajo


imagen5 = PhotoImage(file="tercero.png")
etqImagen=ttk.Label(sub7_Frame,bg="gray2")
etqImagen.grid(column=0,row=0,sticky=(W))
etqImagen['image']=imagen5


imagen6 = PhotoImage(file="quinto.png")
etqImagen=ttk.Label(sub7_Frame,bg="gray2")
etqImagen.grid(column=1,row=0,sticky=(W))
etqImagen['image']=imagen6


#derecho
imagen7 = PhotoImage(file="sexto.png")
etqImagen=ttk.Label(sub5_Frame,bg="gray2")
etqImagen.grid(column=0,row=0,sticky=(W))
etqImagen['image']=imagen7
raiz.mainloop()