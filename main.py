# Prueba Técnica Fernando Herrera

import xlwings as xw
import tkinter as tk
from tkinter import filedialog
from selenium import webdriver
from handleEmail import send_email




#funcion para obtener el nombre del archivo de excel
my_dir=None
def read_name(): 
    global my_dir
    my_dir = filedialog.askopenfile(filetypes=[("Archivos de Excel", "*.xlsx")]).name
    l1.config(text=my_dir)
    window.quit()
  
#Una simple gui para obtener el archivo excel
window = tk.Tk()
window.title("Prueba técnica")
window.geometry("800x600")

b1=tk.Button(window,text="Select File",font=22,command=lambda:read_name(),bg="lightgreen")
b1.grid(row=0,column=0,padx=10,pady=20)
l1=tk.Label(window,text=my_dir,bg="yellow",font=18)
l1.grid(row=0,column=1,padx=2)
window.mainloop()

#Funcion para obtener array de datos
print(my_dir)
def obtenerDatos():
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

registrosExcel = obtenerDatos()

def filtrarDatos(string,pos):
    array=[]     
    for i in registrosExcel:
        if i[pos] == string:
             array.append(i)
    
    return array

atrasados = filtrarDatos("Atrasado",9)
regularizados = filtrarDatos("Regularizado",9)
# print(len(atrasados))
# print(len(regularizados))

send_email(atrasados)

