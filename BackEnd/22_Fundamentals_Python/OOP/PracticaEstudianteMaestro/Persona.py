class Persona:
    listaPersonas = []
    def __init__( self, nombre, apellido ):
        self.nombre = nombre
        self.apellido = apellido
        Persona.listaPersonas.append( self )
    
    def getNombre( self ):
        return self.nombre
    
    def getApellido( self ):
        return self.apellido
    
    def setNombre( self, nuevoNombre ):
        self.nombre = nuevoNombre

    def setApellido( self, nuevoApellido ):
        self.apellido = nuevoApellido
    
    def informacion( self ):
        print( "Nombre:", self.nombre )
        print( "Apellido:", self.apellido )

    def informacionAbstracto( self ):
        raise NotImplementedError

    @classmethod
    def imprimeListaPersonas( cls ):
        for persona in cls.listaPersonas:
            #print( persona.getNombre() + " " + persona.getApellido() )
            persona.informacion()