import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
from PIL import ImageTk, Image

# Archivo
root = tk.Tk()  # Ventana principal
root.minsize(500, 500)
root.maxsize(500, 500)

def elige_juego():
    global Imagen_juego_photo
    global Imagen_juego
    global canvas
    canvas = tk.Canvas(root, width=512, height=512)
    canvas.pack(fill="both", expand=True)
    Imagen_juego = Image.open("C:/Users/Andre/PycharmProjects/Minijuegosv1/image.png")
    Imagen_juego_photo = ImageTk.PhotoImage(Imagen_juego)
    canvas.create_image(0, 0, image=Imagen_juego_photo, anchor="nw")
    canvas.create_text(256, 80, text="Elije el juego!", fill="black", font=('Helvetica 15 bold'))
    ttk.Separator(canvas).pack(side="top", pady="70")

    boton_juego1 = ttk.Button(canvas, text="Piedra, Papel, Tijera",command=juego1)
    boton_juego1.pack(side="top", pady="2", ipady="2", ipadx="40")


    boton_juego2 = ttk.Button(canvas, text="Traduce la palabra",command=juego2)
    boton_juego2.pack(side="top", pady="2", ipady="2", ipadx="45")

    boton_juego3 = ttk.Button(canvas, text="Adivina el número",command=juego3)
    boton_juego3.pack(side="top", pady="2", ipady="2", ipadx="45")

    boton_salir = ttk.Button(canvas, text="Salir",command=root.destroy)
    boton_salir.pack(side="top", pady="20", padx="20", ipady="2", ipadx="40")

def pantalla_main1():
    juego_root1.destroy()
    elige_juego()

def pantalla_main2():
    juego_root2.destroy()
    elige_juego()


def pantalla_main3():
    juego_root3.destroy()
    elige_juego()


def juego1():
    global juego_root1
    canvas.destroy()
    juego_root1 = tk.Canvas(root, width=512, height=512)
    juego_root1.pack(fill="both", expand=True)
    juego_root1.create_image(0, 0, image=Imagen_juego_photo, anchor="nw")

    boton_volver = ttk.Button(juego_root1, text="Volver",command=pantalla_main1)
    boton_volver.pack(side="top", pady="20", padx="20", ipady="2", ipadx="40")

    boton_salir = ttk.Button(juego_root1, text="Salir",command=root.destroy)
    boton_salir.pack(side="top", pady="20", padx="20", ipady="2", ipadx="40")

def juego2():
    global juego_root2
    canvas.destroy()
    juego_root2 = tk.Canvas(root, width=512, height=512)
    juego_root2.pack(fill="both", expand=True)
    juego_root2.create_image(0, 0, image=Imagen_juego_photo, anchor="nw")

    boton_volver = ttk.Button(juego_root2, text="Volver",command=pantalla_main2)
    boton_volver.pack(side="top", pady="20", padx="20", ipady="2", ipadx="40")

    boton_salir = ttk.Button(juego_root2, text="Salir",command=root.destroy)
    boton_salir.pack(side="top", pady="20", padx="20", ipady="2", ipadx="40")


def juego3():
    global juego_root3
    canvas.destroy()

    juego_root3 = tk.Canvas(root, width=512, height=512)
    juego_root3.pack(fill="both", expand=True)
    juego_root3.create_image(0, 0, image=Imagen_juego_photo, anchor="nw")

    main = ttk.Frame(juego_root3)
    main.pack(side="top", expand=True)
    main1 = ttk.Frame(juego_root3)
    main1.pack(side="top", expand=True)
    main2 = ttk.Frame(juego_root3)
    main2.pack(side="top", expand=True)


    label_nombre = ttk.Label(main, text="Introduce el número: ")
    label_nombre.pack(side="left")

    entry_numero = ttk.Entry(main, width=15)
    entry_numero.pack(side="left")


    boton_volver = ttk.Button(main2, text="Volver",command=pantalla_main3)
    boton_volver.pack(side="left", ipady="2", ipadx="20")

    boton_salir = ttk.Button(main2, text="Salir",command=root.destroy)
    boton_salir.pack(side="right", ipady="2",  ipadx="20")

    intentos = 3
    numero_secreto = random.randint(0, 200)

    def adivina_numero():
        nonlocal intentos
        if intentos > 0:
            numero = int(entry_numero.get())
            if numero == numero_secreto:
                resultado.set(f"¡Felicidades! Has adivinado el número secreto que era {numero_secreto} en {intentos} intentos.")
                boton_jugar["state"] = tk.DISABLED
            elif numero < numero_secreto:
                resultado.set(f"El número es mayor, te quedan {intentos} intentos.")
                intentos -= 1
            else:
                resultado.set(f"El número es menor, te quedan {intentos} intentos.")
                intentos -= 1
        else:
            resultado.set(f"Lo siento, has agotado tus intentos. El número era {numero_secreto}.")
            boton_jugar["state"] = tk.DISABLED

    boton_jugar = ttk.Button(main, text="Jugar", command=adivina_numero)
    boton_jugar.pack(side="bottom", ipady="2", ipadx="20")

    resultado = tk.StringVar()
    boton_resultado = ttk.Button(main1, textvariable=resultado)
    boton_resultado.pack(side="bottom")

elige_juego()
root.mainloop()

# https://www.geeksforgeeks.org/using-lambda-in-gui-programs-in-python/