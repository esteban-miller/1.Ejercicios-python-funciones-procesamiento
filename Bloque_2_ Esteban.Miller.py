#Esteban miller 
#Sergio caballero
#Pablo zafra 

path = 'C:/Users/HP/Desktop/practicas PYTHON'
def Ejercicio_Bloque_2(path):
    '''
    Esta funcion toma como argumento una ruta a una carpeta que contenga archivos .pdb y para cada uno de ellos
    muestra su ID, titulo, autores y numero de atomos y aminoacidos
    
    se ha implementado la libreria re porque en algunos ficheros el titulo ocupa mas de una linea (1D00) y el siguiente indentado
    no tiene el mismo numero de espacios. Es posible que pase lo mismo con los autores
    '''
    import os, re
    lista_archivos = [file for file in os.listdir(path) if file.endswith('.pdb')]

    if lista_archivos == []:
        return "La carpeta no contiene ficheros en formato .pdb"
    else: 
        for documento in lista_archivos:
            print("Nombre del archivo:", documento)
            ruta = path + '\\' + documento
        
            with open(ruta, mode ='r', encoding='utf-8') as file:
                titulo, autores, lista_aminoacidos, lista_atomos = '','',[],[]
                for linea in file:
                    if linea.startswith('HEADER'):
                        ID = linea.strip()[-4:]
                    elif linea.startswith('TITLE'):
                        titulo += re.split(r'TITLE\s+',linea.strip())[1]
                    elif linea.startswith("AUTHOR"):
                            autores += re.split(r'AUTHOR\s+',linea.strip())[1]
                    elif linea.startswith('SEQRES'):
                        lista_aminoacidos += linea.strip()[19:].split(' ')
                    elif linea.startswith('ATOM') or linea.startswith('HETATM'):
                        lista_atomos.append(linea.strip()[-2:].replace(' ',""))
                
                dic_atomos = {atomo : lista_atomos.count(atomo) for atomo in set(lista_atomos)}
                dic_amino = {amino : lista_aminoacidos.count(amino) for amino in set(lista_aminoacidos)}
                print("ID:", ID)
                print("Titulo:", titulo)
                print("Autores:", autores)
                print("Hay", len(dic_atomos.keys()), "atomos distintos, en total hay", len(lista_atomos), "y el siguiente diccionario muestra cuantos hay de cada tipo: \n", dic_atomos)
                print("Hay", len(dic_amino.keys()), "aminoacidos distintos, en total hay", len(lista_aminoacidos), "y el siguiente diccionario muestra cuantos hay de cada tipo: \n", dic_amino)
                print('\n')
                
Ejercicio_Bloque_2(path)

