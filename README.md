
# DIAGRAMA DE FLUJO
![image alt](https://github.com/guillermoleano/RIWI_ENTREGABLE/blob/cd1a7cb7e00823d7b78bc85b83291f59f9247a56/DIAGRAMA%20DE%20FLUJO.jpg)



### 🚀 Cómo clonar y ejecutar el proyecto

### 1. Clonar el repositorio
    
    1. Abre **Visual Studio Code**.
    2. Abre la **terminal** (Terminal → New Terminal).
    3. Copia y ejecuta el siguiente comando para clonar el repositorio:
       ```bash
    git clone https://github.com/guillermoleano/RIWI_ENTREGABLE.git ```

### 2. Entrar a la carpeta del proyecto

Después de clonar el repositorio, accede a la carpeta del proyecto con el siguiente comando:

cd RIWI_ENTREGABLE

### 3. Ejecutar el proyecto
Para ejecutar el programa, usa el siguiente comando en la terminal:
```bash
python inventario.py ```

***El programa se ejecutará en la terminal y te pedirá ingresar:
Nombre del producto
Precio
Cantidad***



# EXPLICACION DEL PROYECTO: REGISTRO DE UN PRODUCTO EN UN INVENTARIO

1. Aqui se definen las variables para el nombre del producto, la cantidad y el precio, se asignan los tipos de datos correspondientes a cada variable. 

```python
nombre = str
cantidad = int
precio = float
```
2. Aqui atraves de un ciclo while se valida que el nombre del producto solo contenga letras y espacios, si el nombre es valido se sale del ciclo, de lo contrario se muestra un mensaje de error y se vuelve a pedir el nombre


```python
while True: 
    nombre = input("Ingrese nombre del producto: ")  
    if nombre.replace(" ", "").isalpha(): 
        break 
    else: 
        print("Debe ingresar un nombre valido.") 
```

3. Aqui se valida que la cantidad ingresada sea un numero, si es valido se sale del ciclo, de lo contrario se 
#muestra un mensaje de error y se vuelve a pedir el precio. Por medio del try except se maneja la excepcion 
de que el usuario ingrese un valor no numerico, si el valor es valido se sale del ciclo, de lo contrario se muestra un mensaje de error y se vuelve a pedir el precio.  


```python
while True:
    try:
        precio = float(input("Ingrese precio: "))
        break
    except ValueError:
        print("Debe ingresar un numero valido.")

```
4. Aqui se valida que la cantidad ingresada sea un numero entero, si es valido se sale del ciclo, de lo contrario se muestra


```python
while True: 
    cantidad = input("Ingrese cantidad: ")
    if cantidad.isdigit():
        cantidad = int(cantidad) #Convertir la cantidad a entero
        break
    else:
        print("Debe ingresar un numero valido.")
```


5. Aqui se calcula el costo total multiplicando el precio por la cantidad y se muestra un mensaje con el nombre del producto, el precio, la cantidad y el costo total.

```python
costo_total = precio * cantidad
print(f"Producto: {nombre} / Precio: {precio} / Cantidad: {cantidad} / Total: {costo_total}") 
```


***Explicacion general del codigo: Este codigo es un programa de inventario que permite al usuario ingresar 
el nombre de un producto, su precio y la cantidad disponible. El programa valida que el nombre del producto solo 
contenga letras y espacios, que el precio sea un numero valido y que la cantidad sea un numero entero. Luego, calcula 
el costo total multiplicando el precio por la cantidad y muestra un mensaje con los detalles del producto y el costo total.***








