# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
db = GraphDatabase("http://localhost:7474",username="neo4j", password="1111")

doctor = db.labels.create("Doctor")
patient = db.labels.create("Patient")
meds = db.labels.create("Medicine")

doctores = []

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
    med = db.nodes.create(prescription=medicine)
    
    patient.add(pat)
    meds.add(med)
    pat.relationships.create("takes", med)

def knows():
    p1 = raw_input("Ingrese nombre de paciente 1: ")
    p2 = raw_input("Ingrese nombre de paciente 2: ")
    patient.get(name=p1)[0].relationships.create("knows",patient.get(name=p2)[0])

#def doctor_appointment():
    

def menu():
    print("1. Ingresar Doctor")
    print("2. Ingresar Paciente")
    print("3. Ingresar doctor para paciente")
    print("4. Consultar doctores con cierta especialidad")
    print("5. Ingresar que una persona conoce a otra")

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
        opcion = input("Ingrese la acción a realizar: ")
        print ("**********************************")
        print ("**********************************")

    elif(opcion == 5):
        knows()
        print ("**********************************")
        print ("**********************************")
        menu()
        opcion = input("Ingrese la accion a realizar: ")
        print ("**********************************")
        print ("**********************************")

  #  elif(opcion == 3):
 #       doctor_appointment()

print("Gracias por usar el programa")

