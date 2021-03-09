import math
import inek
# nota 1: todas las inecuaciones son tomadas como menor o mayor a cero
# asi que cualquier inecuacion debe ser cero del otro lado de los simbolos > ó <
# nota 2: solo calcula > ó <
print("elija un tipo de inecuacion\n")
print("1.Lineal (mx+b<0 ó mx+b>0)\n")
print("2.Cuadratica (ax^2+bx+c<0 ó ax^2+bx+c>0\n")
print("3.Radical (Raiz cuadrada de una funcion Lineal o Cuadratica)\n")
print("4.Logaritmica (Logaritmo de una funcion Lineal,Cuadratica o Radical)\n")
op=input("Seleccion:\n")
co=[]
if op=="1":
    co.append(int(input("ingrese cociente de la variable: ")))
    co.append(int(input("ingrese termino independiente: ")))
    simbolo=input("ingrese forma de evaluacion: ")
    inek.lineal(co[0],co[1],simbolo)    
elif op=="2":
    co=[]
    co.append(int(input("ingrese el primer coeficiente: ")))
    co.append(int(input("ingrese el segundo coeficiente: ")))
    co.append(int(input("ingrese el tercer coeficiente: ")))
    simbolo=input("ingrese forma de evaluacion: ")
    inek.cuadratica(co[0],co[1],co[2],simbolo)
elif op=="3":
    print("elija un tipo de ecuacion detro del radical\n")
    print("1.lineal\n")
    print("2.Cuadratica\n")
    op=input("Seleccion:")
    simbolo=input("\ningrese forma de evaluacion: ")
    if op=="1":
        co.append(int(input("ingrese cociente de la variable: ")))
        co.append(int(input("ingrese termino independiente: ")))
        co.append(int(input("ingrese termino del otro lado de la inecuacion: ")))
        inek.radical(0,co,simbolo)
    else:
        co.append(int(input("ingrese el primer coeficiente: ")))
        co.append(int(input("ingrese el segundo coeficiente: ")))
        co.append(int(input("ingrese el tercer coeficiente: ")))
        co.append(int(input("ingrese termino del otro lado de la inecuacion: ")))
        inek.radical(1,co,simbolo)
else:
    print("elija un tipo de ecuacion detro del logaritmo\n")
    print("1.lineal\n")
    print("2.Cuadratica\n")
    print("3.Radical\n")
    op=input("Seleccion:")
    base=int(input("\nIngrese base del logaritmo: "))
    simbolo=input("\nIngrese forma de evaluacion: ")
    if op=="1":
        co.append(int(input("ingrese cociente de la variable: ")))
        co.append(int(input("ingrese termino independiente: ")))
        co.append(int(input("ingrese termino del otro lado de la inecuacion: ")))
        inek.log([0,0],base,co,simbolo)
    elif op=="2":
        co.append(int(input("ingrese el primer coeficiente: ")))
        co.append(int(input("ingrese el segundo coeficiente: ")))
        co.append(int(input("ingrese el tercer coeficiente: ")))
        co.append(int(input("ingrese termino del otro lado de la inecuacion: ")))
        inek.log([1,0],base,co,simbolo)
    elif op=="3":
        print("\nelija un tipo de ecuacion detro del radical\n")
        print("1.lineal\n")
        print("2.Cuadratica\n")
        op=input("Seleccion:")
        simbolo=input("\ningrese forma de evaluacion: ")
        if op=="1":
            co.append(int(input("ingrese cociente del radical: ")))
            co.append(int(input("ingrese cociente de la variable: ")))
            co.append(int(input("ingrese termino independiente: ")))
            co.append(int(input("ingrese termino del otro lado de la inecuacion: ")))
            inek.log([2,0],base,co,simbolo)
        else:
            co.append(int(input("ingrese cociente del radical: ")))
            co.append(int(input("ingrese el primer coeficiente: ")))
            co.append(int(input("ingrese el segundo coeficiente: ")))
            co.append(int(input("ingrese el tercer coeficiente: ")))
            co.append(int(input("ingrese termino del otro lado de la inecuacion: ")))
            inek.log([2,1],base,co,simbolo)



input("Presione ENTER para finalizar")
