//en este archivo va el programa
productos = []
precios = []

def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    
    productos.append(nombre)
    precios.append(precio)
    
    print("Producto registrado correctamente\n")
//deberia ir primero el menu
def menu():
    while True:
        print("===== TIENDA ESCOLAR =====")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Calcular total de compra")
        print("4. Salir")
        
    print("Producto registrado correctamente\n")
    
     
