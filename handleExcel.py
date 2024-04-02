import xlwings as xw

def obtenerDatos(my_dir):
    wb=xw.Book(my_dir)
    sheet = wb.sheets(1)
    rango_datos = sheet.range("A1").expand()
    num_filas = rango_datos.rows.count
    num_columnas = rango_datos.columns.count

    registrosExcel = []

    for i in range(2, num_filas + 1):
        fila = []
        for j in range(1, num_columnas + 1):
            valor_celda = sheet.range((i, j)).value
            if valor_celda is not None:
                fila.append(valor_celda)
        if fila:
                registrosExcel.append(fila)
    wb.close()
    return registrosExcel