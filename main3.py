import numpy as np
import cProfile, pstats, io

def profile(fnc):
    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval
    return inner


@profile
def main(inventario,ventasxDia):

    print('=============================')
    print('Menú Gestión de inventario')
    print('=============================')
    print('1- Agregar producto al inventario')
    print('2- Eliminar producto')
    print('3- Actualizar inventario')
    print('4- Buscar producto en el inventario')
    print('5- Imprimir reporte de inventario')
    print('6- Ventas x dia')
    print('7- Vender producto')
    print('10- Salir')
    print("")

    opcion = int(input("Selecciona una opción: "))

    print("")
  
    if opcion == 1:
        agregarInventario(inventario,ventasxDia)
    elif opcion == 2:
        eliminarInventario(inventario,ventasxDia)
    elif opcion == 3:
        actualizarInventario(inventario,ventasxDia)
    elif opcion == 4:
        buscarInventario(inventario,ventasxDia)
    elif opcion == 5:
        imprimirInventario(inventario,ventasxDia)
    elif opcion ==6:
        registrarVentaxDia(inventario,ventasxDia)
    print("")

def agregarInventario(inventario,ventasxDia):
    nombre_producto = input("Nombre del producto: ")
    cantidad_producto = int(input("Cantidad del producto: "))
    #Metodo append permite apilar un nuevo elemento en la pila
    inventario.append([nombre_producto,cantidad_producto])
    print(inventario)
    main(inventario,ventasxDia)
    
def eliminarInventario(inventario,ventasxDia):
  stack_temporal = []
  nombre_producto = input("Ingrese el nombre del producto a remover: ")
  borro = False
  while(len(inventario)>0):
    #pop permite desapilar un elemento de la pila
    elemento = inventario.pop()
    if(elemento[0] != str(nombre_producto)):
      stack_temporal.append(elemento)
    else:
      borro=True
      print("El producto "+ nombre_producto+ " se eliminó correctamente")
  if(borro==False):
    print("No se encontró el producto con nombre "+ nombre_producto)
  
  main(stack_temporal,ventasxDia)

def actualizarInventario(inventario,ventasxDia):

  nombre_producto = input('Ingresa el nombre del producto a actualizar: ')
  cantidad_producto = int(input("Cuanto es la nueva cantidad: "))

  stack_temporal= []
  actualizo = False
  while(len(inventario)>0):
    elemento = inventario.pop()
    if(elemento[0] != str(nombre_producto)):
      stack_temporal.append(elemento)
    #Cuando el nombre ingresado coincide con el del       producto que se esta desapilando o evaluando entra el else
    else:
      actualizo=True
      stack_temporal.append([nombre_producto,cantidad_producto])
      print("El producto "+ nombre_producto+ " se actualizó correctamente")
  if(actualizo==False):
    print("No se encontró el producto con nombre "+ nombre_producto)
  main(stack_temporal,ventasxDia)

def buscarInventario(
  inventario,ventasxDia):
    stack_temporal=inventario.copy()
    nombre_producto = input('Ingresa el nombre del producto a buscar: ')
    encontro = False
    while(len(stack_temporal)>0):
      elemento = stack_temporal.pop()
      if(elemento[0] == str(nombre_producto)):
        encontro=True
        print("Nombre: " + elemento[0] + " Cantidad: " + str(elemento[1]))       
    if(encontro == False):
      print("No existe un objeto con el nombre "+ nombre_producto)
      
    main(inventario,ventasxDia)
        
def imprimirInventario(inventario,ventasxDia):
  stack_temporal = inventario.copy()
  while(len(stack_temporal)>0):
     elemento = stack_temporal.pop()
     print("Nombre del producto: "+ elemento[0]+" - Cantidad: "+ str(elemento[1]))
  main(inventario,ventasxDia)

def registrarVentaxDia(inventario, ventasxDia):
  #inicializar el arreglo bidimensional (matriz)
  if(ventasxDia[0][0]==''):
    cantidadDias = int(input("Ingresa los dias del mes:"))
    cantidadDiasAux = cantidadDias
    for i in range (0,len(ventasxDia)):
      for j in range (0,len(ventasxDia[0])):
        if(cantidadDiasAux>0):
          dia =(cantidadDias+1)-cantidadDiasAux
          ventasxDia[i][j]= str(dia)+"- 0"
        cantidadDiasAux = cantidadDiasAux-1
  print(ventasxDia)
  diaAIngresar = int(input("Ingresa el dia que quieres registrar ventas:"))

  indice = 0
  for i in range (0,len(ventasxDia)):
      for j in range (0,len(ventasxDia[0])):
        if(diaAIngresar-1 == indice):
          ventasDia = int(input("Ingresa las ventas para este dia: "))
          ventasxDia[i][j] = str(diaAIngresar) + "- "+str(ventasDia)
        indice = indice+1

  print(ventasxDia)

  main(inventario,ventasxDia)


  
main([],np.empty((5,7),dtype='U25'))
