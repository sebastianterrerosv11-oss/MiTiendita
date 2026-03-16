//en este archivo va el programa
productos = []
precios = []

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    
    productos.append(nombre)
    precios.append(precio)
    
    print("Producto registrado correctamente\n")


