#Clase Auto
class Auto:
    color = 'Sin Datos'
    puertas = 'Sin Datos'
    combustible = 'Sin Datos'

    #Metodo o accion de la clase que puede ser ejecutado por 
    #el objeto.
    #El primer argumento obligatorio hace referencia al objeto
    def pintar(self, pintura):
        self.color = pintura

#Instancia de la clase
#Objetos
vw = Auto()
ford = Auto()

#Mostramos el Atributo color del Objeto vw
print('Un solo atributo -> Color -> VW')
print(vw.color)

#Ver atributos Objeto VW
print()
print('Todos los Atributos de -> VW')
print('VW Color:',vw.color)
print('VW Puertas:',vw.puertas)
print('VW Combustible:',vw.combustible)
print('Asignamos un color -> VW y lo mostramos')
vw.pintar('verde')
print('VW Color:',vw.color)
print()
#Mostramos el Atributo color del Objeto FORD
print('Un solo atributo -> Color -> FORD')
print(ford.color)