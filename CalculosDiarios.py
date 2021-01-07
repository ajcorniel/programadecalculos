import tkinter as tk

def valorAlto():
    valorAlto= max(int(entrada1.get()),int(entrada2.get()),int(entrada3.get()),int(entrada4.get()),int(entrada5.get())+int(entrada6.get()),int(entrada7.get()),int(entrada8.get()),int(entrada9.get()),int(entrada10.get()))
    return var2.set(valorAlto)

def valormedio():
    valormedio= (int(entrada1.get())+int(entrada2.get())+int(entrada3.get())+int(entrada4.get())+int(entrada5.get())+int(entrada6.get())+int(entrada7.get())+int(entrada8.get())+int(entrada9.get())+int(entrada10.get())) / 10
    return var.set(valormedio)

def valorBajo():
    valorBajo= min(int(entrada1.get()),int(entrada2.get()),int(entrada3.get()),int(entrada4.get()),int(entrada5.get())+int(entrada6.get()),int(entrada7.get()),int(entrada8.get()),int(entrada9.get()),int(entrada10.get()))
    return var3.set(valorBajo)

def porcentaje():
    porcentaje= ((int(entrada11.get())-int(entrada12.get()))/int(entrada12.get())) * 100
    return var4.set(porcentaje)

def cerrar():
    ventana.destroy()

ventana= tk.Tk()
ventana.title("programa")
ventana.geometry("2500x1500")
ventana.configure(background='grey')
var = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()


e1 = tk.Label(ventana,text='Italo Cambios', background="black", fg= "white")
e1.place(x=100, y=40)
entrada1 = tk.Entry(ventana)
entrada1.place(x=100, y=60)

e2 = tk.Label(ventana,text='R F Venezuela', background="black", fg= "white")
e2.place(x=200, y=40)
entrada2 = tk.Entry(ventana)
entrada2.place(x=200, y=60)

e3 = tk.Label(ventana,text='Remesas Dellivery', background="black", fg= "white")
e3.place(x=300, y=40)
entrada3 = tk.Entry(ventana)
entrada3.place(x=300, y=60)

e4 = tk.Label(ventana,text='Tubolivarexpress', background="black", fg= "white")
e4.place(x=400, y=40)
entrada4 = tk.Entry(ventana)
entrada4.place(x=400, y=60)

e5 = tk.Label(ventana,text='Peruvenws', background="black", fg= "white")
e5.place(x=500, y=40)
entrada5 = tk.Entry(ventana)
entrada5.place(x=500, y=60)

e6 = tk.Label(ventana,text='Emperuzolanos', background="black", fg= "white")
e6.place(x=600, y=40)
entrada6 = tk.Entry(ventana)
entrada6.place(x=600, y=60)

e7 = tk.Label(ventana,text='GlobalcambiosWS', background="black", fg= "white")
e7.place(x=700, y=40)
entrada7 = tk.Entry(ventana)
entrada7.place(x=700, y=60)

e8 = tk.Label(ventana,text='Danilo', background="black", fg= "white")
e8.place(x=800, y=40)
entrada8 = tk.Entry(ventana)
entrada8.place(x=800, y=60)

e9 = tk.Label(ventana,text='Amiga Keylis', background="black", fg= "white")
e9.place(x=900, y=40)
entrada9 = tk.Entry(ventana)
entrada9.place(x=900, y=60)

e10 = tk.Label(ventana,text='AJ', background="black", fg= "white")
e10.place(x=1000, y=40)
entrada10 = tk.Entry(ventana)
entrada10.place(x=1000, y=60)

botoncalculo2 = tk.Button(ventana, text="calcular alta", fg="black", command=valorAlto)
botoncalculo2.place(x=330, y=90)

botoncalculo = tk.Button(ventana, text="calcular media", fg="black", command=valormedio)
botoncalculo.place(x=530, y=90)

botoncalculo3 = tk.Button(ventana, text="calcular baja", fg="black", command=valorBajo)
botoncalculo3.place(x=730, y=90)

e11 = tk.Label(ventana, text="Cambio localbitcoins", background="black", fg="white")
e11.place(x=250, y=350)
entrada11= tk.Entry(ventana)
entrada11.place(x=300, y=400)

e12 = tk.Label(ventana, text="Tasa NAO soles", background="black", fg="white")
e12.place(x=400, y=350)
entrada12= tk.Entry(ventana)
entrada12.place(x=400, y=400)

calculoP = tk.Button(ventana, text="Calcular porcentaje", background="white", fg="black", command=porcentaje)
calculoP.place(x=700, y=400)

resultadoP = tk.Label(ventana, bg="plum", textvariable=var4, width=20)
resultadoP.place(x=500,y=400)

close = tk.Button(ventana, text="cerrar", fg="blue", command=cerrar)
close.place(x=700, y=500)

resultado = tk.Label(ventana, bg="plum", textvariable=var, padx=5, pady=5, width=20)
resultado.place(x=500, y=140)

resultado2 = tk.Label(ventana, bg="plum", textvariable=var2, padx=5, pady=5, width=20)
resultado2.place(x=300, y=140)

resultado3 = tk.Label(ventana, bg="plum", textvariable=var3, padx=5, pady=5, width=20)
resultado3.place(x=700, y=140)


ventana.mainloop()

