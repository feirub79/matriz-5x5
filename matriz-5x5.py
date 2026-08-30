matriz = [[0 for _ in range(5)] for _ in range(5)]
#Ingreso de valores en la matriz
for i in range(5):
    for j in range(5):
        valor = int(
            input(f"Ingrese el valor para la posición [{i}][{j}]: ")
        )
        matriz[i][j] = valor

print("\nMatriz ingresada:")
#Recorrido de la matriz utilizando ciclos anidados
for i in range(5):          
    for j in range(5):
        #impresion
        print(matriz[i][j], end=" ") #continua en la misma linea
    print() #salto de linea al final de la fila