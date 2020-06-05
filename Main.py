from Menu import Menu
if __name__ == '__main__':
    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Crear el arreglo
              2 Registrar horas de un empleado
              3 Total de una tarea
              4 Consultar cuales empleados obtendrían ayuda
              5 Revisar sueldo total de los empleados""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op)
        salir = op == 0