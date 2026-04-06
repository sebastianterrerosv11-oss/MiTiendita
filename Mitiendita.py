
productos = []
precios = []
 
 
def registrar_producto():
    nombre = input("Ingrese el nombre del producto: ").strip()
    if not nombre:
        print("El nombre no puede estar vacío.\n")
        return
 
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: $"))
            if precio < 0:
                print("El precio no puede ser negativo.")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido.")
 
    productos.append(nombre)
    precios.append(precio)
    print(f"✓ Producto '{nombre}' registrado correctamente.\n")

def mostrar_productos():
    if not productos:
        print("No hay productos registrados.\n")
        return
 
    print("\n{:<5} {:<25} {:>10}".format("No.", "Producto", "Precio"))
    print("-" * 42)
    for i, (nombre, precio) in enumerate(zip(productos, precios), 1):
        print("{:<5} {:<25} {:>10,.2f}".format(i, nombre, precio))
    print()   
def hacer_compra():
    if not productos:
        print("No hay productos disponibles. Registre productos primero.\n")
        return
 
    carrito = []      # lista de (nombre, precio, cantidad)
    print("\n===== REALIZANDO COMPRA =====")
 
    while True:
        mostrar_productos()
        print("0. Terminar compra")
        opcion = input("Seleccione el número del producto (0 para terminar): ").strip()
 
        if opcion == "0":
            break
 
        if not opcion.isdigit() or not (1 <= int(opcion) <= len(productos)):
            print("Opción inválida. Intente de nuevo.\n")
            continue
 
        idx = int(opcion) - 1
        while True:
            try:
                cantidad = int(input(f"¿Cuántas unidades de '{productos[idx]}'? "))
                if cantidad <= 0:
                    print("La cantidad debe ser mayor a 0.")
                    continue
                break
            except ValueError:
                print("Ingrese un número entero válido.")
 
        carrito.append((productos[idx], precios[idx], cantidad))
        print(f"✓ {cantidad}x '{productos[idx]}' agregado al carrito.\n")
 
    if not carrito:
        print("No agregó ningún producto al carrito.\n")
        return
 
    imprimir_factura(carrito)    