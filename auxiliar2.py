from auxiliar1 import es_bisiesto

def  cant_dias_mes(mes , año):
    if  mes == 3  or mes ==1  or mes ==5 or  mes == 7 or mes ==8 or mes == 10 or mes == 12:
        return 31
    elif mes== 4 or mes == 6 or mes== 9 or mes==11:
        return 30
    elif es_bisiesto (año)== True and mes==2:
        return 29
    else:
        return 28