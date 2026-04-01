import os

from validators import validar_producto
from validators import validar_cantidad
from validators import validar_precio

# Lista global donde se almacenan los productos
def agregar_producto(inventario, nombre, cantidad, precio):
    
    # Cálculo del costo total del producto
    costo_total = cantidad * precio
    # Creamos un diccionario con los datos del producto
    producto = {
                "nombre": nombre,
                "precio": precio,
                "cantidad":cantidad,
                "costo_total":costo_total,
                }   
    # Agregamos el producto al inventario
    inventario.append(producto)
    # Retornamos la lista actualizada
    return inventario

def mostrar_inventario(inventario):
    # Encabezado de la tabla
    print(f"{'Nombre':<10} {'Precio':<10} {'Cantidad':<10}")
    print("-" * 30)
    # Recorremos cada producto en la lista
    for p in inventario:
        nombre = p["nombre"]
        precio = p["precio"]
        cantidad = p["cantidad"]
        # Mostramos cada producto formateado
        print(f"{nombre:<10} ${precio:<9} {cantidad:<10}")
def buscar_producto(inventario, nombre=None):
    # Validación del nombre (solo letras y espacios)
    #nombre = validar_producto()    # Buscamos el producto en la lista
    encontrado = False
    producto = 0 
    for producto in inventario:
        if producto["nombre"] == nombre:
            print("Producto encontrado")
            encontrado = True
            break  # salimos porque ya lo encontramos

    if encontrado == False:
        print("Producto no encontrado")
        return None

    return nombre

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    nuevo_precio = validar_precio()
    nueva_cantidad = validar_cantidad()
    for producto in inventario:
        if producto['nombre'] == nombre:
            producto['precio'] = nuevo_precio
            producto['cantidad'] = nueva_cantidad
            producto['costo_total'] = nuevo_precio * nueva_cantidad

    print(f"El inventario actual es: {inventario}")

def eliminar_producto(inventario, nombre):
    for producto in inventario:
        if producto['nombre'] == nombre:
            inventario.remove(producto)
            break
    print(f"Producto '{nombre}' eliminado. Inventario actualizado")
def estadisticas(inventario):
    if not inventario:
        print("El inventario está vacío.")
        return

    # Lambda para calcular subtotal
    subtotal = lambda p: p["precio"] * p["cantidad"]

    # Cálculos principales
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)

    # Producto más caro
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])

    # Producto con mayor stock
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    # Mostrar resultados
    print(" Estadísticas del Inventario:")
    print(f"🔹 Unidades totales: {unidades_totales}")
    print(f"🔹 Valor total del inventario: ${valor_total:.2f}")
    print(f"🔹 Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"🔹 Producto con mayor stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']} unidades)")

    # También se pueden devolver los datos si se necesitan
    return unidades_totales, valor_total, producto_mas_caro, producto_mayor_stock



def guardar_csv(inventario, ruta, incluir_header=True):
    import csv
    # Validar inventario vacío
    if not inventario:
        print(" El inventario está vacío. No hay nada que guardar.")
        return

    try:
        with open(ruta, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Encabezado
            if incluir_header:
                writer.writerow(['nombre', 'precio', 'cantidad'])

            # Datos
            for producto in inventario:
                writer.writerow([
                    producto['nombre'],
                    producto['precio'],
                    producto['cantidad']
                ])

        print(f"✅ Inventario guardado en: {ruta}")

    except PermissionError:
        print("❌ Error: No tienes permisos para escribir en ese archivo.")
    except Exception as e:
        print(f"❌ Error inesperado al guardar: {e}")

    import csv

def cargar_csv(ruta, inventario):
    import csv
    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)

            # Validar encabezado
            encabezado = next(reader, None)
            if encabezado != ['nombre', 'precio', 'cantidad']:
                print("❌ Encabezado inválido. Debe ser: nombre,precio,cantidad")
                return inventario

            # Leer filas
            for fila in reader:
                try:
                    if len(fila) != 3:
                        raise ValueError("Fila con columnas incorrectas")

                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        raise ValueError("Valores negativos no permitidos")

                    productos_cargados.append({
                        'nombre': nombre,
                        'precio': precio,
                        'cantidad': cantidad,
                        'costo_total': precio * cantidad
                    })

                except (ValueError, IndexError):
                    filas_invalidas += 1

    except FileNotFoundError:
        print("❌ Error: El archivo no existe.")
        return inventario
    except UnicodeDecodeError:
        print("❌ Error: Problema de codificación del archivo.")
        return inventario
        print(f"❌ Error inesperado: {e}")
        return inventario

    # 🔹 Solo preguntar si inventario actual NO está vacío
    if inventario:
        decision = input("¿Sobrescribir inventario actual? (S/N): ").strip().upper()
    else:
        decision = 'S'  # si inventario está vacío, automáticamente reemplaza

    if decision == 'S':
        inventario = productos_cargados
        accion = "reemplazo"
    else:
    # 🔥 FUSIÓN (por nombre)
        inventario = inventario.copy()

        for nuevo in productos_cargados:
            encontrado = False

            for producto in inventario:
                if producto['nombre'] == nuevo['nombre']:
                    # Sumar cantidad
                    producto['cantidad'] += nuevo['cantidad']

                    # Actualizar precio si es diferente
                    if producto['precio'] != nuevo['precio']:
                        producto['precio'] = nuevo['precio']

                    # Recalcular total
                    producto['costo_total'] = producto['precio'] * producto['cantidad']

                    encontrado = True
                    break

            if not encontrado:
                inventario.append(nuevo)

        accion = "fusión"

    # 🔹 Resumen final
    #print("\n📊 Resumen de carga:")
    #print(f"✔ Productos cargados: {len(productos_cargados)}")
    #print(f"⚠ Filas inválidas omitidas: {filas_invalidas}")
    #print(f"🔄 Acción realizada: {accion}")
    accion = accion if 'accion' in locals() else "ninguna"
    # Retornamos inventario y los datos del resumen
    return inventario, len(productos_cargados), filas_invalidas, accion

   