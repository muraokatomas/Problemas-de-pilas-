from auxiliar1 import es_bisiesto
from auxiliar2 import cant_dias_mes

def fecha_valida(dia, mes, año):
    """Recibe por parametro tres numeros que representan el dia,mes y año,
     y devuelve True si es una fecha valida o False si no lo es"""
     
    if mes < 1 or mes > 12:
        return False
    elif dia>=1 and dia<=cant_dias_mes(mes,año):
        return True
    else:
        return False


    
