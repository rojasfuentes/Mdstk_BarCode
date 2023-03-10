import openpyxl
from openpyxl import load_workbook

workbook = openpyxl.load_workbook(
    'C:/Users/JFROJAS/Desktop/Barcode/src/exampledb.xlsx')
sheet = workbook.active

if __name__ == '__main__':
# crear archivo de Excel para guardar los resultados
    resultados_filename = "todos_los_resultados.xlsx"
resultados_workbook = openpyxl.Workbook()
resultados_sheet = resultados_workbook.active
encabezados = ['Código de barras', 'Nombre', 'Clave', 'Lote', 'Fecha de caducidad']
for i, encabezado in enumerate(encabezados, start=1):
    resultados_sheet.cell(row=1, column=i, value=encabezado)
row_index = 2
    
while True:
        barcode = int(input("Ingrese el código de barras a buscar: "))
        if barcode == "salir":
            break
        name = []
        clave = []
        lote = []
        fecha_caducidad = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            if row[0] == barcode:
                name.append(row[1])
                clave.append(row[2])
                # asumiendo que el número del lote está en la columna 4
                lote.append(row[3])
                # asumiendo que la fecha de caducidad está en la columna 5
                fecha_caducidad.append(row[4])
    
        # Imprimir resultados
        if name:
            print("Nombre(s):", ", ".join(name))
            print("Clave(s):", ", ".join(clave))
            # mostrar opciones únicas de lote
            print("Lote(s):", ", ".join(set(lote)))
            lote_seleccionado = input("Seleccione un lote: ")
            # encontrar las filas correspondientes al lote seleccionado
            resultados = []
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if row[0] == barcode and row[3] == lote_seleccionado:
                    resultados.append({
                        'Nombre': row[1],
                        'Clave': row[2],
                        'Lote': row[3],
                        'Fecha de caducidad': row[4]
                    })
            # imprimir resultados
            print(f"Resultados para el lote {lote_seleccionado}:")
            for resultado in resultados:
                print("Nombre:", resultado['Nombre'])
                print("Clave:", resultado['Clave'])
                print("Lote:", resultado['Lote'])
                print("Fecha de caducidad:", resultado['Fecha de caducidad'])
            # guardar resultados en un archivo Excel
            new_filename = f"resultados_{lote_seleccionado}.xlsx"
            new_workbook = openpyxl.Workbook()
            new_sheet = new_workbook.active
            # escribir encabezados de las columnas
            encabezados = ['Nombre', 'Clave', 'Lote', 'Fecha de caducidad']
            for i, encabezado in enumerate(encabezados, start=1):
                new_sheet.cell(row=1, column=i, value=encabezado)
            # escribir datos de los resultados
            for i, resultado in enumerate(resultados, start=2):
                new_sheet.cell(row=i, column=1, value=resultado['Nombre'])
                new_sheet.cell(row=i, column=2, value=resultado['Clave'])
                new_sheet.cell(row=i, column=3, value=resultado['Lote'])
                new_sheet.cell(row=i, column=4, value=resultado['Fecha de caducidad'])
            new_workbook.save(new_filename)
        else:
            print("No se encontraron resultados")