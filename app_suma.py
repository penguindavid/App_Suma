# se importala libreria tkinter 
from tkinter import *
# -----------------------------
# funciones de la app 
# -----------------------------


# -----------------------------
# ve ntana principal de la app
# -----------------------------

# se declara una variable  llamada ventana_principal, que anquiere las caracteristicas de un juego

ventana_principal= Tk()

# Titulo de ventana 
ventana_principal.title("David macias ")

# Tamaño de la ventana 
ventana_principal.geometry("800x500")

# deshabilita boton de minimizar la ventana 
ventana_principal.resizable(0,0)

# color de fondo de la ventana 
ventana_principal.config(bg= "gray")

#--------------------------
# variables globales
#--------------------------
a = StringVar()
b = StringVar()
c = IntVar()
# -------------------------
# frame 1 entrada de datos
# -------------------------

frame_1  = Frame(ventana_principal)
frame_1.config(bg = "ivory2", width=780,height=240)
frame_1.place(x=10, y=10)

#etiqueta para el titulo de la app 
titulo= Label(frame_1,text="colegio San Jose de Guanenta")
titulo.config(bg="yellow", fg="blue", font= ("arial", 16))
titulo.place(x=250,y=10)

# imag-en-Logo
logo= PhotoImage(file="img/btn-suma.png")
label_logo = Label (frame_1,image=logo)
label_logo.place(x=10,y=10)

#etiqueta para subtitulo 1 de la app
subtitulo1= Label(frame_1,text ="especialidad en sistemas")
subtitulo1.config(bg="yellow", fg="blue", font= ("Arial",12))
subtitulo1.place(x=300, y=50)

# etiqueta para subtitulo 2de la app
subtitulo2= Label(frame_1,text ="Suma de dos enteros")
subtitulo2.config(bg="ivory2", fg="blue", font= ("Arial",15))
subtitulo2.place(x=300, y=70)

# etiqueta para el primer valor
label_a= Label(frame_1,text ="a =")
label_a.config(bg="ivory2", fg="blue", font= ("Arial",20))
label_a.place(x=300, y=120)

# etiqueta para el segundo valor
label_a= Label(frame_1,text ="b =")
label_a.config(bg="ivory2", fg="blue", font= ("Arial",20))
label_a.place(x=300, y=160) 

# Entry

entry_a= Entry(frame_1, width=4, textvariable=a)
entry_a.config (font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487, y=120)

entry_b= Entry(frame_1, width=4, textvariable=b)
entry_b.config (font=("Arial", 20), justify=CENTER)
entry_b.place(x=487, y=160)


# -----------------------------
# frame 2 panel de operaciones
# -----------------------------



frame_2  = Frame(ventana_principal)
frame_2.config(bg = "ivory2", width=780,height=120)
frame_2.place(x=10, y=260)

# ----------------------
# boton para sumar 
# ----------------------
bt_sumar= Button(frame_2, Text"sumar", width=10, height=10)

# -----------------------------
# frame 3 Resultados
# -----------------------------

frame_3  = Frame(ventana_principal)
frame_3.config(bg = "ivory2", width=780,height=120)
frame_3.place(x=10, y=390)


# metodo principal que despliega la ventana en pantalla 
ventana_principal.mainloop()