# -*- coding: cp1252 -*-
# -*- coding: utf-8 -*-
from neo4jrestclient.client import GraphDatabase
db = GraphDatabase("http://localhost:7474",username="neo4j", password="1234")

doctor = db.labels.create("Doctor")
patient = db.labels.create("Patient")
meds = db.labels.create("Medicine")

def add_doctor():
    nm = raw_input("Ingrese el nombre del doctor: ")
    fld = raw_input("Ingrese la especialidad del doctor: ")
    num = raw_input("Numero para contactar al doctor: ")
    doc = db.nodes.create(name=nm, field=fld, number=num)
    doctor.add(doc)

def menu():
    print("1. Ingresar Doctor")
    print("2. Ingresar Paciente")
    print("3. Ingresar doctor para paciente")
    print("4. Consultar doctores con cierta especialidad")
    print("5. Ingresar que una persona conoce a otra")

menu()
opcion = input("Ingrese la acci�n a realizar: ")
print ("**********************************")
print ("**********************************")

while(opcion != 9):
    if(opcion == 1):
        add_doctor()
        menu()
        opcion = input("Ingrese la acci�n a realizar: ")
        print ("**********************************")
        print ("**********************************")



    elif(opcion == 2):
        print("se elige el 2")
        print ("**********************************")
        print ("**********************************")
        opcion = input("Ingrese la acci�n a realizar: ")
        print ("**********************************")
        print ("**********************************")

print("Gracias por usar el programa")
    
"""
doctor = db.labels.create("Doctor")
u1 = db.nodes.create(name="David", esp="cirujano")
doctor.add(u1)
u2 = db.nodes.create(name="Sangmin", esp="pediatra")
doctor.add(u2)
u3 = db.nodes.create(name="David", esp="cirujano")
doctor.add(u3)
"""

