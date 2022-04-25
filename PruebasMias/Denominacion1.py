#array={"nombre":[
#               jose, 
#               juan, 
#               Victor, 
#               Esteban],
#       "Apellido":[
#               Martinez, 
#               Perez, 
#               Monroy, 
#               Arce], 
#       "Codigo de empleado":[
#               321548,
#               315698,
#               159875,
#               235489
#       "Sueldo":[
#               1555.50,
#               2300,
#               2000.60,
#               2784.40
#                ] 
#      }

residuo = 0
mil = 0
quinientos=0
docientos=0
cien=0
cincuenta=0
veinte=0
diez=0
cinco=0
dos=0
un=0
cincuentaCen=0
veinteCen=0
total=0
denominaciones = [["mil: ", mil], ["quinientos: ",quinientos], ["docientos: ",docientos], ["cien: ",cien], ["cincuenta: ",cincuenta],
                 ["veinte: ",veinte], ["diez: ",diez], ["cinco: ",cinco], ["dos: ",dos], ["un: ",un], ["ciencuentaCent: ",cincuentaCen]]

Tabla={
    "nombre":["Jose","Juan","Victor","Esteban"],
    "apellido":["Martinez","Perez", "Monroy","Arce"],
    "codigo de empleado":[321548,315698,159875,235489],
    "sueldo":[1555.50,2300,2000.60,2784.40]
}

# for llave in Tabla:
#     print(llave, ": ", Tabla[llave], sep='')
#print(Tabla["nombre"])


def Denominacion(residuo):
    while residuo != 0:
        if residuo!=0:
            mil=residuo//1000
            residuo=residuo%1000
            denominaciones[0][1]+=mil
            if residuo!=0:
                quinientos=residuo//500
                residuo=residuo%500
                denominaciones[1][1]+=quinientos
                if residuo!=0:
                    docientos=residuo//200
                    residuo=residuo%200
                    denominaciones[2][1]+=docientos
                    if residuo!=0:
                        cien=residuo//100
                        residuo=residuo%100
                        denominaciones[3][1]+=cien
                        if residuo!=0:
                            cincuenta=residuo//50
                            residuo=residuo%50
                            denominaciones[4][1]+=cincuenta
                            if residuo!=0:
                                veinte=residuo//20
                                residuo=residuo%20
                                denominaciones[5][1]+=veinte
                                if residuo!=0:
                                    diez=residuo//10
                                    residuo=residuo%10
                                    denominaciones[6][1]+=diez
                                    if residuo!=0:
                                        cinco=residuo//5
                                        residuo=residuo%5
                                        denominaciones[7][1]+=cinco
                                        if residuo!=0:
                                            dos=residuo//2
                                            residuo=residuo%2
                                            denominaciones[8][1]+=dos
                                            if residuo!=0:
                                                un=residuo//1
                                                residuo=residuo%1
                                                denominaciones[9][1]+=un
                                                if residuo!=0:
                                                    cincuentaCen=residuo//.50
                                                    residuo=residuo%.50
                                                    denominaciones[10][1]+=cincuentaCen
                                                if residuo!=0:
                                                    residuo=0
                                                    
    return(denominaciones)

#leer uno por uno el sueldo y en cada iteracion del for mandar llamar el metodo "Denominacion"
for index in Tabla["sueldo"]:
    residuo = index
    Denominacion(residuo)
#suma total de los sueldos
for sumas in Tabla["sueldo"]:
    total+=sumas

print("total a pagar: ", total)
print (denominaciones)

"puedo asignarle el monto de Denominacion que se le"
"debe dar a cada empleado con su codigo de empleado"
