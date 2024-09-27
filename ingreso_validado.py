def ingresar_y_validar_entero(mensaje: str) -> int:
    """
    Ingresa un numero entero validado.

    args:
    mensaje(str)

    returns:
    retorna el numero entero.
    """
    estado = 0;

    while estado == 0:
       
       try:
         numero = int(input(mensaje));
         estado = 1;
         break;
    
       except:
        print("Error: ");
        estado = 0;

    return numero;

def ingresar_y_validar_string(mensaje: str) -> str:
    """
    Ingresa un string validado.

    args:
    mensaje(str)

    returns:
    retorna el string.
    """

    estado = 0;
    error = 1;

    while estado == 0:

        if error == 1:
            string = input(mensaje);
            lenght = len(string);
        
        else:
           print("Error: ");
           string = input(mensaje);
           lenght = len(string);
           
    
        for i in range(lenght):

            if i + 1 == lenght:
               estado = 1;
        
            if string[i].isalpha():
                continue;
    
            elif string[i].isspace():
                continue;
            
            elif string[i].isdigit():
                continue;

            else:
                error = 0;
                estado = 0;
                break;             

    return string;