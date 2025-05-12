###ejercicio 1

import math

def es_primo(n):
    """Verifica si un número n es primo."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def suma_primos(N):
    """Calcula la suma de los primeros N números primos y muestra los primos encontrados."""
    primos = []  # Lista para almacenar los primos
    num = 2  # Empezamos a buscar primos desde el número 2
    suma = 0  # Variable para acumular la suma

    while len(primos) < N:
        if es_primo(num):
            primos.append(num)  # Agregamos el primo encontrado a la lista
            suma += num  # Sumamos el primo al total
        num += 1  # Incrementamos para comprobar el siguiente número

    # Mostrar los resultados
    print(f"Los primeros {N} números primos son: {primos}")
    print(f"La suma de los primeros {N} números primos es: {suma}")
    return suma, primos

# Ejemplo de uso:
N = 10  # Aquí defines cuántos primos quieres sumar
suma, primos = suma_primos(N)


##### ejercicio 3
import re

# Diccionario 
masas_atomicas = {
    'C': 12.011,   # Carbono
    'H': 1.007,    # Hidrógeno
    'O': 15.999,   # Oxígeno
    'N': 14.006,   # Nitrógeno
    'Fe': 55.845,} # Hierro 

def calc_masa_mol(fórmula):
   
    elementos = re.findall(r'([A-Z][a-z]?\d*)', fórmula)
    
    masa_total = 0
    
    for elem in elementos:
        # Dividimos el símbolo del elemento y la cantidad 
        simbolo = re.match(r'[A-Za-z]+', elem).group(0)  
        cantidad = re.search(r'\d+', elem)
        cantidad = int(cantidad.group(0)) if cantidad else 1  # Si no hay número, asumimos 1
        
        # Si el símbolo está en el diccionario 
        if simbolo in masas_atomicas:
            masa_total += masas_atomicas[simbolo] * cantidad
        else:
            raise ValueError(f"Elemento desconocido: {simbolo}")
    
    return masa_total

#prueba
metano = 'C H4'
glucosa = 'C6 H12 O6'
grupo_hemo = 'C34 H32 Fe N4 O4'

print(f"Masa molecular del Metano: {calc_masa_mol(metano)} g/mol")
print(f"Masa molecular de la Glucosa: {calc_masa_mol(glucosa)} g/mol")
print(f"Masa molecular del Grupo Hemo: {calc_masa_mol(grupo_hemo)} g/mol")
