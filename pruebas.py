import unittest

def agregarInventarioTesteo(inventario,ventasxDia):
    nombre_producto = input("Nombre del producto: ")
    cantidad_producto = int(input("Cantidad del producto: "))
    
    inventario.append([nombre_producto,cantidad_producto])
    print(inventario)
    return inventario
    
def eliminarInventarioTesteo(inventario,ventasxDia):
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
    
  return stack_temporal

def actualizarInventarioTesteo(inventario,ventasxDia):

  nombre_producto = input('Ingresa el nombre del producto a actualizar: ')
  cantidad_producto = int(input("Cuanto es la nueva cantidad: "))

  stack_temporal= []
  actualizo = False
  while(len(inventario)>0):
    elemento = inventario.pop()
    if(elemento[0] != str(nombre_producto)):
      stack_temporal.append(elemento)
    
    else:
      actualizo=True
      stack_temporal.append([nombre_producto,cantidad_producto])
  return stack_temporal

def buscarInventarioTesteo(
  inventario,ventasxDia):
    stack_temporal=inventario.copy()
    nombre_producto = input('Ingresa el nombre del producto a buscar: ')
    encontro = False
    while(len(stack_temporal)>0):
      elemento = stack_temporal.pop()
      if(elemento[0] == str(nombre_producto)):
        encontro=True
        return elemento
    return None

class TestSum(unittest.TestCase):

  def test_agregar_producto(self):
    print("--- test_agregar_producto --- ")
    inventario = []
    agregarInventarioTesteo(inventario,None)
    self.assertEqual(1, len(inventario), "Se esperaba 1")
    print("")

  def test_eliminar_producto(self):
    print("--- test_eliminar_producto --- ")
    inventario = [['Manzana',100],['Banano',200]]
    inventario = eliminarInventarioTesteo(inventario, None)
    self.assertEqual(100,inventario[0][1],"Se esperaban 100 Manzanas")
    print("")

  def test_actualizar_producto(self):
    print("--- test_actualizar_producto --- ")
    inventario = [['Arroz',100]]
    inventario = actualizarInventarioTesteo(inventario, None)
    self.assertNotEqual(100,inventario[0][1],"Se esperaban manazanas diferentes a 100")
    print("")

  def test_buscar_producto(self):
    print("--- test_buscar_producto --- ")
    inventario = [['Arroz',100],['Sandia',200],['Manzana',50]]
    elemento = buscarInventarioTesteo(inventario, None)
    self.assertIsNotNone(elemento,"Se esperaba un elemento")
    print("")
    
unittest.main()
