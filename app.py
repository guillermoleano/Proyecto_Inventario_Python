# Importamos las funciones desde utils.py
from servicios import agregar_producto
from servicios import mostrar_inventario
from servicios import buscar_producto
from servicios import actualizar_producto
from servicios import eliminar_producto
from servicios import estadisticas
from servicios import guardar_csv
from servicios import cargar_csv
from validators import validar_producto
from validators import validar_cantidad
from validators import validar_precio

import os
inventario = []
# Lista principal del inventario
# Función para limpiar la consola (Windows / Linux / Mac)
def clear():
    os.system("cls" if os.name == "nt" else "clear")

ruta = os.path.abspath('inventario.csv')
inventario, productos_cargados, filas_invalidas, accion = cargar_csv(ruta, [])

while True:
    # Menú de opciones
    opcion = input("""Seleccione una de las siguientes opciones:
    1. Agregar producto
    2. Mostrar inventario
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Calcular estadisticas
    7. Guardar CSV
    8. Cargar CSV
    9. Salir
    Opción: """)

    # Agregar producto
    if opcion == "1":
        #Pedimos los datos del producto por medio de validators.py
        nombre = validar_producto() # Validación del nombre (solo letras y espacios)
        cantidad = validar_cantidad() # Validación de la cantidad (solo números enteros)
        precio = validar_precio() # Validación del precio (número decimal)
        clear()
        inventario = agregar_producto(inventario, nombre, cantidad, precio)
        print("Producto agregado correctamente.")
    # Opción 2: Mostrar inventario
    elif opcion == "2":
        clear()
        if not inventario:  # validar si está vacío
            print("El inventario está vacío")
        else:
    # Mostramos los productos    
            mostrar_inventario(inventario)  # mostrar la lista real
            
    elif opcion == "3":
        clear()
        nombre = validar_producto()    # Buscamos el producto en la lista
        buscar_producto(inventario, nombre)
    elif opcion == "4":
        clear()
        nombre_a_actualizar = validar_producto()
        nombre = buscar_producto(inventario, nombre_a_actualizar)
        actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
    elif opcion == "5":
        clear()
        nombre = buscar_producto(inventario)
        eliminar_producto(inventario, nombre)
    elif opcion == "6":
        clear()
        estadisticas(inventario)
    elif opcion == "7":
        clear()
        if not inventario:  # validar si está vacío
            print("El inventario está vacío")
        else:
            guardar_csv(inventario, ruta, incluir_header=True)
    elif opcion == "8":
        clear()
        print("Cargando inventario desde CSV...")
        inventario, productos_cargados, filas_invalidas, accion = cargar_csv(ruta, inventario)
    
        # Imprimir resumen solo después de cargar
        print("\n📊 Resumen de carga:")
        print(f"✔ Productos cargados: {productos_cargados}")
        print(f"⚠ Filas inválidas omitidas: {filas_invalidas}")
        print(f"🔄 Acción realizada: {accion}")
    elif opcion == "9":
        clear()
        break
    else:
        clear()
        print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")