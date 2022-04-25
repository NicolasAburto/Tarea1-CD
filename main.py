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
        self.Carrera = []
        self.PasosCaballo = 0

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
            self.__nombre = "<Name>"
        
        nombre = str( nombre).strip()
        self.__nombre = "<Name>" if not nombre else nombre 

    @property
    def PasosCarrera( self):
        # DEVUELVE EL NÚMERO DE PASOS EN LA CARRERA QUE LLEVA HASTA ESE MOMENTO
        
        return self.PasosCaballo

    def AñadirCarrera( self, carrera):
        # AÑADIR UNA CARRERA PARA QUE EL CABALLO PUEDA PARTICIPAR
        
        self.Carrera.append( carrera)
        self.PasosCaballo = 0

    def Avanzar( self):
        #AVANZA UN NÚMERO DE PASOS ALEATORIO ENTRE LOS VALORES 0 Y 9, EN SU TURNO CORRESPONDIENTE

        self.PasosCaballo += random.randrange( 0, 10 )

class Carrera:

    __PASOS_META = 50

    def __init__( self, nombre = None):
        # CONSTRUCTOR
       
        self.PasosMeta = 50
        self.nombre = nombre
        self.__caballos = dict()
        self.__CaballoGanador = []

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
    def PasosMeta( self):
        # DEVUELVE EL NÚMERO DONDE SE ENCUENTRA LA META
       
        return self.__PasosMeta

    @PasosMeta.setter
    def PasosMeta( self, PasosMeta = None):
        # DEFINE EL NUMERO DE PASOS EN LA QUE SE ENCUENTRA LA META

        self.__PasosMeta = PasosMeta

    @property
    def CaballoGanador( self):
        # DEVUELVE UNA TUPLA CON LOS CaballoGanador DE LA CARRERA

        return tuple( self.__CaballoGanador)

    def CantidadInscritos( self):
        # DEVUELVE EL NÚMERO DE CABALLOS QUE ESTÁN EN LA CARRERA
        
        return len( self.__caballos)

    def MostrarTurno( self):
        # MUESTRA EL ESTADO DE LA CARRERA HASTA ESE MOMENTO

        for caballo, datos in self.__caballos.items():
            print( "%2d-%12s: %s" % (datos["dorsal"], caballo.nombre[:12], "="*datos["pasos"]))

        print( "%15s:%s" % ("Meta", " "*self.__PasosMeta + "|"))
            
    def AñadirCaballo( self, caballo):
        # REGISTRA LOS CABALLOS A PARTICIPAR EN LA CARRERA

        self.__caballos[caballo] = {"pasos": 0, "puesto": None,
                                    "dorsal": self.CantidadInscritos()+1}
        caballo.AñadirCarrera( self)

    def AvanzarTurno( self):
        # AVANZA UN TURNO EN TODOS LOS CABALLOS QUE ESTÁN EN LA CARRERA

        esFinalDeCarrera = False
        for caballo, datos in self.__caballos.items():
            caballo.Avanzar()
            datos["pasos"] = caballo.PasosCarrera
            if (not esFinalDeCarrera and
                caballo.PasosCarrera >= self.PasosMeta):
                esFinalDeCarrera = True
        return esFinalDeCarrera

    def Puestos( self):
        # CALCULA EN QUE PUESTO QUEDÓ CADA CABALLO, ASÍ TAMBIÉN GUARDA EL CABALLO GANADOR
   
        self.__clasificacion = sorted(self.__caballos.items(), key=lambda x: x[1]["pasos"], reverse=True)
        puesto = 1
        pasosAnterior = self.__clasificacion[0][1]["pasos"]
        for caballo, datos in self.__clasificacion:
           if datos["pasos"] < pasosAnterior:
                puesto += 1
                pasosAnterior = datos["pasos"]
           elif puesto == 1: self.__CaballoGanador.append( caballo)
           datos["puesto"] = puesto
            
    def PuestoFinal( self, caballo):
        # DEVUELVE EL PUESTO EN QUE QUEDÓ CADA CABALLO

        return self.__caballos[caballo]["puesto"]
        
    def Ganador( self, caballo):
        # DEVUELVE SI ES QUE UN CABALLO GANÓ LA CARRERA O NO

        return caballo in self.__CaballoGanador

    def TablaDeResultados( self):
        # MUESTRA EN LA TERMINAL EL PUESTO EN QUE QUEDÓ CADA CABALLO

        print( "\n######################## TABLA DE RESULTADOS ########################\n")
        for caballo, datos in self.__clasificacion:
            print( "%dº.- Caballo %2d | Nombre: %2s" % 
                   (datos["puesto"], datos ["dorsal"], caballo.nombre))
     
while True:
    pasos = input( "\nPASOS PARA LLEGAR A LA META: %d \n\nPresione ENTER para comenzar..." % Carrera.PASOS_META())
    try:
        carrera = Carrera( pasos)
    except ArgumentoException as e:
        print( e)
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
        print( "\nIntroduce el nombre del Caballo %d" % (i+1))
        nombre = input( "\tNombre: ")
        try:
            caballo = Caballo( nombre)
        except ArgumentoException as e:
            print( e)
            print( "Introduce el nombre del caballo correctamente")
            continue
        break
    carrera.AñadirCaballo( caballo)

print( "\nLa carrera está por comenzar ...\n")

esFinalDeCarrera = False
while not esFinalDeCarrera: 
    time.sleep(1)
    esFinalDeCarrera = carrera.AvanzarTurno()
    carrera.MostrarTurno()
    
carrera.Puestos()
carrera.TablaDeResultados()
print( "\nCaballo Ganador: \n" + str( [caballo.nombre for caballo in carrera.CaballoGanador]))