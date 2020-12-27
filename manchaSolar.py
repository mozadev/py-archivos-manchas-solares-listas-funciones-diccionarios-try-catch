
from io import open


def avg_sunspot(sunspot_dict, year_tuple=(1749,2011), month_tuple=(1,12)):

    manchasxmes=list(sunspot_dict.values())

    listadeseada = []
    for i in range(year_tuple[1]-year_tuple[0]+1):
        for j in range(month_tuple[1]-month_tuple[0]+1):
            listadeseada.append(manchasxmes[i+year_tuple[0]-1749][j])


    def promedio(listadeseada):
        suma=0
        numelem=len(listadeseada)

        for el in listadeseada:
            suma=suma+el
        return suma/numelem

    return promedio(listadeseada)


def init_dictionary(file_str, sunspot_dict):
    archivo_texto = open(file_str, "r")
    archivo_texto.readline()
    archivo_texto.readline()
    archivo_texto.readline()
    archivo_texto.readline()
    for lin in archivo_texto:
        sepa = lin.split()
        ldat = []
        manchasfloat = []
        if len(sepa) == 13 or len(sepa)==10:
            for elem in sepa:
                info = elem.strip()
                if info != "":
                    ldat.append(info)
            if len(ldat) == 13 or len(ldat)==10:
                anio = ldat[0]
                manchas = ldat[1:13]
                for elem2 in manchas:
                    manchasenteror = float(elem2)
                    manchasfloat.append(manchasenteror)


                if anio not in sunspot_dict:
                    sunspot_dict[anio] = manchasfloat

def main():
    sunspot_dict = {}
    file_str  = input("Nombre del archivo a abrir: ")
    keep_going=True

    while keep_going:
        try:
            init_dictionary(file_str, sunspot_dict)
        except IOError:
            print("archivo invalido, intente nuevamente")
            file_str=input("Nombre del archivo a abrir: ")
            continue

        print("Ene, 1900-1905:", avg_sunspot(sunspot_dict, (1900, 1905), (1, 1)))
        print("Ene-Jun, 2000-2011:",  avg_sunspot(sunspot_dict, (2000, 2011), (1, 6)))
        print("Todos los años, Ene:",avg_sunspot(sunspot_dict, month_tuple= (1, 1)))
        print("Todos los meses, 1900-1905:",avg_sunspot(sunspot_dict, year_tuple=(1900, 1905)))

        try:
            print("Ejemplo de año invalido:", avg_sunspot(sunspot_dict, (100, 1000), (1, 1)))
        except KeyError:
            print("Llave (año) incorrecta")

        try:
            print("Ejemplo de mes inválido:", avg_sunspot(sunspot_dict, (2000, 2011), (1, 100)))
        except IndexError:
            print("Indice (mes) incorrrecto")
        keep_going = False
    print("Funcion main ejecutada sin errores")


main()
