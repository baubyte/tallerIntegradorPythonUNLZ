
class Alumno():
    nombre = None
    apellido = None
    notas = []
    promedio = None
    estado = None

    def __init__(self):
        self.nombre = input('Nombre del Alumno: ')
        self.apellido = input('Apellido del Alumno: ')
        while True:
            nota = int(input('Ingrese una Nota: '))
            if nota == 0:
                self.promedio = sum(self.notas) / len(self.notas)
                break
            elif nota >= 1 and  nota <=10:
                self.notas.append(nota)
            else:
                print("Nota Invalidad Intente de Nuevo.")

    def __str__(self):
        if (self.promedio >= 7):
            self.estado = ' \"Promociona\"'
        elif(self.promedio >= 4 and self.promedio < 7):
            self.estado = ' \"Final\"'
        else:
            self.estado = ' \"Recursa\"'
        return f"""
        - Nombre {self.nombre} 
        - Apellido {self.apellido}
        - Promedio {self.promedio}
        - Estado {self.estado}
        """


alumno = Alumno()
print(alumno)