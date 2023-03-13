import tkinter as tk


def ingresar_numero():
    numero = entry.get()
    print("El número ingresado es:", numero)


# Crear la ventana
ventana = tk.Tk()

# Crear el label que dice "Ingresa un número"
label = tk.Label(ventana, text="Ingresa un número:")
label.pack()

# Crear el entry para que el usuario ingrese el número
entry = tk.Entry(ventana)
entry.pack()

# Crear el botón para que el usuario pueda enviar el número
boton = tk.Button(ventana, text="Enviar", command=ingresar_numero)
boton.pack()

# Mostrar la ventana
ventana.mainloop()
