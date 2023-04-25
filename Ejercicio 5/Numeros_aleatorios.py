import random
import Abintree as ab

# Generar 1000 numeros aleatorios enteros y contar cuantos son pares y cuantos impares

def generar_numeros_aleatorios_arbol_binario():
    """Genera 1000 numeros aleatorios enteros y los guarda en un arbol binario"""
    arbol = ab.BinaryTree()
    for i in range(1000):
        arbol.insert(random.randint(0, 1000))
    return arbol

def contar_numeros_pares_impares(arbol):
    """Cuenta cuantos numeros pares e impares hay en el arbol"""
    pares = 0
    impares = 0
    for i in range(len(arbol)):
        if arbol.getAt(i) % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def main():
    """Funcion principal"""
    arbol = generar_numeros_aleatorios_arbol_binario()
    pares, impares = contar_numeros_pares_impares(arbol)
    print("Pares: ", pares)
    print("Impares: ", impares)

if __name__ == "__main__":
    main()