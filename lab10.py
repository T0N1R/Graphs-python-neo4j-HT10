# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
"""
Algoritmos y Estructuras de Datos
Laboratorio 10

Antonio Reyes #17273
Esteban Cabrera #17781
Miguel #17102
"""
from neo4jrestclient.client import GraphDatabase
db = GraphDatabase("http://localhost:7474",username="neo4j", password="1111")

doctor = db.labels.create("Doctor")
patient = db.labels.create("Patient")
meds = db.labels.create("Medicine")

name = []

def add_doctor():
    nm = raw_input("Ingrese el nombre del doctor: ")
    fld = raw_input("Ingrese la especialidad del doctor: ")
    num = raw_input("Numero para contactar al doctor: ")
    doc = db.nodes.create(name=nm, field=fld, number=num)
    doctor.add(doc)

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

def add_medication():
    nm = raw_input("Ingrese el nombre del medicamento: ")
    med = db.nodes.create(prescription=nm)
    meds.add(med)

def knows():
    p1 = raw_input("Ingrese nombre de paciente 1: ")
    p2 = raw_input("Ingrese nombre de paciente 2: ")
    patient.get(name=p1)[0].relationships.create("knows",patient.get(name=p2)[0])
    patient.get(name=p2)[0].relationships.create("knows",patient.get(name=p1)[0])

def what_field():
    opcion = raw_input("Ingrese la especialidad: ")
    #SOLO DEBE FUNCIONAR este comando-->  MATCH (n:Doctor {field:'Cirujano'}) RETURN n
    query = "MATCH (n:Doctor {field:'"+opcion+"'}) RETURN n"
    results = db.query(query, data_contents=True)
    a = results.rows
    for list in a:
        for x in list:
            print x
 
def doctor_appointment():
    doc = raw_input("Ingrese el nombre del doctor: ")
    pat = raw_input("Ingrese el nombre del paciente: ")
    patient.get(name=pat)[0].relationships.create("visits", doctor.get(name=doc)[0])

def prescribe():
    doc = raw_input("Ingrese el nombre del doctor: ")
    pat = raw_input("Ingrese el nombre del paciente: ")
    med = raw_input("Ingrese el nombre del medicamento: ")
    patient.get(name=pat)[0].relationships.create("takes", meds.get(prescription=med)[0])
    doctor.get(name=doc)[0].relationships.create("prescribes", meds.get(prescription=med)[0])

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
    
    #for list in a:
     #   for x in list:
      #      if x != x-1:
       #         print x

def menu():
    print("1. Ingresar Doctor")
    print("2. Ingresar Paciente")
    print("3. Ingresar Medicamento")
    print("4. Ingresar doctor para paciente")
    print("5. Recetar medicamento para paciente")
    print("6. Consultar doctores con cierta especialidad")
    print("7. Ingresar que una persona conoce a otra")
    print("8. Recomendar doctor")
    print("9. Salir")

menu()
opcion = input("Ingrese la acción a realizar: ")
print ("**********************************")
print ("**********************************")

while(opcion != 9):
    if(opcion == 1):
        add_doctor()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 2):
        add_patient()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 3):
        add_medication()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 4):
        doctor_appointment()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 5):
        prescribe()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")
        
    elif(opcion == 6):
        what_field()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 7):
        knows()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 8):
        recomendation()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

    else:
        print("La opción ingresada no es valida")
        menu()
        opcion = input("Ingrese la accion a realizar: ")


print("Gracias por usar el programa")

