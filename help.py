def filtrarDatos(registrosExcel,string,pos):
    array=[]     
    for i in registrosExcel:
        if i[pos] == string:
             array.append(i)
    
    return array

def sanitizarPalabra(texto):
    palabras = texto.split() 
    return palabras[0].lower()


def transformDate(fecha):
    return fecha.strftime("%Y-%m-%d")

# print(sanitizarPalabra("aaaaaAa BBBBBBBBBB"))