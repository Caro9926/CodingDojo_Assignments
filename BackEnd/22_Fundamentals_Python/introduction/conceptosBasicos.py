import random

# Un comentario en linea
nombre_alex = "Alejandro"
calificacionAlex = 9.6
edad = 20
graduado = True

print( "Nombre: " + nombre_alex )
print( f"Calificacion: {calificacionAlex}" )
print( "Edad: %d Calificacion: %f Nombre: %s" % (edad, calificacionAlex, nombre_alex) )
print( "Graduado: {} Nombre: {}".format(graduado, nombre_alex) )
print( "Calificacion: " + str(calificacionAlex) )

print( type(graduado) )

print( random.randint(1,100) )

print( nombre_alex.upper() )