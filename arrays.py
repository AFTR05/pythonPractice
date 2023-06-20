import math

def prome(numbers):
    suma = sum(numbers)
    prom = suma / len(numbers)
    return prom

def organice(numbers):
    numbers.sort()
    return numbers

def justEven(numbers):
    even=[]
    for numero in numbers:
        if numero % 2 == 0:
            even.append(numero)
    return even        

def justOdd(numbers):
    odd=[]
    for numero in numbers:
        if numero % 2 != 0:
            odd.append(numero)
    return odd  

# Ejemplo de uso
listNumber = [5,8,12,3,6,10,8,6,4]
prom = prome(listNumber)
print("El promedio de la lista es:", prom)
print(f"La lista organizada es: {organice(listNumber)}")
print(f"La lista solo con pares es: {justEven(listNumber)}")
print(f"La lista solo con impares es: {justOdd(listNumber)}")