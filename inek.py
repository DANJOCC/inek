#LIBRERIA DE FUNCIONES PARA CALCULOS DE INECUACIONES, INEK
#HECHO POR: DANIEL JOSE CARRIZO CONCHO

import math

#INECUACIONES LINEALES DE LA FORMA mx+b<0 Ó mx+b>0
def lineal(x,b,simbolo):
    res=-b/x
    sim=">"
    if simbolo==">":
        if x<0:
            print("x < ",res)
            sim="<"
        else:
            print("x > ",res)

    else:
        if x<0:
            print("x > a ",res)
        else:   
            print("x < ",res)
            sim="<"
    
    return [sim,res]#DEVUELVE UNA LISTA CON EL SIMBOLO Y EL VALOR DE LA RESPUESTA

#INECUACIONES CUADRATICAS DE LA FORMA ax^2+bx+c<0 ó ax^2+bx+c>0

def cuadratica(a,b,c,simbolo):
    x1=0
    x2=0
    sim1="<"
    sim2="<"
    dis=math.pow(b,2)-4*a*c #SE CALCULA LA DISCRIMINANTE DE LA ECUACION
    if dis<0:
        print("raices irreales imposible resolver")
        return "imposible de resolver con numeros reales"
    else:
        x1=(-b + math.sqrt(dis))/(2*a)
        x2=(-b - math.sqrt(dis))/(2*a)

        if x1==x2:
                if (a>0 and b>0 and c>=0 and simbolo==">") or (a<0 and b<0 and c<0 and simbolo=="<"):
                    print("x debe ser diferente de ", x1)
                    return[x1,x2]
                elif (a>0 and b>0 and c>0 and simbolo=="<") or (a>0 and b>0 and c>0 and simbolo=="<"):
                    print("imposible de resolver con numeros reales")
                    return "imposible de resolver con numeros reales"
        point=[x1,x2]
        point.sort()
        if a<0:
            if simbolo==">":
                print(point[0]," < x < ",point[0])
            else:
                print("x < ",point[0]," x > ",point[1])
                sim2=">"
        else:
            if simbolo=="<":
                print(point[0]," < x < ",point[0])
            else:
                print("x < ",point[0]," x > ",point[1])
                sim2=">"
    
    return [point[0],point[1],sim1,sim2]#DEVUELVE EL PAR DE VALORES Y SIMBOLOS DE LA RESPUESTA

#FUNCION ENCARGA DE RESOLVER INECUACIONES MAS COMPLEJAS, POR EJEMPLO:
#PARA A(y) UNA FUNCION RADICAL, LOGARITMICA, ABSOLUTA,ETC.
#Y y=ax^2+bx+c
#TAL QUE A(ax^2+bx+c)<N SIENDO N UN NUMERO REAL
#LA FUNCION SERA CAPAZ DE CALCULAR LA RESPUESTA DE ESTAS FUNCIONES
 
def conjunto(alfa,beta,tipo):

    #ALFA Y BETA SON LISTAS CON LOS SIMBOLOS Y VALORES DE LAS RESPUESTAS DE INECUACIONES CUADRATICAS O LINEALES
    #TIPO ES UN NUMERO QUE INDICA EL TIPO DE INECUACION 0=LINEAL 1=CUADRATICA
      
    if tipo==0:
        if alfa[0]==beta[0]:
            if alfa[0]==">":
                if alfa[1]>beta[1]:
                    print("Respuesta final: x > ",alfa[1])
                    return [0,alfa[1],alfa[0]]
                else:
                    print("Respuesta final: x > ",beta[1])
                    return [0,beta[1],alfa[0]]
            else:
                if alfa[1]<beta[1]:
                    print("Respuesta final: x < ",alfa[1])
                    return [0,alfa[1],alfa[0]]
                else:
                    print("Respuesta final: x < ",beta[1])
                    return [0,beta[1],alfa[0]]
        elif alfa[0]==">" and beta[0]=="<":
            if alfa[1]>beta[1]:
                print("Respuesta final: Conjunto vacio, sin interseccion aparente")
                return [0,"vacio"]
            else:
                print("Respuesta final: ",alfa[1]," < x < ",beta[1])
                return [0,alfa[1],beta[1],"<"]
        else:
            if alfa[1]>beta[1]:
                print("Respuesta final: ",beta[1]," < x < ",alfa[1])
                return [0,beta[1],alfa[1],"<"]
            else:
                print("Respuesta final: Conjunto vacio, sin interseccion aparente")
                return[0,"vacio"]
    elif tipo==1:
        if alfa=="imposible de resolver con numeros reales" or beta=="imposible de resolver con numeros reales":
            return "imposible de resolver con numeros reales"
            

        x1=[alfa[0],alfa[1]]
        x2=[beta[0],beta[1]]

        x1.sort()
        x2.sort()

        if alfa[2]==alfa[3] and beta[2]==beta[3]:
            if x1[0]>=x2[0] and x1[1]<=x2[1]:
                print("respuesta final: ",x1[0]," < x <",x1[1])
                return[1,x1[0],x1[1],"<"]
            elif x1[0]>=x2[0] and x1[1]>=x2[1]:
                print("respuesta final: ",x1[0]," < x <",x2[1])
                return[1,x1[0],x2[1],"<"]
            elif x1[0]<=x2[0] and x1[1]>=x2[1]:
                print("respuesta final: ",x2[0]," < x <",x2[1])
                return[1,x2[0],x2[1],"<"]
            else:
                print("respuesta final: ",x2[0]," < x <",x1[1])
                return[1,x2[0],x1[1],"<"]
        elif alfa[2]!=alfa[3] and beta[2]!=beta[3]:
            if x1[0]>=x2[0] and x1[1]<=x2[1]:
                print("respuesta final: ",x2[0]," > x , x > ",x2[1])
                return[1,x2[0],x2[1],">","<"]
            elif x1[0]>=x2[0] and x1[1]>=x2[1]:
                print("respuesta final: ",x2[0]," > x , x > ",x1[1])
                return[1,x2[0],x1[1],">","<"]
            elif x1[0]<=x2[0] and x1[1]>=x2[1]:
                print("respuesta final: ",x1[0]," > x , x > ",x1[1])
                return[1,x1[0],x1[1],">","<"]
            else:
                print("respuesta final: ",x1[0]," > x , x > ",x2[1])
                return[1,x1[0],x2[1]]
        elif alfa[2]==alfa[3] and beta[2]!=beta[3]:
            if x1[0]<=x2[0] and x2[0]<=x1[1] and x1[1]<=x2[1]:
                print("respuesta final: ",x1[0]," < x < ",x2[0])
                return[1,x1[0],x2[0],"<"]
            elif x2[0]<=x1[0] and x1[0]<=x2[1] and x2[1]<=x1[1]:
                print("respuesta final: ",x2[1]," < x < ",x1[1])
                return[1,x2[1],x1[1],"<"]
            elif (x1[0]>=x2[1] and x1[1]>=x2[1]) or (x1[0]<=x2[0] and x1[1]<=x2[0]):
                print("respuesta final: ",x1[0]," < x < ",x1[1])
                return[1,x1[0],x1[1],"<"]
            elif x1[0]>=x2[0] and x1[1]<=x2[1]:
                print("respuesta final:Conjunto vacio, sin intersecciones")
                return[1,"vacio"]
            else:
                print("respuesta final: ",x1[0]," < x < ",x2[0]," o ",x2[1]," < x < ",x1[1])
                return[1,x1[0],x2[0],x2[1],x1[1],"<"]
        else:
            if x1[0]<=x2[0] and x2[0]<=x1[1] and x1[1]<=x2[1]:
                print("respuesta final: ",x1[1]," < x < ",x2[1])
                return[1,x1[1],x2[1],"<"]
            elif x2[0]<=x1[0] and x1[0]<=x2[1] and x2[1]<=x1[1]:
                print("respuesta final: ",x2[0]," < x < ",x1[0])
                return[1,x2[0],x1[0],"<"]
            elif (x1[0]>=x2[1] and x1[1]>=x2[1]) or (x1[0]<=x2[0] and x1[1]<=x2[0]):
                print("respuesta final: ",x2[0]," < x < ",x2[1])
                return[1,x2[0],x2[1],"<"]
            elif x1[0]>=x2[0] and x1[1]<=x2[1]:
                print("respuesta final: ",x2[0]," < x < ",x1[0]," o ",x1[1]," < x < ",x2[1])
                return[1,x2[0],x1[0],x1[1],x2[1],"<"]
            else:
                print("respuesta final: sin intersecciones")
                return[1,"vacio"]

#FUNCION PARA INECUACIONES CON RADICALES
#SE CONSIDERA A TODOS LOS RADICALES POSITIVOS Y MENORES A UN NUMERO MAYOR A CERO O MAYORES A
#CUALQUIER NUMERO MAYOR A CERO
def radical(tipo,coeficientes,simbolo):

    #COEFICIENTES ES UNA LISTA DE LOS COEFICIENTES DE LAS ECUACIONES INTERNAS DEL RADICAL
    #Y EL ULTIMO VALOR ES NUMERO DEL LADO DERECHO DE LA INECUACION (A(y)<N ó A(y)>n)

    if tipo==0:
        alfa=lineal(coeficientes[0],coeficientes[1],">")
        beta=lineal(coeficientes[0],coeficientes[1]-(math.pow(coeficientes[2],2)),simbolo)
        conjunto(alfa,beta,tipo)
        
    else:
        alfa=cuadratica(coeficientes[0],coeficientes[1],coeficientes[2],">")
        beta=cuadratica(coeficientes[0],coeficientes[1],coeficientes[2]-(math.pow(coeficientes[3],2)),simbolo)
        conjunto(alfa,beta,tipo)
        
    return "exito"

#FUNCION PARA INECUACIONES LOGARITMICAS DE CUALQUIER BASE, EXCEPTO CERO Y NUMERO NEGATIVOS
#SE CONSIDERA A TODOS LOS LOGARITMOS POSITIVOS

def log(tipo,base,coeficientes,simbolo):
    #PARA ESTE CASO EL PRIMER NUMERO DE COEFICIENTES, SI SE CALCULA CON RADICALES REPRESENTA SU COEFICIENTE
    
    if base<=0:
        return "Base invalida"
    if tipo[0]==0:
        alfa=lineal(coeficientes[0],coeficientes[1],">")
        beta=lineal(coeficientes[0],coeficientes[1]-(math.pow(coeficientes[2],base)),simbolo)
        conjunto(alfa,beta,tipo[0])
    elif tipo[0]==1:
        alfa=cuadratica(coeficientes[0],coeficientes[1],coeficientes[2],">")
        beta=cuadratica(coeficientes[0],coeficientes[1],coeficientes[2]-(math.pow(coeficientes[3],base)),simbolo)
        conjunto(alfa,beta,tipo[1])
    else:
        if tipo[1]==0:
            if coeficientes[0]<=0:
                return "coeficiente del radical invalido"
            alfa=lineal(coeficientes[1],coeficientes[2],">")
            beta=lineal(coeficientes[1],coeficientes[2]-(math.pow(2*(coeficientes[2]-coeficientes[0]),base)),simbolo)
            conjunto(alfa,beta,tipo[0])
        else:
            alfa=cuadratica(coeficientes[1],coeficientes[2],coeficientes[3],">")
            beta=cuadratica(coeficientes[1],coeficientes[2],coeficientes[3]-(math.pow(2*(coeficientes[4]-coeficientes[0]),base)),simbolo)
            conjunto(alfa,beta,tipo[0])




