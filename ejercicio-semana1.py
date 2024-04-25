class Persona:
    def __init__(self, nombre, apellido, cedula):

        self.nombre = nombre 
        self.apellido=apellido
        self.cedula=cedula
    @staticmethod
    def mostrar(lista):
      print("nombre    apellido    cedula \n")
      for i in lista:
         print(i.nombre,"   ",i.apellido,"    ",i.cedula,"\n")
    def validar(self):
       if self.nombre.isnumeric()==True or self.apellido.isnumeric()==True or self.cedula.isnumeric()==True:
          return False
       else:
          return True


lista=[]
persona = Persona("jorge","garcia","34.987.203")
persona2=Persona("felipe","alvarado","19.094.853")
persona3=Persona("mario","perez","23.345.212")
if persona.validar() and persona2.validar() and persona3.validar():
   lista.append(persona)
   lista.append(persona2)
   lista.append(persona3)
   Persona.mostrar(lista)

else:
   print("se ingreso un dato invalido")