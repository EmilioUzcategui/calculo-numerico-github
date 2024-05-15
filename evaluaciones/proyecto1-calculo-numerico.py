import flet as ft
from flet import View,Page,AppBar,ElevatedButton,Text
from flet import RouteChangeEvent,ViewPopEvent,CrossAxisAlignment,MainAxisAlignment
import numpy as np
from flet_core.control_event import ControlEvent

'''
Nombre: Emilio Uzcategui
cedula: 30347197
universidad: Jose Antonio Paez
version de python del entorno virtual: 3.11.6
version de flet: 0.22.1
version de numpy:1.26.4
'''
#matrices de 0 que se usaran para llenarlas manualmente
matriz1 = np.zeros((2,3)).astype(float)
matriz2 = np.zeros((3,4)).astype(float)
matriz3 = np.zeros((4,5)).astype(float)
matriz4 = np.zeros((5,6)).astype(float)
#contadores que controlan que no nos pasemos al introducir elementos a una matriz manualmente
cont1=0
cont2=0
cont3=0
cont4=0
#contadores que sirven como indices al llenar las matrices manualmente
fila_actual1=0
fila_actual2=0
fila_actual3=0
fila_actual4=0

#funcion que permite invertir los numeros que se convierten pasandolos como cadenas
def invertir(cadena):
    invertido=""
    for i in range(len(cadena)-1,-1,-1):
        invertido+=cadena[i]
    return invertido

#convertores de binario

def binario_ternario(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def binario_cuaternario(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def binario_octal(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_octal(num)))

def binario_hexadecimal(numero):
    num=binario_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

def binario_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(2**i) 
        i+=1 
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

#convertores de ternario

def ternario_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(3**i)
        i+=1  
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

def ternario_binario(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_binario(num)))

def ternario_cuaternario(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def ternario_octal(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_octal(num)))

def ternario_hexadecimal(numero):
    num=ternario_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

#convertores de cuaternario

def cuaternario_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(4**i) 
        i+=1 
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

def cuaternario_binario(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_binario(num)))

def cuaternario_ternario(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def cuaternario_octal(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_octal(num)))

def cuaternario_hexadecimal(numero):
    num=cuaternario_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

#convertores de octal

def octal_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(8**i) 
        i+=1 
    for i in numerot:
        lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum

def octal_binario(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_binario(num)))

def octal_ternario(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def octal_cuaternario(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def octal_hexadecimal(numero):
    num=octal_decimal(numero)
    return invertir(str(decimal_hexadecimal(num)))

#convertores de hexadecimal

def hexadecimal_decimal(numero):
    i=0
    acum=0
    lista=[]
    lista2=[]
    numerot=invertir(str(numero))
    while(i<len(str(numero))):
        lista.append(16**i) 
        i+=1 
    for i in numerot:
        if i=="A":
            lista2.append(10)
        elif i=="B":
            lista2.append(11)
        elif i=="C":
            lista2.append(12)
        elif i=="D":
            lista2.append(13)
        elif i=="E":
            lista2.append(14)
        elif i=="F":
            lista2.append(15)
        else:
            lista2.append(int(i))
    for i in range(0,len(lista)):
        acum+=lista[i]*lista2[i]
    return acum  

def hexadecimal_binario(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_binario(num)))

def hexadecimal_ternario(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_terciario(num)))

def hexadecimal_cuaternario(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_cuaternario(num)))

def hexadecimal_octal(numero):
    num=hexadecimal_decimal(numero)
    return invertir(str(decimal_octal(num)))
 
#convertores de decimal

def decimal_binario(numero):
    resto=0
    bin=""
    while numero>0:
        resto = numero%2
        numero=numero//2
        bin+=str(resto)
    return bin
     

def decimal_octal(numero):
    resto = 0
    octal=""
    while numero>0:
        resto = numero%8
        numero=numero//8
        octal+=str(resto)
    return octal

def decimal_cuaternario(numero):
    resto = 0
    cuat=""
    while numero>0:
        resto = numero%4
        numero=numero//4
        cuat+=str(resto)
    return cuat

def decimal_hexadecimal(numero):
    resto=0
    hexa=""
    while numero>0:
        resto = numero%16
        if resto==10:
            hexa+="A"
            numero=numero//16
        elif resto==11:
            hexa+="B"
            numero=numero//16
        elif resto==12:
            hexa+="C"
            numero=numero//16

        elif resto==13:
            hexa+="D"
            numero=numero//16
        elif resto==14:
            hexa+="E"
            numero=numero//16
        elif resto==15:
            hexa+="F"
            numero=numero//16
        else:
            hexa+=str(resto)
            numero=numero//16
    return hexa

def decimal_terciario(numero):
    resto=0
    terc=""
    while numero>0:
        resto = numero%3
        numero=numero//3
        terc+=str(resto)
    return terc
print(ternario_decimal(1021))

#validaciones de numeros

#validacion decimal

def validar_decimal(numero):
    if str(numero)=="":
        return False
    for i in numero:
        if numero.isnumeric()==False:
            return False
        else:
            return True

#validacion de binario

def validar_binario(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>1 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True
    
#validacion de ternario

def validar_ternario(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>2 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True

#validacion de cuaternario

def validar_cuaternario(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>3 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True

#validacion de octal

def validar_octal(numero):
    if str(numero)=="":
        return False
    cont=0
    for i in numero:
        if numero.isnumeric()==False:
            return False
        elif int(i)>7 or int(i)<0:
            cont+=1
    if cont!=0:
        return False
    else:
        return True

#validar hexadecimal

def validar_hexadecimal(numero):
    cont=0
    conte=0
    if str(numero)=="":
        return False
    for i in numero:
        print(i)
        if i=="A":
            cont+=1
        elif i=="B":
            cont+=1
        elif i=="C":
            cont+=1
        elif i=="D":
            cont+=1
        elif i=="E":
            cont+=1
        elif i=="F":
            cont+=1
        else:
            if i.isnumeric()==False:
                return False
            else:
                cont+=1
        
    if cont!=0:
        return True       
    

#pagina principal
def main(page:ft.Page):
    page.title="proyecto 1 de calculo numerico"
    page.window_width=600
    page.window_height=600
    page.padding=0
    
    
    #funcion que permite cambiar las distintas vistas de la pagina
    def cambiar_pagina(e: RouteChangeEvent):
        #funcion que imprime en el campo de texto los numeros convertidos
        def evento_convertir(e):
            if str(lista_convertir)!=str(str(lista_convertidos)):
                if str(lista_convertir.value)=="de binario" and str(lista_convertidos.value)=="a ternario":
                    if validar_binario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(binario_ternario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()

                elif str(lista_convertir.value)=="de binario" and str(lista_convertidos.value)=="a cuaternario":
                    if validar_binario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(binario_cuaternario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de binario" and str(lista_convertidos.value)=="a octal":
                    if validar_binario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(binario_octal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de binario" and str(lista_convertidos.value)=="a decimal":
                    if validar_binario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(binario_decimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de binario" and str(lista_convertidos.value)=="a hexadecimal":
                    if validar_binario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(binario_hexadecimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de ternario" and str(lista_convertidos.value)=="a binario":
                    if validar_ternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(ternario_binario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de ternario" and str(lista_convertidos.value)=="a cuaternario":
                    if validar_ternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(ternario_cuaternario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de ternario" and str(lista_convertidos.value)=="a octal":
                    if validar_ternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(ternario_octal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de ternario" and str(lista_convertidos.value)=="a decimal":
                    if validar_ternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(ternario_decimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de ternario" and str(lista_convertidos.value)=="a hexadecimal":
                    if validar_ternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(ternario_hexadecimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de cuaternario" and str(lista_convertidos.value)=="a binario":
                    if validar_cuaternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(cuaternario_binario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de cuaternario" and str(lista_convertidos.value)=="a ternario":
                    if validar_cuaternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(cuaternario_ternario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de cuaternario" and str(lista_convertidos.value)=="a octal":
                    if validar_cuaternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(cuaternario_octal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de cuaternario" and str(lista_convertidos.value)=="a decimal":
                    if validar_cuaternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(cuaternario_decimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de cuaternario" and str(lista_convertidos.value)=="a hexadecimal":
                    if validar_cuaternario(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(cuaternario_hexadecimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de octal" and str(lista_convertidos.value)=="a binario":
                    if validar_octal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(octal_binario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de octal" and str(lista_convertidos.value)=="a ternario":
                    if validar_octal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(octal_ternario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de octal" and str(lista_convertidos.value)=="a cuaternario":
                    if validar_octal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(octal_cuaternario(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de octal" and str(lista_convertidos.value)=="a decimal":
                    if validar_octal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(octal_decimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de octal" and str(lista_convertidos.value)=="a hexadecimal":
                    if validar_octal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str(octal_hexadecimal(int(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de decimal" and str(lista_convertidos.value)=="a binario":
                    if validar_decimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=invertir((decimal_binario(int(campo_texto_ingresar.value))))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de decimal" and str(lista_convertidos.value)=="a ternario":
                    if validar_decimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=invertir((decimal_terciario(int(campo_texto_ingresar.value))))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de decimal" and str(lista_convertidos.value)=="a cuaternario":
                    if validar_decimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=invertir((decimal_cuaternario(int(campo_texto_ingresar.value))))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de decimal" and str(lista_convertidos.value)=="a octal":
                    if validar_decimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=invertir((decimal_octal(int(campo_texto_ingresar.value))))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de decimal" and str(lista_convertidos.value)=="a hexadecimal":
                    if validar_decimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=invertir((decimal_hexadecimal(int(campo_texto_ingresar.value))))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de hexadecimal" and str(lista_convertidos.value)=="a binario":
                    if validar_hexadecimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str((hexadecimal_binario(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de hexadecimal" and str(lista_convertidos.value)=="a ternario":
                    if validar_hexadecimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str((hexadecimal_ternario(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de hexadecimal" and str(lista_convertidos.value)=="a cuaternario":
                    if validar_hexadecimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str((hexadecimal_cuaternario(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de hexadecimal" and str(lista_convertidos.value)=="a octal":
                    if validar_hexadecimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str((hexadecimal_octal(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                elif str(lista_convertir.value)=="de hexadecimal" and str(lista_convertidos.value)=="a decimal":
                    if validar_hexadecimal(str(campo_texto_ingresar.value))==True:
                        campo_texto_resultados.value=str((hexadecimal_decimal(campo_texto_ingresar.value)))
                        page.update()
                    else:
                        campo_texto_resultados.value="error"
                        page.update()
                else:
                    campo_texto_resultados.value="error"
                    page.update()

            else:
                campo_texto_resultados.value="error"
                page.update()
                    
        #funcion que controla cuando el modo es automatico o manual. si es automatico se desactiva el campo de texto y 
        #el boton ingresar, de lo contrario se activan los controles anteriores        
        def cambio_automatico(e):
            if str(lista_automatico.value)=="automatico":
                boton_agregar.disabled=True
                campo_texto_ingresar2.disabled=True
                boton_ejecutar.disabled=False
                page.update()
            else:
                boton_agregar.disabled=False
                campo_texto_ingresar2.disabled=False
                boton_ejecutar.disabled=True
                page.update()
        #funcion que controla que tipo de dimension tiene la matriz a la que se le va a agregar los valores 
        def agregar(e:ControlEvent):
            cont_validar=0
            if campo_texto_ingresar2.value=="":
                cont_validar+=1
            else:
                for i in campo_texto_ingresar2.value:
                    #validamos que los elementos de la matriz no sean caracteres extraños o una cadena de texto
                    if i=="," or i.isnumeric()==True or i=="." or i=="-" or i==" " or campo_texto_ingresar2.value=="":
                        pass
                    else:
                        cont_validar+=1
            if cont_validar==0:
                if lista_dimension.value=="2X2":
                    global fila_actual1
                    global cont1
                    #valores_matriz es una lista que contiene los valores actuales de la fila que se introducio en el campo de texto, que luego se le asigna a la
                    #matriz de 0 y se vuelve a actualizar cuando introducimos otra fila
                    valores_matriz=campo_texto_ingresar2.value.split(",")
                    valores_matriz = [float(valor.strip()) for valor in valores_matriz]
                    #validacion que nos permite saber si se introducieron mas menos datos de los que admite la dimension de la matriz
                    if len(valores_matriz)==3:
                        #validacion que nos permite parar de ingresar valores cuando la matriz ya este llena respecto a su dimension
                        if cont1==1:
                            boton_agregar.disabled=True
                            boton_ejecutar.disabled=False
                            campo_texto_ingresar2.value=""
                            page.update()
                        #de lo contrario se agregan los valores a la matriz
                        cont1+=1
                        matriz1[fila_actual1]=valores_matriz[:3]
                        fila_actual1=(fila_actual1+1)
                        campo_texto_ingresar2.value=""
                    
                        page.update()
                    elif len(valores_matriz)<3:
                        area_texto.value="ingrese al menos 3 valores "  
                        page.update() 
                    else:
                        area_texto.value="este numero de valores rebasa la dimension de la matriz "  
                        page.update() 
            
                elif lista_dimension.value=="3X3":
                    global fila_actual2
                    global cont2
                    valores_matriz=campo_texto_ingresar2.value.split(",")
                    valores_matriz = [float(valor.strip()) for valor in valores_matriz]
                    if len(valores_matriz)==4:
                        if cont2==2:
                            boton_agregar.disabled=True
                            boton_ejecutar.disabled=False
                            campo_texto_ingresar2.value=""
                            
                            page.update()
                        cont2+=1
                        matriz2[fila_actual2]=valores_matriz[:4]
                    
                        fila_actual2=(fila_actual2+1)
                        campo_texto_ingresar2.value=""
                    
                        page.update()
                    elif len(valores_matriz)<4:
                        area_texto.value="ingrese al menos 4 valores "  
                        page.update() 
                    else:
                        area_texto.value="este numero de valores rebasa la dimension de la matriz "  
                        page.update()
                elif lista_dimension.value=="4X4":
                    global fila_actual3
                    global cont3
                    valores_matriz=campo_texto_ingresar2.value.split(",")
                    valores_matriz = [float(valor.strip()) for valor in valores_matriz]
                    if len(valores_matriz)==5:
                        if cont3==3:
                            boton_agregar.disabled=True
                            boton_ejecutar.disabled=False
                            campo_texto_ingresar2.value=""
                            
                            page.update()
                        cont3+=1
                        matriz3[fila_actual3]=valores_matriz[:5]
                    
                        fila_actual3=(fila_actual3+1)
                        campo_texto_ingresar2.value=""
                    
                        page.update()
                    elif len(valores_matriz)<5:
                        area_texto.value="ingrese al menos 5 valores "  
                        page.update() 
                    else:
                        area_texto.value="este numero de valores rebasa la dimension de la matriz "  
                        page.update()
                elif lista_dimension.value=="5X5":
                    global fila_actual4
                    global cont4
                    valores_matriz=campo_texto_ingresar2.value.split(",")
                    valores_matriz = [float(valor.strip()) for valor in valores_matriz]
                    if len(valores_matriz)==6:
                        if cont4==4:
                            boton_agregar.disabled=True
                            boton_ejecutar.disabled=False
                            campo_texto_ingresar2.value=""
                            page.update()
                        cont4+=1
                        matriz4[fila_actual4]=valores_matriz[:4]
                    
                        fila_actual4=(fila_actual4+1)
                        campo_texto_ingresar2.value=""
                    
                        page.update()
                 
                    elif len(valores_matriz)<6:
                        area_texto.value="ingrese al menos 6 valores "  
                        page.update() 
                    else:
                        area_texto.value="este numero de valores rebasa la dimension de la matriz "  
                        page.update()
            else:
                area_texto.value="error, se ingreso algo incorrecto o el campo de texto esta vacio"  
                page.update()
        #funcion que ejecuta el metodo gauss jordan en una matriz NXN y a su vez mostramos el proceso en el campo de texto
        #junto con los resultados
        def gauss_jordan(A, b):
            #unimos la matriz de resultados y la matriz de coeficientes
            Ab = np.concatenate((A, b.reshape(-1, 1)), axis=1)
            n = len(Ab)
           
            cadena="MATRIZ AMPLIADA \n\n"
            #guardamos en cadena la matriz original
            for i in Ab:
                cadena+=str(i)+"\n"
            cadena+="-----------------------------------------\n"    
            #ciclo que transforma la matriz en una triangular superior con solo 1's en la diagonal principal
            for i in range(n):
                Ab[i] /=Ab[i][i]
                for j in range(i+1, n):
                    factor = Ab[j][i]
                    Ab[j] -= factor * Ab[i]
                for l in Ab:
                     cadena+=str(l)+ "\n"
                cadena+="-----------------------------------------\n"
    

            #ciclo que transforma a la matriz en la matriz identidad
            for i in range(n-1, -1, -1):
                for j in range(i-1, -1, -1):
                    factor = Ab[j][i]
                    Ab[j] -= factor * Ab[i]
                for l in Ab:
                     cadena+=str(l)+ "\n"
                cadena+="-----------------------------------------\n"

            cadena+="\nsoluciones\n\n"
            #ciclo que agrega las soluciones a la matriz de soluciones
            solucion=[]
            for i in range(0,len(Ab[0])-1):
                solucion.append(Ab[i][len(Ab[0])-1])
                
            r=0
            for i in solucion:
                cadena+=f"x{r+1}={str(i)}\n"
                r+=1
            area_texto.value=cadena
            area_texto.update()
            
    
        def gauss_jordan2(A):
            Ab = A
            n = len(Ab)
            print(n)
            cadena="MATRIZ AMPLIADA \n\n"
            for i in Ab:
                cadena+=str(i)+"\n"
            cadena+="-----------------------------------------\n"    
            for i in range(n):  
                Ab[i]/=Ab[i][i]
                for j in range(i+1, n):
                    factor = Ab[j][i]
                    Ab[j] -= factor * Ab[i]
                for l in Ab:
                     cadena+=str(l)+ "\n"
                cadena+="-----------------------------------------\n"
    

    
            for i in range(n-1, -1, -1):
                for j in range(i-1, -1, -1):
                    factor = Ab[j][i]
                    Ab[j] -= factor * Ab[i]
                for l in Ab:
                     cadena+=str(l)+ "\n"
                cadena+="-----------------------------------------\n"

            cadena+="\nsoluciones\n\n"
        
            solucion=[]
            for i in range(0,len(Ab[0])-1):
                solucion.append(Ab[i][len(Ab[0])-1])
            r=0
            for i in solucion:
                cadena+=f"x{r+1}={str(i)}\n"
                r+=1
            area_texto.value=cadena
            area_texto.update()
        #funcion ejecuta las funciones correspondientes para mostrar la informacion de la matriz y sus resultados en pantalla         
        def ejecucion(n):
            global cont1
            global cont2
            global cont3
            global cont4
            global matriz1
            global matriz2
            global matriz3
            global matriz4
            global fila_actual1
            global fila_actual2
            global fila_actual3
            global fila_actual4

            #validacion que nos permite saber si estamos trabajando en modo automatico o manual
            if lista_automatico.value=="automatico":
                if lista_dimension.value=="2X2":
                    a=np.random.randint(1,9,(2,2)).astype(float)
                    b=np.random.randint(1,9,(2))
                    gauss_jordan(a.copy(),b.copy())
                elif lista_dimension.value=="3X3":
                    a=np.random.randint(1,9,(3,3)).astype(float)
                    b = np.random.randint(1, 9,(3))
                    gauss_jordan(a.copy(),b.copy())
                elif lista_dimension.value=="4X4":
                    a=np.random.randint(1,9,(4,4)).astype(float)
                    b = np.random.randint(1, 9,(4))
                    gauss_jordan(a.copy(),b.copy())
                elif lista_dimension.value=="5X5":
                    a=np.random.randint(1,9,(5,5)).astype(float)
                    b = np.random.randint(1, 9,(5))
                    gauss_jordan(a.copy(),b.copy())
            else:
                if lista_dimension.value=="2X2":
                    gauss_jordan2(matriz1.copy())
                    matriz1 = np.zeros((2,3)).astype(float)
                    boton_ejecutar.disabled=True
                    boton_agregar.disabled=False
                    fila_actual1=0
                    cont1=0
                    campo_texto_ingresar2.value=""
                    page.update()
                elif lista_dimension.value=="3X3":
                    gauss_jordan2(matriz2.copy())
                    matriz2 = np.zeros((3,4)).astype(float)
                    boton_ejecutar.disabled=True
                    boton_agregar.disabled=False
                    fila_actual2=0
                    cont2=0
                    campo_texto_ingresar2.value=""
                    page.update()
                elif lista_dimension.value=="4X4":
                    gauss_jordan2(matriz3.copy())
                    matriz3 = np.zeros((4,5)).astype(float)
                    boton_ejecutar.disabled=True
                    boton_agregar.disabled=False
                    fila_actual3=0
                    cont3=0
                    campo_texto_ingresar2.value=""
                    page.update()
                elif lista_dimension.value=="5X5":
                    gauss_jordan2(matriz4.copy())
                    matriz4 = np.zeros((5,6)).astype(float)
                    boton_ejecutar.disabled=True
                    boton_agregar.disabled=False
                    fila_actual4=0
                    cont4=0
                    campo_texto_ingresar2.value=""
                    page.update()

        #lista desplegable que nos permite elegir desde que tipo de base numerica vamos a convertir
        lista_convertir = ft.Dropdown(
                                label="Elige una opcion",
                                width=200,
                                options=[
                                    ft.dropdown.Option("de binario"),
                                    ft.dropdown.Option("de ternario"),
                                    ft.dropdown.Option("de cuaternario"),
                                    ft.dropdown.Option("de octal"),
                                    ft.dropdown.Option("de decimal"),
                                    ft.dropdown.Option("de hexadecimal")
                                ],
                                
                            
                            )  
        #lista desplegable que nos permite elegir hasta que base numerica vamos a convertir
        lista_convertidos=ft.Dropdown(
                                label="Elige una opcion",
                                width=200,
                                options=[
                                    ft.dropdown.Option("a binario"),
                                    ft.dropdown.Option("a ternario"),
                                    ft.dropdown.Option("a cuaternario"),
                                    ft.dropdown.Option("a octal"),
                                    ft.dropdown.Option("a decimal"),
                                    ft.dropdown.Option("a hexadecimal")
                                ],
                                
                            )
        #boton que permite convertir el numero introducido en el campo de texto, el cual incluto el metodo evento convertir que se encarga de las operaciones
        boton_convertir=ElevatedButton(text="convertir",width=150,on_click=evento_convertir)
        #lista desplegable que nos permite elegir el modo en el que queremos crear las matrices
        lista_automatico=ft.Dropdown(
                                label="Elige el modo",
                                width=150,
                                options=[
                                    ft.dropdown.Option("automatico"),
                                    ft.dropdown.Option("manual"),
                                    
                                ],
                                on_change=cambio_automatico
                                
                            )
        #lista desplegable que nos permite elegir la dimension de la matriz que queremos introducir
        lista_dimension=ft.Dropdown(
                                label="Elige la dimension",
                                width=150,
                                options=[
                                    ft.dropdown.Option("2X2"),
                                    ft.dropdown.Option("3X3"),
                                    ft.dropdown.Option("4X4"),
                                    ft.dropdown.Option("5X5"),
                                ],
                                
                            )
        #campo de texto en donde ingresamos los valores de las matrices
        campo_texto_ingresar2=ft.TextField(label="ingresa las filas",text_align=ft.TextAlign.LEFT,width=150)
        #area de texto en donde se muestra el proceso de eliminacion de gauss jordan y los resultados correspondientes
        area_texto=ft.TextField(label="resultados",width=450,height=270,multiline=True,read_only=True)
        #boton que agrega la fila que introducimos en campo_texto_ingresar2 a la matriz
        boton_agregar=ft.ElevatedButton(text="agregar",width=100,on_click=agregar)
        #boton que maneja el evento on_click que llama a la funcion ejecucion
        boton_ejecutar=ft.ElevatedButton(text="ejecutar",width=100,on_click=ejecucion)
        #campo de texto que muestra los numeros convertidos
        campo_texto_resultados=ft.TextField(label="resultados",width=200,height=100,read_only=True,text_align=ft.TextAlign.CENTER)
        #campo de texto que permite ingresar unicamente numeros enteros para su posterior conversion
        campo_texto_ingresar=ft.TextField(label=f"ingrese un numero entero",text_align=ft.TextAlign.LEFT, width=200,value="")
        #limpiamos las vistas
        page.views.clear()
        page.views.append(
            View(
                route="/",
                controls=[
                    #control que nos permite regresar a la pagina principal
                    AppBar(title=Text("principal"),bgcolor=ft.colors.BLUE),
                    #boton que nos lleva a la vista del convertor de numeros
                    ElevatedButton(text="convertor de numeros",on_click=lambda _:page.go("/convertor"),width=300,height=100),
                    #boton que nos lleva al programa de matrices
                    ElevatedButton(text="programa de matrices",on_click=lambda _:page.go("/matrices"),width=300,height=100),
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=50
                
            )
        )
        #validamos que el boton de convertir numeros se haya ingresado, si es asi esto nos llevara a la vista del convertor de numeros
        if page.route=="/convertor":
            page.views.append(
            View(
                route="/convertor",
                #agregamos los controles a la pagina
                controls=[
                    AppBar(title=Text("convertor de numeros"),bgcolor=ft.colors.PINK_ACCENT),
                    ft.Row(
                        controls=[
                            lista_convertir,
                            lista_convertidos
                        ],
                        spacing=40, alignment=MainAxisAlignment.CENTER        
                    ),
                    campo_texto_ingresar,boton_convertir,campo_texto_resultados
                    
                    
                    
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=50
                
                )

            )
         #validamos que el boton de matrices se haya ingresado, si es asi esto nos llevara a la vista del programa de matrices
        if page.route=="/matrices":
            page.views.append(View(
                route="/matrices",
                controls=[
                    AppBar(title=Text("metodo Gauss-Jordan"),bgcolor=ft.colors.PINK_ACCENT),
                    ft.Row(
                        controls=[
                            lista_dimension,lista_automatico,campo_texto_ingresar2
                        ],
                        spacing=25, alignment=MainAxisAlignment.CENTER        
                    ),
                    ft.Row(
                        controls=[
                            boton_agregar,boton_ejecutar
                        ]
                        ,spacing=25,alignment=MainAxisAlignment.CENTER
                    ),
                    area_texto
                    

                    
                    
                    
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=50
                
                ))

            
        #actualizamos la pagina para que se apliquen los cambios 
        page.update()
    def pop(e:ViewPopEvent):
        page.views.pop()
        vista: View=page.views[-1]
        page.go(vista.route)
    #cuando la ruta cambie ejecutamos el metodo cambiar pagina
    page.on_route_change=cambiar_pagina
    page.on_view_pop=pop
    page.go(page.route)

if __name__ == '__main__':
    ft.app(target=main)
