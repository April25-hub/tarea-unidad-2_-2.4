# tarea-unidad-2_-2.4
Arzaba Diaz April 1174 3W

print(" ")

print("Arzaba Diaz April 3W 1173")

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva):

    """
    esta funcion calcula el total de una factura aplicando el IVA.

    
    
    args:
    
    cantidad_sin_iva (float): La cantidad sin IVA.
    
    porcentaje_iva (float): El porcentaje de IVA a aplicar.

    
    
    returns:
    
    float: el total de la factura incluyendo el IVA.
    
    """
    
    #esta line calculara el monto del IVA
    
    monto_iva = cantidad_sin_iva * (porcentaje_iva / 100)

    
    
    #esta linea calculara el total de la factura
    
    total_factura = cantidad_sin_iva + monto_iva

    
    
    return total_factura



#esta linea solicitara al usuario la cantidad sin IVA

cantidad_sin_iva = float(input("Ingrese la cantidad sin IVA: "))



#esta linea solicitara al usuario el porcentaje de IVA

porcentaje_iva = float(input("Ingrese el porcentaje de IVA: "))



#esta linea calculara el total de la factura

total = calcular_total_factura(cantidad_sin_iva, porcentaje_iva)



#esta linea mostrara el resultado

print(f"El total de la factura es: {total:.2f}")
![image](https://github.com/user-attachments/assets/a8da32ae-1c9f-40eb-8149-d287c2b44304)
![image](https://github.com/user-attachments/assets/5f3b3913-7745-404f-a560-671e9e6443bf)





