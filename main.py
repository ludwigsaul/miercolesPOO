from cosas import Alumno, Perro

def main():
    al1 = Alumno("jose", 11, "ICO")
    print(vars(al1))
    al1.__nombre="Diego"
    print(vars(al1))
    al1.set_nombre("Maria")
    print(vars(al1))
    print("---To String")
    print(al1)
    al1.set__edad(999)
    print(al1)
    al1.estudiar(4)
    al1.estudiar()
    print("-----PERRO-----")
    perro1 = Perro("Poddle", 2, 0.35)
    print(vars(perro1))
    perro1.raza = "De la calle" #set en notacion Pythonic
    print(vars(perro1))
    perro1.edad = 12
    perro1.estatura = 0.45
    print(perro1)
    cachorro = Perro.es_cachorro(perro1.edad)
    print(cachorro)
    Perro.dormir(7)
    danes = Perro.perro_grande(0.8)
    print(danes)


main()