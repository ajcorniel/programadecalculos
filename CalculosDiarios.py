import tkinter as tk
from PIL import Image, ImageTk
import glob

class Resize:
    def __init__(
                self,image="",
                shrink_ratio=2):
        self.image = image
        self.root = tk.Tk()
        self.root.title("Shrink")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.img = tk.PhotoImage(file=self.image)
        self.label = tk.Label(self.root, image=self.img)
        self.label.pack()
        self.lab1 = tk.Label(self.root)
        self.lab1['text'] = "..."
        self.lab1.pack()
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH)
        for file in glob.glob("*.png"):
            self.listbox.insert(0, file)
        self.lab2 = tk.Label(self.root, text="Insert ratio to shrink image (2=50%)")
        self.lab2.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.root.mainloop() 




def valormedio():
    entradas = [entrada1.get(), entrada2.get(), entrada3.get(), entrada4.get(), entrada5.get(), entrada6.get(), entrada7.get(), entrada8.get(), entrada9.get(), entrada10.get()]
    if entradas[9]=='':
        entradas.pop(9)   
    if entradas[8]=='':
        entradas.pop(8)   
    if entradas[7]=='':
        entradas.pop(7)    
    if entradas[6]=='':
        entradas.pop(6)   
    if entradas[5]=='':
        entradas.pop(5)   
    if entradas[4]=='':
        entradas.pop(4)    
    if entradas[3]=='':
        entradas.pop(3)    
    if entradas[2]=='':
        entradas.pop(2)
    if entradas[1]=='':
        entradas.pop(1)
    if entradas[0]=='':
        entradas.pop(0)
    valores = [int(i) for i in entradas]
    valorAlto= max(valores)
    valormedio= sum(valores) / len(valores)
    valorBajo= min(valores)
    return var3.set(valorBajo), var.set(valormedio), var2.set(valorAlto)

def porcentaje():
    result= ((int(entrada11.get())-int(entrada12.get()))/int(entrada12.get())) * 100
    porcentaje = str(round(result, 2)) + "%"
    return var4.set(porcentaje)

def borrar():
    entrada1.delete(0,999)
    entrada2.delete(0,999)
    entrada3.delete(0,999)
    entrada4.delete(0,999)
    entrada5.delete(0,999)
    entrada6.delete(0,999)
    entrada7.delete(0,999)
    entrada8.delete(0,999)
    entrada9.delete(0,999)
    entrada10.delete(0,999)
    entrada11.delete(0,999)
    entrada12.delete(0,999)


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
image = Image.open("nao.jpg")
image = image.resize((150, 155), Image.ANTIALIAS) ## The (250, 250) is (height, width)
photo = ImageTk.PhotoImage(image)
label = tk.Label(ventana, image = photo)
label.image = photo
label.place(x=30, y=30)

e1 = tk.Label(ventana,text='Italo Cambios', background="black", fg= "white")
e1.place(x=227, y=80)
entrada1 = tk.Entry(ventana)
entrada1.place(x=220, y=100)

e2 = tk.Label(ventana,text='R F Venezuela', background="black", fg= "white")
e2.place(x=337, y=80)
entrada2 = tk.Entry(ventana)
entrada2.place(x=330, y=100)

e3 = tk.Label(ventana,text='Remesas Dellivery', background="black", fg= "white")
e3.place(x=447, y=80)
entrada3 = tk.Entry(ventana)
entrance3 = str(entrada3)
entrada3.place(x=440, y=100)

e4 = tk.Label(ventana,text='Tubolivarexpress', background="black", fg= "white")
e4.place(x=557, y=80)
entrada4 = tk.Entry(ventana)
entrance4 = str(entrada4)
entrada4.place(x=550, y=100)

e5 = tk.Label(ventana,text='Peruvenws', background="black", fg= "white")
e5.place(x=667, y=80)
entrada5 = tk.Entry(ventana)
entrance5 = str(entrada5)
entrada5.place(x=660, y=100)

e6 = tk.Label(ventana,text='Emperuzolanos', background="black", fg= "white")
e6.place(x=777, y=80)
entrada6 = tk.Entry(ventana)
entrance6 = str(entrada6)
entrada6.place(x=770, y=100)

e7 = tk.Label(ventana,text='GlobalcambiosWS', background="black", fg= "white")
e7.place(x=887, y=80)
entrada7 = tk.Entry(ventana)
entrance7= str(entrada7)
entrada7.place(x=880, y=100)

e8 = tk.Label(ventana,text='Danilo', background="black", fg= "white")
e8.place(x=997, y=80)
entrada8 = tk.Entry(ventana)
entrance8 = str(entrada8)
entrada8.place(x=990, y=100)

e9 = tk.Label(ventana,text='Amiga Keylis', background="black", fg= "white")
e9.place(x=1107, y=80)
entrada9 = tk.Entry(ventana)
entrance9 = str(entrada9)
entrada9.place(x=1100, y=100)

e10 = tk.Label(ventana,text='AJ', background="black", fg= "white")
e10.place(x=1217, y=80)
entrada10 = tk.Entry(ventana)
entrance10 = str(entrada10)
entrada10.place(x=1210, y=100)

botoncalculo = tk.Button(ventana, text="calcular", fg="black", command=valormedio)
botoncalculo.place(x=660, y=230)


e11 = tk.Label(ventana, text="Cambio localbitcoins", background="black", fg="white")
e11.place(x=500, y=300)
entrada11= tk.Entry(ventana)
entrada11.place(x=500, y=320)

e12 = tk.Label(ventana, text="Tasa NAO soles", background="black", fg="white")
e12.place(x=630, y=300)
entrada12= tk.Entry(ventana)
entrada12.place(x=630, y=320)

calculoP = tk.Button(ventana, text="Calcular porcentaje de ganancia", background="white", fg="black", command=porcentaje)
calculoP.place(x=610, y=380)

RP = tk.Label(ventana, text="Ganancia", background="black", fg="white" )
RP.place(x=760,y=300)
resultadoP = tk.Label(ventana, bg="plum", textvariable=var4, width=20)
resultadoP.place(x=760,y=320)

borrar = tk.Button(ventana, text="borrar todo", fg="blue", command=borrar, height = 10, width = 10)
borrar.place(x=1100, y=190)

close = tk.Button(ventana, text="cerrar", fg="blue", command=cerrar)
close.place(x=1200, y=20)

R = tk.Label(ventana,text='Media', background="black", fg= "white")
R.place(x=660, y=140)
resultado = tk.Label(ventana, bg="plum", textvariable=var, padx=5, pady=5, width=20)
resultado.place(x=600, y=160)

R2 = tk.Label(ventana,text='Alta', background="black", fg= "white")
R2.place(x=460, y=140)
resultado2 = tk.Label(ventana, bg="plum", textvariable=var2, padx=5, pady=5, width=20)
resultado2.place(x=400, y=160)

R3 = tk.Label(ventana,text='Baja', background="black", fg= "white")
R3.place(x=860, y=140)
resultado3 = tk.Label(ventana, bg="plum", textvariable=var3, padx=5, pady=5, width=20)
resultado3.place(x=800, y=160)

ventana.mainloop()

