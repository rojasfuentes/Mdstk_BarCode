# Mdstk_BarCode
**Change the workbook Path**  
workbook = openpyxl.load_workbook(
    'filepath/file.xlsx')  
**Activate venv**  
env\Scripts\activate.bat  

El siguiente programa permite buscar información en una base de datos de productos a través de un código de barras. Se utiliza la librería openpyxl para leer la información desde un archivo de Excel y para guardar los resultados en otro archivo de Excel.

El usuario ingresa el código de barras a buscar y el programa muestra los resultados correspondientes. Si hay varias opciones de lote para un producto, el usuario puede seleccionar uno de ellos para ver los resultados correspondientes.

Además, el programa guarda los resultados en un archivo de Excel con un nombre que incluye la fecha y hora de la búsqueda, para que cada búsqueda tenga un archivo diferente.


