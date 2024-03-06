numeros = [10, 20, 30, 40, 50]

i = 0
while i < len( numeros ):
    print( numeros[i] )
    i += 1
else:
    print( "Se termino el ciclo" )

for x in range( 0, len(numeros ), 2 ):
    print( x )

for y in range( 1, 11 ):
    print( y )

for elemento in numeros:
    print( elemento )

estudiante = {
    "nombre" : "Alex",
    "apellido" : "Martinez",
    "edad" : 25
}

for propiedad in estudiante:
    print( propiedad )
    print( estudiante[propiedad] )