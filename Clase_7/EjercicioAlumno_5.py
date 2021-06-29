class Alumno():
    

    def __init__(self):
        self.nombre = input('Nombre del Alumno: ')
        self.apellido = input('Apellido del Alumno: ')
        self.notaFinal = float(input('Nota Final del Alumno: '))

    def __str__(self):
        mensaje = 'El Alumno '+self.apellido +', '+self.nombre +' con Nota Final '+str(self.notaFinal)
        if (self.notaFinal >= 7):
            mensaje += ' \"Promoción\" 🙂'
        elif(self.notaFinal >= 4 and self.notaFinal < 7):
            mensaje += ' \"Final\" 😭 '
        else:
            mensaje += ' \"Recursa\" 💀'
        return mensaje

alumno = Alumno()

print(alumno)