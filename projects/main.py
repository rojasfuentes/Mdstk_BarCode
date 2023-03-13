import openpyxl
from openpyxl import load_workbook
import datetime
import tkinter as tk
from tkinter import messagebox

# Abrir archivo de excel y cargar hoja activa
workbook = openpyxl.load_workbook(
    'C:/Users/JFROJAS/Desktop/Barcode/src/exampledb.xlsx')
sheet = workbook.active

# Crear archivo de resultados y cargar hoja activa
timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
resultados_filename = f"resultados_{timestamp}.xlsx"
resultados_workbook = openpyxl.Workbook()
resultados_sheet = resultados_workbook.active

# Agregar encabezados al archivo de resultados
encabezados = ['Barcode', 'Nombre', 'Clave', 'Lote', 'Fecha de caducidad']
for i, encabezado in enumerate(encabezados, start=1):
    resultados_sheet.cell(row=1, column=i, value=encabezado)


def search_barcode(barcode):
    name = []
    clave = []
    lotes = []
    fecha_caducidad = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == barcode:
            name.append(row[1])
            clave.append(row[2])
            lotes.append(row[3])
            fecha_caducidad.append(row[4])
    if not name:
        messagebox.showerror("Error", "No se encontraron resultados")
    else:
        lotes_seleccionados = list(set(lotes))
        lotes_seleccionados.sort()
        seleccion_lotes(lotes_seleccionados, barcode, name,
                        clave, lotes, fecha_caducidad)


def seleccion_lotes(lotes_seleccionados, barcode, name, clave, lotes, fecha_caducidad):
    ventana_lotes = tk.Tk()
    ventana_lotes.geometry("300x300")
    ventana_lotes.title("Seleccione un lote")
    for lote in lotes_seleccionados:
        tk.Button(ventana_lotes, text=lote, command=lambda lote_seleccionado=lote: resultados_busqueda(
            lote_seleccionado, barcode, name, clave, lotes, fecha_caducidad)).pack()
    ventana_lotes.mainloop()


def resultados_busqueda(lote, barcode, name, clave, lotes, fecha_caducidad):
    resultados = []
    for row in range(len(lotes)):
        if lotes[row] == lote:
            resultados.append({
                'Barcode': barcode,
                'Nombre': name[row],
                'Clave': clave[row],
                'Lote': lote,
                'Fecha de caducidad': fecha_caducidad[row]
            })
    guardar_resultados(resultados)


def guardar_resultados(resultados):
    # agregar resultados al archivo de resultados
    for resultado in resultados:
        resultados_sheet.append(
            [resultado['Barcode'], resultado['Nombre'], resultado['Clave'], resultado['Lote'], resultado['Fecha de caducidad']])

    # guardar archivo de resultados
    resultados_workbook.save(resultados_filename)
    messagebox.showinfo(
        "Éxito", f"Se han encontrado {len(resultados)} resultado(s) para el lote seleccionado")


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Buscar código de barras")
    tk.Label(root, text="Ingrese el código de barras a buscar:").pack()
    barcode_entry = tk.Entry(root)
    barcode_entry.pack()

    def on_click():
        barcode = int(barcode_entry.get())
        search_barcode(barcode)

    tk.Button(root, text="Buscar", command=on_click).pack()
    root.mainloop()
