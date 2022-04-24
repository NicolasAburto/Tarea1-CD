########################################### Descripción del proyecto: ###########################################
#   Programa en Python que simula una carrera de caballos.
#   Descipción:
#    - Se creará un programa que simule una carrera de caballos con avance aleatorio.
#    - Código desarrollado mediante metodología de programación modular, con el objetivo de reutilizar bibliotecas de funciones y/o métodos.
#    - Versión: 0.1 (Prueba y demostración)
#
#   Autores:
#       - José Avilán (https://github.com/JoseAvilan)
#       - Nicolas Aburto (https://github.com/NicolasAburto)
#       - Franco Avilés (https://github.com/FrancoAv1)
#
#   Licencia:
#       - Abril 2022. Apache 2.0.
#
#################################################################################################################

import random, time

class ArgumentoException( Exception):
    # Excepción a ser lanzadas por error en los argumentos de llamada a una función o método.
    pass

class Caballo:

    def __init__( self, nombre = None):
        #CONSTRUCTOR

        self.nombre = nombre
        self.__carreras = []
        self.__pasosCarreraActual = 0

    def __str__( self):
        # DEVUELVE EL OBJETO COMO UNA CADENA, COMO UN TOSTRING()

        return self.nombre

    @property
    def nombre( self):
        # DEVUELVE EL NOMBRE DEL CABALLO

        return self.__nombre

    @nombre.setter
    def nombre( self, nombre = None):
        # DEFINE EL NOMBRE A LOS CABALLOS

        if nombre is None:
            self.__nombre = "<Sin Nombre>"
        
        nombre = str( nombre).strip()
        self.__nombre = "<Sin nombre>" if not nombre else nombre 

    @property
    def pasosCarreraActual( self):
        # DEVUELVE EL NÚMERO DE PASOS EN LA CARRERA QUE LLEVA HASTA ESE MOMENTO
        
        return self.__pasosCarreraActual

    def inscribirCarrera( self, carrera):
        # AÑADIR UNA CARRERA PARA QUE EL CABALLO PUEDA PARTICIPAR
        
        if carrera is None:
            raise ArgumentoException( "Error en el argumento carrera (None).")

        if carrera in self.__carreras:
            raise ArgumentoException( "Ya se ha inscrito en esa carrera.")

        self.__carreras.append( carrera)
        self.__pasosCarreraActual = 0

    def avanzarPasos( self):
        #AVANZA UN NÚMERO DE PASOS ALEATORIO ENTRE LOS VALORES 0 Y 9, EN SU TURNO CORRESPONDIENTE

        self.__pasosCarreraActual += random.randrange( 0, 10 )

class Carrera:

    __PASOS_META = 80

    def __init__( self, pasosMeta = None, nombre = None):
        # CONSTRUCTOR
       
        self.pasosMeta = pasosMeta
        self.nombre = nombre
        self.__caballos = dict()
        self.__ganadores = []

    def PASOS_META():
        # DEVUELVE EL NÚMERO DE PASOS EN LA QUE ESTÁ LA META

        return Carrera.__PASOS_META

    @property
    def nombre( self):
        # DEVUELVE EL NOMBRE DEL CABALLO
       
        return self.__nombre

    @nombre.setter
    def nombre( self, nombre = None):
        # DEFINE EL NOMBRE DE LA CARRERA
     
        if nombre is None:
            self.__nombre = "<Sin Nombre>"
        
        nombre = str( nombre).strip()
        self.__nombre = "<Sin nombre>" if not nombre else nombre 

    @property
    def pasosMeta( self):
        # DEVUELVE EL NÚMERO DONDE SE ENCUENTRA LA META
       
        return self.__pasosMeta

    @pasosMeta.setter
    def pasosMeta( self, pasosMeta = None):
        # DEFINE EL NUMERO DE PASOS EN LA QUE SE ENCUENTRA LA META
        
        if not pasosMeta:
            self.__pasosMeta = Carrera.__PASOS_META
            return

        try:
            pasosMeta = int( pasosMeta)
        except ValueError as e:
            print( e)
            raise ArgumentoException( "Argumento pasosMeta inválido.")

        if pasosMeta < 1:
            raise ArgumentoException( "Argumento pasosMeta < 1.")

        self.__pasosMeta = pasosMeta

    @property
    def ganadores( self):
        # DEVUELVE UNA TUPLA CON LOS GANADORES DE LA CARRERA

        return tuple( self.__ganadores)

    def numeroDeInscritos( self):
        # DEVUELVE EL NÚMERO DE CABALLOS QUE ESTÁN EN LA CARRERA
        
        return len( self.__caballos)

    def visualizarTurno( self):
        # MUESTRA EL ESTADO DE LA CARRERA HASTA ESE MOMENTO

        for caballo, datos in self.__caballos.items():
            print( "%2d-%12s: %s" % 
                   (datos["dorsal"], caballo.nombre[:12], "="*datos["pasos"]))

        print( "%15s:%s" % ("Meta", " "*self.__pasosMeta + "|"))
            
    def registrarCaballo( self, caballo):
        # REGISTRA LOS CABALLOS A PARTICIPAR EN LA CARRERA

        if caballo is None:
            raise ArgumentoException( "Argumento caballo inválido (None).")
        
        if caballo in self.__caballos: 
            raise ArgumentoException( "El caballo ya está inscrito.")

        self.__caballos[caballo] = {"pasos": 0, "puesto": None,
                                    "dorsal": self.numeroDeInscritos()+1}
        caballo.inscribirCarrera( self)

    def avanzarTurno( self):
        # AVANZA UN TURNO EN TODOS LOS CABALLOS QUE ESTÁN EN LA CARRERA

        esFinalDeCarrera = False
        for caballo, datos in self.__caballos.items():
            caballo.avanzarPasos()
            datos["pasos"] = caballo.pasosCarreraActual
            if (not esFinalDeCarrera and
                caballo.pasosCarreraActual >= self.pasosMeta):
                esFinalDeCarrera = True
        return esFinalDeCarrera

    def calcularPuestos( self):
        # CALCULA EN QUE PUESTO QUEDÓ CADA CABALLO, ASÍ TAMBIÉN GUARDA EL CABALLO GANADOR
   
        self.__clasificacion = sorted(self.__caballos.items(), 
                                      key=lambda x: x[1]["pasos"], reverse=True)
        puesto = 1
        pasosAnterior = self.__clasificacion[0][1]["pasos"]
        for caballo, datos in self.__clasificacion:
           if datos["pasos"] < pasosAnterior:
                puesto += 1
                pasosAnterior = datos["pasos"]
           elif puesto == 1: self.__ganadores.append( caballo)
           datos["puesto"] = puesto
            
    def puestoAlcanzado( self, caballo):
        # DEVUELVE EL PUESTO EN QUE QUEDÓ CADA CABALLO

        if caballo not in self.__caballos:
            raise ArgumentoException( "El caballo no participó en la carrera.")

        return self.__caballos[caballo]["puesto"]
        
    def esGanador( self, caballo):
        # DEVUELVE SI ES QUE UN CABALLO GANÓ LA CARRERA O NO

        return caballo in self.__ganadores

    def mostrarClasificacion( self):
        # MUESTRA EN LA TERMINAL EL PUESTO EN QUE QUEDÓ CADA CABALLO

        print( "\n**** CLASIFICACIÓN DE LA CARRERA ****")
        for caballo, datos in self.__clasificacion:
            print( "%dº.- Dorsal %2d | %20s | Pasos %d" % 
                   (datos["puesto"], datos["dorsal"], caballo.nombre, 
                    datos["pasos"]))
     
while True:
    pasos = input( "Pasos línea de meta [%d]: " % Carrera.PASOS_META())
    try:
        carrera = Carrera( pasos)
    except ArgumentoException as e:
        print( e)
        print( "Introduce los datos de la carrera correctamente.")
        continue
    break

while True:
    numeroDeCaballos = input( "\nIntroduce el número de caballos: ")
    if not numeroDeCaballos.strip(): continue
    try:
        numeroDeCaballos = int( numeroDeCaballos)
    except ValueError as e:
        print( e)
        print( "Debes introducir un número de caballos participantes.")
        continue
    if numeroDeCaballos > 1: break

    print( "Debes introducir al menos dos caballos.")

for i in range( numeroDeCaballos):
    while True:
        print( "\nIntroduce los datos del Caballo %d" % (i+1))
        nombre = input( "\tNombre: ")
        try:
            caballo = Caballo( nombre)
        except ArgumentoException as e:
            print( e)
            print( "Introduce los datos del caballo correctamente")
            continue
        break
    carrera.registrarCaballo( caballo)

print( "\nLa carrera está por comenzar ...\n")

esFinalDeCarrera = False
while not esFinalDeCarrera: 
    time.sleep(1)
    esFinalDeCarrera = carrera.avanzarTurno()
    carrera.visualizarTurno()
    
carrera.calcularPuestos()
carrera.mostrarClasificacion()
print( "Ganadores: " + str( [caballo.nombre for caballo in carrera.ganadores]))