from auxiliar1 import es_bisiesto
from auxiliar2 import cant_dias_mes
from auxiliar3 import fecha_valida
from auxiliar4 import pide_cant_pilas

def main():
    '''Generará a traves de los datos ingresados por un unico usuario un
    informe estadistico mensual a partir de datos de la recoleccion de pilas
    usadas por las universidades bonaerenses.'''


    anio = int(input ('ingrese el año: '))
    mes = int(input ('ingrese el mes: ' ))
    while anio < 2023 or mes < 1 or mes > 12: 
        anio = int(input ('incorrecto reingrese el año: ' ))
        mes= int(input ('incorrecto reingrese el mes: ' ))
    
    cant_univ = 0
    uni_no_boton = 0
    total_pilas_salinas = 0
    total_pilas_alcalinas = 0
    total_pilas_litio = 0
    total_pilas_boton = 0
    maximo_enviado = 0
    total_kg_unis = 0
    pregunta = input ('Desea ingresar una universidad S/N: ' )
    
    while pregunta == 'S':
        abrev_uni = input ('Ingrese el nombre abreviado de la Universidad: ')
        cant_univ += 1
        dia = int(input ('Ingrese el dia: ' ))
        
        while fecha_valida(dia,mes,anio) == False:
            dia = int(input ('Dia inválido, reingrese el dia: '))
        
        gramos_total = 0
        
        while gramos_total <= 0 or gramos_total >= 350000:
            cant_pilas_salinas = pide_cant_pilas ('Salinas')
            cant_pilas_alcalinas = pide_cant_pilas ('Alcalinas')
            cant_pilas_litio = pide_cant_pilas ('de Litio')
            cant_pilas_boton = pide_cant_pilas ('Boton')
            gramos_total = (cant_pilas_salinas + cant_pilas_alcalinas + cant_pilas_litio + cant_pilas_boton) 
            if cant_pilas_litio == 0:
                porcentaje_pilas_litio = 0
            else:
                porcentaje_pilas_litio =(cant_pilas_litio * 100) / gramos_total
            kg_total = gramos_total / 1000
        print ('Universidad: ',abrev_uni)
        print ('Fecha de envio:', dia,'/', mes,'/',anio)
        print ('Gramos de pilas Salinas: ', cant_pilas_salinas)
        print ('Gramos de pilas Alcalinas: ', cant_pilas_alcalinas)
        print ('Gramos de pilas de Litio: ', cant_pilas_litio)
        print ('Gramos de pilas Boton: ', cant_pilas_boton)
        print ('Total de KG enviados:', kg_total)
        print ('Porcentaje de pilas de Litio:', porcentaje_pilas_litio, '%')
        pregunta = input ('Desea ingresar otra universidad S/N: ', )
        total_pilas_salinas += cant_pilas_salinas
        total_pilas_alcalinas += cant_pilas_alcalinas
        total_pilas_litio += cant_pilas_litio
        total_pilas_boton += cant_pilas_boton
        total_kg_unis += kg_total
        if cant_pilas_boton == 0:
                uni_no_boton += 1 
        if maximo_enviado < kg_total:
            maximo_enviado = kg_total
        else:
            maximo_enviado = maximo_enviado    
    total_pilas_litio = total_pilas_litio / 1000
    total_pilas_salinas = total_pilas_salinas / 1000
    total_pilas_alcalinas = total_pilas_alcalinas / 1000
    total_pilas_boton = total_pilas_boton / 1000
    
    if cant_univ == 0:
        porcentaje_total = 0
    elif cant_univ == 1:
        porcentaje_total = porcentaje_pilas_litio
    else:
        porcentaje_total = (total_pilas_litio * 100) / total_kg_unis
    
    print ('Periodo del informe', mes,'/',anio)
    print ('Catidad de Universidades: ',cant_univ)
    print ('KG total de pilas Salinas: ', total_pilas_salinas)
    print ('KG total de pilas Alcalinas: ', total_pilas_alcalinas)
    print ('KG total de pilas de Litio: ', total_pilas_litio)
    print ('KG total de pilas Boton: ', total_pilas_boton)
    print ('Total de KG: ', total_kg_unis)
    print ('Porcentaje total de pilas de Litio: ', porcentaje_total, '%')
    print ('Cantidad de universidades que no enviaron pilas Boton: ', uni_no_boton)
    print ('Maximo total de KG enviados: ', maximo_enviado)
