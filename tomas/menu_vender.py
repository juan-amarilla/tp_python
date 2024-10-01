from validates import validar_producto_vender, validar_cantidad_producto

def vender(inventario:list)->list:
    '''
        Realiza la venta de uno o más productos, mostrando el valor final de la compra y descontando el producto del inventario.

        Args:
        inventario (list)

        Returns:
        inventario (list)
    '''
    
    continuar = "s"
    total_a_pagar = 0
    largo_lista= len(inventario)
    
    while continuar == "s":
        print("\nProductos para vender: ")

        # Imprimimos el inventario con el número del producto a ingresar
        for i in range(len(inventario)): 
            nombre_producto = inventario[i][0]
            precio_producto = inventario[i][2]
            print(f"[{i+1}] {nombre_producto} | ${precio_producto}")

        #El usuario ingresa los datos
        print("---------------------------")
        numero_producto = input("Ingrese el número del producto a vender: ")
        numero_producto = validar_producto_vender(numero_producto, largo_lista)

        cantidad = input("Ingrese la cantidad: ")
        cantidad_disponible = inventario[numero_producto-1][1]
        cantidad = validar_cantidad_producto(cantidad, cantidad_disponible)
        
        #Descontamos el producto del inventario y calculamos el total a pagar
        inventario[numero_producto-1][1] = cantidad_disponible - cantidad
        total_a_pagar += inventario[numero_producto-1][2] * cantidad

        continuar = input("¿Desea vender otro producto? s / n: ").lower()

    mensaje_final = f'''¡OPERACIÓN EXITOSA!
    Total a pagar: ${total_a_pagar}
'''
    print(mensaje_final)

    return inventario


