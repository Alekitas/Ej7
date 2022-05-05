from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

if __name__=='__main__':
    lista=[]
    archivo=open('Libro1.csv')
    reader=csv.reader(archivo,delimiter=';')
    for fila in reader:
        numviajero=fila[0]
        DNI=int(fila[1])
        nombre=fila[2]
        apellido=fila[3]
        millasacum=int(fila[4])
        unViajero=ViajeroFrecuente(numviajero,DNI,nombre,apellido,millasacum)
        lista.append(unViajero)
    archivo.close()
    opcion=0
    numv=int(input('Ingrese numero de viajero: '))
    while opcion!=-1:
        print('\n1- Consultar Cantidad de Millas Acumuladas\n')
        print('2-Acumular Millas\n')
        print('3-Canjear Millas\n')
        print('4-Ingrese -1 para finalizar\n')
        opcion=int(input('Ingrese una opcion: '))
        if opcion==1:
            for i in range(len(lista)):
                print('Cantidad total de millas acumuladas del viajero: ',lista[i].returnnumviajero(),';',lista[i].canttotalmillas())
        elif opcion==2:
            act=int(input('Ingrese cantidad de millas del ultimo viaje: '))
            lista[numv-1].acumularmillas(int(act))
            print('Cantidad de millas actualizada: ',lista[numv-1].canttotalmillas())
        elif opcion==3:
            mcanj=int(input('Ingrese cantidad de millas a canjear: '))
            lista[numv-1].canjearmillas(mcanj)
            print('Millas actuales: ',lista[numv-1].canttotalmillas())
    otroViajero=ViajeroFrecuente('2','32435212','Alekas','perez',4000)
    if otroViajero==lista[numv-1]:
        print('El viajero 2 --tiene las mismas-- millas que el viajero 1')
    else:
        print('El viajero 1 --no tiene las mismas-- millas que el viajero 2')
    otroViajero=300+otroViajero
    print(otroViajero.canttotalmillas())
    otroViajero=100-otroViajero
    print(otroViajero.canttotalmillas())
    