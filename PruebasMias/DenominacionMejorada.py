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
veinteCent=0
diezCent=0
total=0
denominaciones = {
                    "mil": mil, 
                    "quinientos":quinientos, 
                    "docientos":docientos, 
                    "cien":cien, 
                    "cincuenta":cincuenta,
                    "veinte":veinte, 
                    "diez":diez, 
                    "cinco":cinco, 
                    "dos":dos, 
                    "un":un, 
                    "ciencuentaCent":cincuentaCen,
                    "veinteCent":veinteCent,
                    "diezCent":diezCent
                }

Tabla={
    "nombre":["Jose","Juan","Victor","Esteban"],
    "apellido":["Martinez","Perez", "Monroy","Arce"],
    "codigo de empleado":[321548,315698,159875,235489],
    "sueldo":[1555.50,2300,2000.60,2784.40]
}

# for llave in Tabla:
#     print(llave, ": ", Tabla[llave], sep='')
# print(Tabla["nombre"])
mil1=1000

def Denominacion(residuo):
    while residuo != 0:
        if residuo!=0:
            mil, residuo = divmod(residuo, 1000)
            # mil=residuo//1000
            # residuo=residuo%1000
            residuo = round(residuo,2)
            denominaciones["mil"]+=mil
            if residuo!=0:
                quinientos, residuo = divmod(residuo, 500)
                residuo = round(residuo,2)
                denominaciones["quinientos"]+=quinientos
                if residuo!=0:
                    docientos, residuo = divmod(residuo, 200)
                    residuo = round(residuo,2)
                    denominaciones["docientos"]+=docientos
                    if residuo!=0:
                        cien, residuo = divmod(residuo,100)
                        residuo = round(residuo,2)
                        denominaciones["cien"]+=cien
                        if residuo!=0:
                            cincuenta, residuo = divmod(residuo, 50)
                            residuo = round(residuo,2)
                            denominaciones["cincuenta"]+=cincuenta
                            if residuo!=0:
                                veinte, residuo = divmod(residuo, 20)
                                residuo = round(residuo,2)
                                denominaciones["veinte"]+=veinte
                                if residuo!=0:
                                    diez, residuo = divmod(residuo, 10)
                                    residuo = round(residuo,2)
                                    denominaciones["diez"]+=diez
                                    if residuo!=0:
                                        cinco, residuo = divmod(residuo, 5)
                                        residuo = round(residuo,2)
                                        denominaciones["cinco"]+=cinco
                                        if residuo!=0:
                                            dos, residuo = divmod(residuo, 2)
                                            residuo = round(residuo,2)
                                            denominaciones["dos"]+=dos
                                            if residuo!=0:
                                                un, residuo = divmod(residuo, 1)
                                                denominaciones["un"]+=un
                                                if residuo!=0:
                                                    cincuentaCen, residuo = divmod(residuo, .50)
                                                    denominaciones["ciencuentaCent"]+=cincuentaCen
                                                    if residuo!=0:
                                                        veinteCent, residuo = divmod(residuo, .20)
                                                        denominaciones["veinteCent"]+=veinteCent
                                                        if residuo!=0:
                                                            diezCent, residuo = divmod(residuo, .10)
                                                            denominaciones["diezCent"]+=diezCent
                                                            
                                                    
    return(denominaciones)

#leer uno por uno el sueldo y en cada iteracion del for mandar llamar el metodo "Denominacion"
for index in Tabla["sueldo"]:
    residuo = index
    Denominacion(residuo)

#suma total de los sueldos
for sumas in Tabla["sueldo"]:
    total+=sumas

for den in denominaciones:
    print(den, ": ", denominaciones[den], sep='')

print("total a pagar: ", total)

#print (denominaciones)

"puedo asignarle el monto de Debominacion que se le"
"debe dar a cada empleado con su codigo de empleado"

#8 -> 1000
#1 -> 500
#1 -> 100
#2 -> 20
#1 -> 0.50