import tkinter as tk

botones_en_pantalla = False


def ocultar_botones():
    global botones_en_pantalla
    boton1.pack_forget()
    boton2.pack_forget()
    boton3.pack_forget()
    botones_en_pantalla = False


def mostrar_botones():
    global botones_en_pantalla
    boton1.pack()
    boton2.pack()
    boton3.pack()
    botones_en_pantalla = True


def boton_click():
    print("Botón presionado")
    ocultar_botones()


def ingresar_numero(event):
    global botones_en_pantalla
    numero = entry.get()
    print("El número ingresado es:", numero)
    entry.delete(0, tk.END)  # Borra el contenido del entry
    if not botones_en_pantalla:
        mostrar_botones()


def salir():
    ventana.destroy()  # Cierra la ventana


# Crear la ventana
ventana = tk.Tk()

# Darle foco a la ventana
ventana.focus_force()

# Crear el label que dice "Ingresa un número"
label = tk.Label(ventana, text="Ingresa un número:")
label.pack()

# Crear el entry para que el usuario ingrese el número
entry = tk.Entry(ventana)
entry.pack()

# Posicionar el foco en el Entry
entry.focus()

# Crear el botón para que el usuario pueda enviar el número
boton = tk.Button(ventana, text="Enviar",
                  command=lambda: ingresar_numero(None), width=10, height=1)
boton.pack(padx=10, pady=10)

# Crear los botones numerados del 1 al 3
boton1 = tk.Button(ventana, text="1", command=boton_click)
boton2 = tk.Button(ventana, text="2", command=boton_click)
boton3 = tk.Button(ventana, text="3", command=boton_click)

# Crear el botón "Salir"
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack()

# Mostrar la ventana
ventana.mainloop()
