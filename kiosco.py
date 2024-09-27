import ingreso_validado as ingre
import kiosco_validaciones as valida

def mostrar_inventario(inventario: list) -> int:
    """
    Mostrara el inventario

    Args:
    inventario(list)

    return:
    1 si salio exitoso o 0 si salio mal
    """

    retorno = 0;

    for i in range(len(inventario)):
        print(inventario[i]);

        if i + 1 == len(inventario):
            retorno = 1;

    return retorno;

def agregar(inventario: list) -> int:
    """
    Agrega un producto nuevo al inventario

    Args:
    inventario(list)

    return:
    1 si salio exitoso o 0 si salio mal
    """

    lista = [];
    estado = 0;
    opcion = "";

    while opcion != "salir":

        nombre = ingre.ingresar_y_validar_string("Ingrese el nombre del producto nuevo: ");
        nombre = valida.validar_nombre(nombre);

        cantidad = ingre.ingresar_y_validar_entero("Ingrese una cantidad para el producto nuevo: ");
        cantidad = valida.validar_cantidad(cantidad);

        precio = ingre.ingresar_y_validar_entero("Ingrese un precio por unidad al producto nuevo: ");
        precio = valida.validar_precio(precio);

        lista.append(nombre);
        lista.append(cantidad);
        lista.append(precio);

        inventario.append(lista);
        lista = [];

        opcion = ingre.ingresar_y_validar_string("Escriba salir si termino de agregar productos: ");
    
    estado = mostrar_inventario(inventario);

    return estado;