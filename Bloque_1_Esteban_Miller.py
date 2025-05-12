# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 18:16:27 2024

@author: HP
"""
## EJERCICIO 1
lista_1 = [12, 3, 4, 5]
lista_2 = [2, 4, 1, 7]

def calculadora_de_pares(lista_1, lista_2, operacion): 
    resultado_ = []
    for un_numero, otro_numero in zip(lista_1, lista_2):
        if operacion == 'sumar' :
            resultado_.append(un_numero+ otro_numero)
        elif operacion == 'restar' :
            resultado_.append(un_numero - otro_numero)
        elif operacion == 'multiplicar' :
            resultado_.append(un_numero * otro_numero)
        elif operacion == 'dividir' :
            if otro_numero != 0:
                resultado_.append(un_numero / otro_numero)
            else : resultado_.append(0)
    return resultado_
resultado_suma =calculadora_de_pares(lista_1, lista_2,'sumar')
print(resultado_suma)

resultado_resta =calculadora_de_pares(lista_1, lista_2, 'restar')
print(resultado_resta)

resultado_multiplicar =calculadora_de_pares(lista_1, lista_2, 'multiplicar')
print(resultado_multiplicar)

resultado_dividir =calculadora_de_pares(lista_1, lista_2, 'dividir')
print(resultado_dividir)

### ejercicio 2

def contar_consonantes(palabra):
    consonantes ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in palabra if char in consonantes) 
 
def string_con_mas_consonantes(lista):
    max_consonantes = -1
    resultado__ = ""
    indice = -1
    
    for i, palabra in enumerate(lista):
        num_consonantes = contar_consonantes(palabra)
        if num_consonantes > max_consonantes:
            max_consonantes = num_consonantes
            resultado__ = palabra
            indice = i 
    return resultado__ , len(resultado__), indice

lista_de_strings = ["Teclado", "Raton", "Pantalla", "Tecla", "Pixel"]
resultado__ = string_con_mas_consonantes(lista_de_strings)
print(resultado__)
resultado__














