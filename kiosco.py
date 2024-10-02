import ingreso_validado as ingre
import kiosco_validaciones as valida

def mensaje_estado(numero_estado: int) -> str:
    """
    Tomara el mensaje exitoso o no exitoso

    Args:
    numero_estado(int)

    return:
    Retornara el mensaje
    """

    if numero_estado == 1:
        mensaje = "Salio exitoso. ";
    
    else:
        mensaje = "No salio exitoso. ";

    return mensaje;

def mostrar_inventario(inventario: list) -> int:
    """
    Mostrara el inventario

    Args:
    inventario(list)

    return:
    Retorna 1 si salio bien o 0 si salio mal
    """

    retorno = 0;

    
    print("-------------------------------------")
    print("\nINVENTARIO")

    for i in range(len(inventario)): 

        print("-------------------------------------")
        print(f"[{i+1}] Nombre: {inventario[i][0]} | Stock: {inventario[i][1]} | Precio: ${inventario[i][2]}")

        if i == len(inventario) - 1:

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


def venta(inventario: list) -> int:
    '''
    Realiza la venta de uno o más productos, mostrando el valor final de la compra y 
    descontando el producto del inventario.

    Args:
    inventario (list)

    Returns:
    1 si salio bien o 0 si salio mal
    '''
    
    continuar = "s";
    total_a_pagar = 0;
    largo_lista = len(inventario);
    estado = 0;
    
    while continuar == "s":

        print("\nProductos para vender: ")

        for i in range(len(inventario)): 
            nombre_producto = inventario[i][0];
            precio_producto = inventario[i][2];
            print(f"[{i+1}] {nombre_producto} | ${precio_producto}");

        print("---------------------------");

        numero_producto = ingre.ingresar_y_validar_entero("Debe ingresar un número: ");
        numero_producto = valida.validar_producto_vender(numero_producto, largo_lista);

        cantidad = ingre.ingresar_y_validar_entero("Debe ingresar una cantidad: ");
        cantidad_disponible = inventario[numero_producto-1][1];
        cantidad = valida.validar_cantidad_producto(cantidad, cantidad_disponible);
        
        inventario[numero_producto-1][1] = cantidad_disponible - cantidad;
        total_a_pagar += inventario[numero_producto-1][2] * cantidad;

        continuar = input("¿Desea vender otro producto? s / n: ").lower();
    
        estado = 1;

    mensaje_final = f'''¡OPERACIÓN EXITOSA!
    Total a pagar: ${total_a_pagar}
    '''

    print(mensaje_final);

    return estado;