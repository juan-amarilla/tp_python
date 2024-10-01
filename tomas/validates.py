

def validar_se_ingrese_numero(valor_input):
    while valor_input == "" or not valor_input.isdigit() or valor_input.startswith("-") or "." in valor_input:
        valor_input = input("Debe ingresar un número valido. Vuelva a intentar: ")
    valor_input = int(valor_input)
    return valor_input


def validar_producto_vender(producto, largo_lista):

    #validamos que no se ingrese un string vacio, que el número no sea negativo y que el número(str) ingresado sea un número.
    producto = validar_se_ingrese_numero(producto)

    #validamos que el número este dentro del rango de la lista, si la lista tiene 10 posiciones el número no puede valer 11
    while producto > largo_lista:
        producto = input("Número fuera de rango. Vuelva a intentar: ")
        #volvemos a hacer la primer validación
        validar_se_ingrese_numero(producto)
        producto = int(producto)

    return producto


def validar_cantidad_producto(cantidad, cantidad_disponible):

    cantidad = validar_se_ingrese_numero(cantidad)  

    while cantidad_disponible - cantidad < 0:
        print("¡Cantidad no disponible!")
        print(f"Stock disponible: {cantidad_disponible}")
        
        cantidad = input("Ingrese una cantidad valida: ")
        cantidad = validar_se_ingrese_numero(cantidad)
    
    return cantidad
