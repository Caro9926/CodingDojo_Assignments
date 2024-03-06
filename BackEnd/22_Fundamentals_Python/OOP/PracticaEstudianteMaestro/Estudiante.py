from Persona import Persona

class Estudiante(Persona):
    listaEstudiantes = []
    def __init__( self, nombre, apellido, id, curso ):
        super().__init__( nombre, apellido )
        self.id = id
        self.curso = curso
        self.calificaciones = []
        Estudiante.listaEstudiantes.append( self )
    
    def asignaCalificacion( self, nota ):
        self.calificaciones.append( nota )

    def informacionAbstracto(self):
        self.informacion()
        print( "Curso: ", self.curso )
        print( "Calificaciones: " )
        print( self.calificaciones )
    
    # Sobre escritura
    #def informacion( self ):
    #    super().informacion()
    #    print( "Calificaciones: " )
    #    print( self.calificaciones )

    # Sin sobre escritura
    def informacionEstudiante( self ):
        self.informacion()
        print( "Curso: ", self.curso )
        print( "Calificaciones: " )
        print( self.calificaciones )
    
    @classmethod
    def imprimeListaEstudiantes( cls ):
        for estudiante in cls.listaEstudiantes:
            estudiante.informacionEstudiante()