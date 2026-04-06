
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
 