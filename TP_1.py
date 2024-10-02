import kiosco as kios
from ingreso_validado import ingresar_y_validar_entero

inventario = [
    ["Chupetin sable de luz", 50, 200],
    ["Agua de la fuerza", 35, 3200],
    ["Gomitas holocubo", 25, 990],
    ["Barrita de cereal wookiee", 40, 2500],
    ["Galletitas R2D2", 20, 15800],
]

opcion = 0;

print("Quiosco Yoda's Snack");
print("---------------------");

mensaje = """
1-Agregar producto al inventario
2-Realizar una venta
3-Mostrar productos disponibles
4-Salir del sistema\n""";

while opcion != 4:

   opcion = ingresar_y_validar_entero(mensaje);

   match opcion:

        case 1:
            estado = kios.agregar(inventario);
            mensaje_estado = kios.mensaje_estado(estado);
            print(mensaje_estado);
        
        case 2:
            estado = kios.venta(inventario);
            mensaje_estado = kios.mensaje_estado(estado);
            print(mensaje_estado);
        
        case 3:
            estado = kios.mostrar_inventario(inventario);
            mensaje_estado = kios.mensaje_estado(estado);
            print(mensaje_estado);
        
        case 4:
            print("Se salio exitosamente el programa gracias por usarlo. ");
        
        case _:
            print("No");