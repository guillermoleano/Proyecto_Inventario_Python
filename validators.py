def validar_producto():
    nombre = str
    # Validación del nombre (solo letras y espacios)
    while True: 
        nombre = input("Ingrese nombre del producto: ")  
        if nombre.replace(" ", "").isalpha(): 
            break 
        else: 
            print("Debe ingresar un nombre valido.") 
    return nombre
def validar_cantidad():    
    cantidad = int
    # Validación de la cantidad (solo números enteros)    
    while True: 
        cantidad = input("Ingrese cantidad: ")
        if cantidad.isdigit():
            cantidad = int(cantidad) #Convertir la cantidad a entero
            break
        else:
            print("Debe ingresar un numero valido.")
    return cantidad
def validar_precio(): 
    precio = float
    # Validación del precio (número decimal)    
    while True:
        try:
            precio = float(input("Ingrese precio: "))
            break
        except ValueError:
            print("Debe ingresar un numero valido.")
    return precio