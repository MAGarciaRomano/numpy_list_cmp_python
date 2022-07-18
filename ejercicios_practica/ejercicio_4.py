# Numpy [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con comprensión de listas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Utilizar comprensión de listas con condicionales

    # 1)
    # Utilizar comprensión de listas para convertir
    # una lista de números como str en números tipo int
    # sería un conversor string --> int
    # Ojo! Tener cuidado con lo string/caracteres
    # que no son números, utilizar condicionales para detectarlos
    # reemplazar dicho str "no numérico" por 0
    # TIP: Recomendamos ver el método "isdigit" de strings
    # para aplicar en este caso.
    list_numeros_str = ['5', '2', '3', '', '7', 'NaN']
    conversion = [int(x) if x.isdigit() else 0 for x in list_numeros_str]
    print('Lista de números a partir de convertir o reemplazar strings.')
    print(conversion)


    # ¿Ya terminaron el ejercicio? ¿Por qué no prueban
    # hacer negativo alguno de los números de la lista?
    # ¿Qué sucede con isdigit? Sorprendente, ¿no?
    
    # Dos opciones de solución:
    # a) Multiplicando  por -1 la comprensión realizada en el punto anterior:
    conversion_negativos = [-1*(int(x)) if x.isdigit() else 0 for x in list_numeros_str]
    print('Los string convertidos en enteros y multiplicados por -1.')
    print(conversion_negativos)

    # b) Creando nueva lista  y por compresión multiplicar por -1
    # cada elemento de la lista conversion.
    negativos = [-1*x for x in conversion]
    print('Los enteros de la lista conversion multiplicados por -1.')
    print(negativos)    

    print("Terminamos")