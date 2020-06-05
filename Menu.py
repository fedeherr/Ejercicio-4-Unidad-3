from Colección import Coleccion
class Menu:
    __switcher=None
    __manejoemp = None
    def __init__(self):
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        a = int(input("Ingrese la cantidad de componentes que quiera que tenga el arreglo: "))
        self.__manejoemp=Coleccion(a)
        b = self.__manejoemp.manejarEmpleadosCon()
        if (b == 1):
            b = self.__manejoemp.manejarEmpleadosExt()
            if (b == 1):
                b = self.__manejoemp.manejarEmpleadosPla()
                
    def opcion2(self):
        dnie = int(input("Ingrese el DNI del empleado: "))
        hor = int(input("Ingrese las horas trabajadas hoy: "))
        self.__manejoemp.nuevaHoras(dnie, hor)
        
    def opcion3(self):
        tar = input("Ingrese la tarea a buscar: ")
        self.__manejoemp.totalTarea(tar)
    def opcion4(self):
        self.__manejoemp.ayudaSueldo()

    def opcion5(self):
        self.__manejoemp.mostrarSueldo()