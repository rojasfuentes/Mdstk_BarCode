# Mdstk_BarCode
**Change the workbook Path**  
workbook = openpyxl.load_workbook(
    'filepath/file.xlsx')  
**Activate venv**  
env\Scripts\activate.bat  

Este es un programa que permite buscar productos en una base de datos de códigos de barras. El usuario ingresa el código de barras del producto que desea buscar y el programa muestra los resultados correspondientes, incluyendo el nombre del producto, la clave, el lote y la fecha de caducidad. Si hay varios resultados, el usuario puede seleccionar el lote deseado y agregar la cantidad de productos que desea buscar. El programa guarda los resultados en un archivo de Excel separado y muestra un mensaje de éxito al usuario.

El programa utiliza la librería openpyxl para cargar y guardar archivos de Excel y la librería tkinter para crear la interfaz gráfica de usuario.

**Requisitos previos**  
El programa requiere Python 3 y las siguientes librerías:  

openpyxl  
tkinter

