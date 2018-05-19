# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
"""
Algoritmos y Estructuras de Datos
Hoja de trabajo 10

Antonio Reyes #17273
Esteban Cabrera #17781
Miguel #17102
"""
from neo4jrestclient.client import GraphDatabase
db = GraphDatabase("http://localhost:7474",username="neo4j", password="1111")

#Se nombran los labels: Doctor, Patient, Medicine
doctor = db.labels.create("Doctor")
patient = db.labels.create("Patient")
meds = db.labels.create("Medicine")

#1
#agregar un doctor al grafo
#se pide el nombre, especializacion y numero, luego se agrega a neo4j utilizando db.nodes.create + los valores dentro del nodo.
#este nodo de agrega al label doctor.
def add_doctor():
    nm = raw_input("Ingrese el nombre del doctor: ")
    fld = raw_input("Ingrese la especialidad del doctor: ")
    num = raw_input("Numero para contactar al doctor: ")
    doc = db.nodes.create(name=nm, field=fld, number=num)
    doctor.add(doc)

#2
#agregar un paciente al grafo
#se pide el nombre del paciente, nombre de doctor, fecha de visita, medicamento
#luego de crear el nodo y agregarlo al label patient, se realizan las relaciones con pat.relationships.create (nombre de arista, nodo)
def add_patient():
    nm = raw_input("Ingrese el nombre del paciente: ")
    doc_name = raw_input("Ingresa el doctor del paciente: ")
    dt = raw_input("Ingresa fecha de visita: ")
    medicine = raw_input("Ingresa medicina recetada: ")
    pat = db.nodes.create(name=nm, doctor=doc_name, date=dt, prescription=medicine)
    patient.add(pat)
    pat.relationships.create("takes", meds.get(prescription=medicine)[0])
    pat.relationships.create("visits", doctor.get(name=doc_name)[0])
    doctor.get(name=doc_name)[0].relationships.create("prescribes",meds.get(prescription=medicine)[0])

#3
#se crea el nodo de medicamento y se agrega al label meds
def add_medication():
    nm = raw_input("Ingrese el nombre del medicamento: ")
    med = db.nodes.create(prescription=nm)
    meds.add(med)

#4
#Se crea la relacion entre un paciente y el doctor (el paciente visita a cierto doctor)
def doctor_appointment():
    doc = raw_input("Ingrese el nombre del doctor: ")
    pat = raw_input("Ingrese el nombre del paciente: ")
    patient.get(name=pat)[0].relationships.create("visits", doctor.get(name=doc)[0])

#5
#Se crean dos realciones, una es la relacion entre el paciente y el medicamente (toma ese medicamento)
#la segunda relacion es entre el doctor y el medicamento (el doctor receta ese medicamento)
def prescribe():
    doc = raw_input("Ingrese el nombre del doctor: ")
    pat = raw_input("Ingrese el nombre del paciente: ")
    med = raw_input("Ingrese el nombre del medicamento: ")
    patient.get(name=pat)[0].relationships.create("takes", meds.get(prescription=med)[0])
    doctor.get(name=doc)[0].relationships.create("prescribes", meds.get(prescription=med)[0])


#6
#Se van a buscar todos los doctores con una especialidad elegida por el usuario
def what_field():
    opcion = raw_input("Ingrese la especialidad: ")
    #SOLO DEBE FUNCIONAR este comando-->  MATCH (n:Doctor {field:'Cirujano'}) RETURN n
    query = "MATCH (n:Doctor {field:'"+opcion+"'}) RETURN n"
    results = db.query(query, data_contents=True)
    a = results.rows
    for list in a:
        for x in list:
            print x
 
#7
#Se crea una relacion entre pacientes (se conocen)
def knows():
    p1 = raw_input("Ingrese nombre de paciente 1: ")
    p2 = raw_input("Ingrese nombre de paciente 2: ")
    patient.get(name=p1)[0].relationships.create("knows",patient.get(name=p2)[0])
    patient.get(name=p2)[0].relationships.create("knows",patient.get(name=p1)[0])

#8
#Se crea una relacion entre doctores (se conocen, se escribe "knows_Doctor" para no confundirlo con la relacion entre pacientes
def doc_knows():
    d1 = raw_input("Ingrese el nombre del doctor 1: ")
    d2 = raw_input("Ingrese el nombre del doctor 2: ")
    doctor.get(name=d1)[0].relationships.create("knows_Doctor", doctor.get(name=d2)[0])
    doctor.get(name=d2)[0].relationships.create("knows_Doctor", doctor.get(name=d1)[0])

#9
#El paciente un doctor que tenga una especialidad específica, pero que haya sido visitado por alguien que él conoce, o que un conocido de un conocido ha visitado
def recomendation():
    pat = raw_input("Ingrese el paciente que quiere recomendacion: ")
    fld = raw_input("Ingrese la especializacion que desea: ")
    query = "match (p:Patient{name:'"+pat+"'})-[:knows*1..2]->(amigos)-[:visits]->(d:Doctor{field:'"+fld+"'}) return d"
    results = db.query(query, data_contents=True)
    a = results.rows
    b = []
    for x in a:
        if x not in b:
            b.append(x)
            print x

#10
#Referir a su paciente a otro doctor con una especialidad específica. Pero el doctor nuevo debe ser conocido por el doctor original, o ser un conocido de un conocido del doctor original
def refer_patient():
    doc = raw_input("Ingrese el nombre del doctor actual: ")
    pat = raw_input("Ingrese el nombre del paciente: ")
    field = raw_input("Ingrese la especializacion que se necesita: ")
    #"match (d:Doctor{name:'Mario'})-[:knowsDoc*1..2]->(a:Doctor{field:'Pediatra'}) return a"
    query = "match (d:Doctor{name:'"+doc+"'})-[:knows_Doctor*1..2]->(a:Doctor{field:'"+field+"'}) return a"
    results = db.query(query, data_contents=True)
    a = results.rows
    b = []
    print ("Se puede referir el paciente " + "**" + pat + "** " + "a los siguientes doctores: ")
    for x in a:
        if x not in b:
            b.append(x)
            print x
            
def menu():
    print("1. Ingresar Doctor")
    print("2. Ingresar Paciente")
    print("3. Ingresar Medicamento")
    print("4. Ingresar doctor para paciente")
    print("5. Recetar medicamento para paciente")
    print("6. Consultar doctores con cierta especialidad")
    print("7. Ingresar que una persona conoce a otra")
    print("8. Ingresar que un doctor conoce a otro doctor")
    print("9. Recomendar doctor")
    print("10. Referir paciente a otro doctor")
    print("11. Salir")

menu()
opcion = input("Ingrese la acción a realizar: ")
print ("**********************************")
print ("**********************************")

while(opcion != 11):

    #1. Ingresar doctor
    if(opcion == 1):
        add_doctor()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #2. Ingresar paciente
    elif(opcion == 2):
        add_patient()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #3. Ingresar medicamento
    elif(opcion == 3):
        add_medication()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #4. Ingresar doctor para paciente
    elif(opcion == 4):
        doctor_appointment()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #5. Recetar medicamento para paciente
    elif(opcion == 5):
        prescribe()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

     #6. Consultar doctor para cierta especialidad   
    elif(opcion == 6):
        what_field()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #7. Ingresar que una persona conoce a otra
    elif(opcion == 7):
        knows()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #8. Ingresar que un doctor conoce a otro doctor
    elif(opcion == 8):
        doc_knows()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #9. Recomendar doctor
    elif(opcion == 9):
        recomendation()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #10. Referir paciente a otro doctor
    elif(opcion == 10):
        refer_patient()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

    #En el caso que no eligan un numero entre 1-10 (o 11)
    else:
        print("La opción ingresada no es valida")
        menu()
        opcion = input("Ingrese la accion a realizar: ")


print("Gracias por usar el programa")

