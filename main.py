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

    titulo = tk.Label(juego_root1, text="Piedra, Papel y Tijera", font=("Helvetica", 20))
    titulo.pack(pady=20)

    opcionJugador = tk.IntVar(value=0)
    opciones = [("Piedra", 0), ("Papel", 1), ("Tijera", 2)]
    for texto, valor in opciones:
        tk.Radiobutton(
            juego_root1,
            text=texto,
            variable=opcionJugador,
            value=valor
        ).pack()

    resultado = tk.StringVar(value="")
    etiqueta_resultado = tk.Label(juego_root1, textvariable=resultado, font=("Helvetica", 12))
    etiqueta_resultado.pack(pady=10)

    def jugar():
        opcionMaquina = random.randint(0, 2)
        opcionesTexto = ["Piedra", "Papel", "Tijera"]
        eleccionMaquina = opcionesTexto[opcionMaquina]

        if opcionJugador.get() == opcionMaquina:
            resultado.set(f"Máquina eligió {eleccionMaquina}. ¡Empate!")
        elif (opcionJugador.get() == "Piedra" and opcionMaquina == "Papel") or (opcionJugador.get() == "Tijera" and opcionMaquina == "Piedra") or (opcionJugador.get() == "Papel" and opcionMaquina == "Tijera"):
            resultado.set(f"Máquina eligió {eleccionMaquina}. ¡Ganaste!")
        else:
            resultado.set(f"Máquina eligió {eleccionMaquina}. ¡Perdiste!")

    boton_jugar = ttk.Button(juego_root1, text="Jugar", command=jugar)
    boton_jugar.pack(pady=10)

    main2 = ttk.Frame(juego_root1)
    main2.pack(side="top", expand=True)

    boton_volver = ttk.Button(main2, text="Volver", command=pantalla_main1)
    boton_volver.pack(side="left", ipady="2", ipadx="20")

    boton_salir = ttk.Button(main2, text="Salir", command=root.destroy)
    boton_salir.pack(side="right", ipady="2", ipadx="20")

def juego2():
    global juego_root2
    canvas.destroy()

    juego_root2 = tk.Canvas(root, width=512, height=512)
    juego_root2.pack(fill="both", expand=True)
    juego_root2.create_image(0, 0, image=Imagen_juego_photo, anchor="nw")

    main = ttk.Frame(juego_root2)
    main.pack(side="top", expand=True)
    main1 = ttk.Frame(juego_root2)
    main1.pack(side="top", expand=True)
    main2 = ttk.Frame(juego_root2)
    main2.pack(side="top", expand=True)

    label_nombre = ttk.Label(main, text="Traduce la palabra: ")
    label_nombre.pack(side="left")

    entry_str = ttk.Entry(main, width=15)
    entry_str.pack(side="left")

    boton_volver = ttk.Button(main2, text="Volver", command=pantalla_main2)
    boton_volver.pack(side="left", ipady="2", ipadx="20")

    boton_salir = ttk.Button(main2, text="Salir", command=root.destroy)
    boton_salir.pack(side="right", ipady="2", ipadx="20")

    palabras = {
        "stone": "piedra",
        "fire": "fuego",
        "body": "cuerpo",
        "call": "llamar",
        "clean": "limpiar",
        "doctor": "doctor",
        "card": "tarjeta",
        "club": "club",
        "dance": "bailar",
        "dream": "soñar",
        "black": "negro",
        "class": "clase",
        "child": "niño",
        "country": "país",
        "finish": "terminar",
        "eat": "comer",
        "boat": "barco",
        "end": "fin",
        "fast": "rápido",
        "song": "canción",
    }

    resultado = tk.StringVar()
    etiqueta_resultado = ttk.Label(main1, textvariable=resultado)
    etiqueta_resultado.pack()

    puntos = tk.IntVar(value=0)
    palabras_restantes = tk.IntVar(value=5)
    palabra_actual = tk.StringVar()

    def cambiar_palabra():
        if palabras_restantes.get() > 0:
            nueva_palabra = random.choice(list(palabras.keys()))
            palabra_actual.set(nueva_palabra)
            resultado.set(f"Traduce la palabra: {nueva_palabra}")
        else:
            resultado.set(f"Juego terminado. Puntuación final: {puntos.get()} de 5")
            boton_jugar["state"] = "disabled"

    def jugar():
        if palabras_restantes.get() > 0:
            respuesta = entry_str.get().strip().lower()
            if respuesta == palabras[palabra_actual.get()].lower():
                puntos.set(puntos.get() + 1)
                resultado.set("¡Correcto!")
            else:
                resultado.set(f"Incorrecto. La respuesta correcta era: {palabras[palabra_actual.get()]}")

            palabras_restantes.set(palabras_restantes.get() - 1)
            cambiar_palabra()

    # Botón para iniciar el juego
    boton_jugar = ttk.Button(main, text="Jugar", command=jugar)
    boton_jugar.pack(side="bottom", ipady="2", ipadx="20")

    # Iniciar el juego mostrando la primera palabra
    cambiar_palabra()

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