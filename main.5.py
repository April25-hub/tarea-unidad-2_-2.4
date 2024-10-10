print(" ")
print("Arzaba Diaz April 3W 1173")
def total_factura(cantidad_sin_iva, porcentaje_iva):
    """
    esta funcion calcula el total de una factura luego de aplicar el IVA
    
    args:
    cantidad_sin_iva (float): Monto de la factura sin IVA
    porcentaje_iva (float): Porcentaje de IVA a aplicar (en porcentaje, no en decimal)

    returns:
    float: total de la factura incluyendo el IVA
    """
    # Calculamos el monto del IVA
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    # Calculamos el total de la factura
    total = cantidad_sin_iva + iva
    return total

# ejemplo de uso
cantidad = 100  # monto sin IVA
porcentaje = 21  # porcentaje de IVA
resultado = total_factura(cantidad, porcentaje)
print(resultado)  # salida: 121.0
