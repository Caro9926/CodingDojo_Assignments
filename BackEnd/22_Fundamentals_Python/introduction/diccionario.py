
findesemana = {"Dom": "Domingo", "Sáb": "Sábado"} # notación literal
capitales = {} # crea un diccionario vacío y luego agrega valores
capitales["svk"] = "Bratislava"
capitales["deu"] = "Berlin"
capitales["dnk"] = "Copenhagen"
print(findesemana)
print(capitales)
##Acceder valores
print(findesemana["Dom"])
print(capitales["svk"])


print("len() method :", len(findesemana))

##Remover valores
#valor_eliminado = capitales.pop('svk') # eliminará la clave 'svk' y devolverá su valor
#del capitales['dnk'] # eliminará la clave y no devolverá nada

##Diccionarios anidados
contexto = {'preguntas': [
    { 'id': 1, 'contenido': '¿Por qué hay luz en el refrigerador y no en el congelador?'},
    { 'id': 2, 'content': '¿Por qué las ovejas no se encogen cuando llueve?'},
    { 'id': 3, 'contenido': '¿Por qué se llaman apartamentos cuando están todos pegados?'},
    { 'id': 4, 'contenido': '¿Por qué los autos conducen en la autopista y se estacionan en la entrada?'}
]}



