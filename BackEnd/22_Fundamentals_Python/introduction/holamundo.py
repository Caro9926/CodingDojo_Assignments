# 1. TAREA: imprime "Hola, mundo"
print("Hola Mundo")
# 2. imprime "Hola, Noelle" con el nombre en una variable
name = "Carolina"
print("Hola",name )	#con coma
print( "Hola " + name )	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
number = 14
print( "Hola", number )	# con una coma
print( "Hola " + str(number) )	# con una +	
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
fave_food1 = "tallarines"
fave_food2 = "pollo a la brasa"
print( "Mi comida favorita es {} y mi segunda comida favorita es {}".format(fave_food1, fave_food2)) # con .format()
print(f"Mi comida favorita es {fave_food1} y mi segunda comida favorita es {fave_food2}" ) # con una cadena f
##Otras formas
print("Mi nombre es %s y cumplo %d" % (name, number))


