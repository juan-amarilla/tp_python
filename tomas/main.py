from menu_vender import vender
from menu_mostrar_inventario import mostrar

continuar = True
inventario = [
    ["Chupetin Sable de luz", 50, 200],
    ["Agua La Fuerza", 35, 3200],
    ["Gomitas Holocubo", 25, 990],
    ["Barrita de Cereal Wookiee", 48, 2500],
    ["Galletitas R2D2", 20, 15800],
]

print("Quiosco Yoda's Snack")
print("---------------------")

menu = ''' 
    MENU:
    [1] Agregar producto al inventario.
    [2] Realizar una venta.
    [3] Mostrar productos disponibles.
    [4] Salir del sistema.

    Elegir una opcion del menu: '''


while continuar:

    eleccion_menu = input(menu)

    match eleccion_menu:

        case "1":
            pass
        case "2":
            vender(inventario)
        case "3":
            mostrar(inventario)
        case "4":
            print("¡Gracias por usar nuestro servicio!")
            continuar = False
        
