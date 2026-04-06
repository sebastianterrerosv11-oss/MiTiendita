
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