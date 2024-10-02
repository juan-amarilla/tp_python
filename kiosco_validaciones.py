import ingreso_validado as ingre

def validar_nombre(producto_nombre: str) -> str:
    """
    Valida el nombre del producto

    Args:
    producto_nombre(str)

    Return:
    Retorna el nombre validado
    """

    while len(producto_nombre) <= 3:
        producto_nombre = ingre.ingresar_y_validar_string("Cantidad de caracteres insuficientes: ingrese el nombre que tenga mas de 3 caracteres: ");

    return producto_nombre;

def validar_cantidad(cantidad: int) -> int:
    """
    Valida la cantidad del producto

    Args:
    cantidad(int)

    Return:
    Retorna la cantidad validada
    """

    while cantidad < 20:
        cantidad = ingre.ingresar_y_validar_entero("Ingrese una cantidad mayor e igual a 20 para el producto nuevo: ");

    return cantidad;

def validar_precio(precio: int) -> int:
    """
    Valida el precio del producto

    Args:
    precio(int)

    Return:
    Retorna el precio validado
    """

    while precio < 200:
        precio = ingre.ingresar_y_validar_entero("Ingrese un precio mayor e igual a 200 para el producto nuevo: ");

    return precio;

def validar_producto_vender(producto: int, largo_lista: int) -> int:
    """
    Valida el producto a la venta

    Args:
    producto(int)
    largo_lista(int)

    return:
    Retorna el producto a la venta
    """
    
    while producto > largo_lista or producto < 1:
        producto = ingre.ingresar_y_validar_entero("Debe ingresar un número: ");

    return producto


def validar_cantidad_producto(cantidad: int, cantidad_disponible: int) -> int:
    """
    Valida el stock

    Args:
    cantidad(int)
    cantidad_disponible(int)

    return:
    Retorna el producto a la venta
    """

    while cantidad > cantidad_disponible or cantidad < 0:

       print("¡Cantidad no disponible!");
       print(f"Stock disponible: {cantidad_disponible}");
    
       cantidad = ingre.ingresar_y_validar_entero("Ingrese una cantidad valida: ");
    
    return cantidad;