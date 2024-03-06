for x in range(0, 10, 2):
    print(x)

#Recorrer cadenas:
for x in 'Hello':
    print(x)

#Recorrer listas
mi_lista = ["abc", 123, "xyz"]
for i in range(0, len(mi_lista)): #el indicie como si fuera javascript
    print(i, mi_lista[i])
# salida: 0 abc, 1 123, 2 xyz
    
# O 

for v in mi_lista:
    print(v)
# salida: abc, 123, xyz

mi_dicc = { "nombre": "Noelle", "lenguaje": "Python" }
for k in mi_dicc:
    print(k)
# salida: nombre, lenguaje

mi_dicc = { "name": "Noelle", "languaje": "Python" }
for k in mi_dicc:
    print(mi_dicc[k])
# salida: Noelle, Python

#Break
for val in "cadena":
    if val == "e":
        break
    print(val) #Hasta ahí lo quiero, luego no
# salida: c, a, d

#Continue
for val in "cadena":
    if val == "e": #Me va a dar todos los demás elementos
        continue
    print(val)

# salida: c, a, d, n, a
# nota: no hay e en el resultado, pero el bucle continuó hasta después de la e

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# solo se ejecuta en una salida limpia del bucle while (es decir, no un break)
   print("sentencia else final")
# salida: 3, 2, 1