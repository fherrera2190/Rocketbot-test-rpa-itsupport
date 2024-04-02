def filtrarDatos(registrosExcel,string,pos):
    array=[]     
    for i in registrosExcel:
        if i[pos] == string:
             array.append(i)
    
    return array