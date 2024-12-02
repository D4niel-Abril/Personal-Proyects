rtaante = False


while True:
    if rtaante:
        print("El resultado anterior es: ", rta)
        numero1 = rta
    else:
        numero1 = int(input("ingrese el primer numero: "))
    while True:
        operacion = input("Quieres hacer una suma(+), resta(-) multiplicacion(*), division(/) o potenciacion(**) (solo escribe el signo) ")
        if operacion in ["+", "-", "*", "/","**"]:
            break
        else:
            print("Operacion no valida, intentalo de nuevo: ")
    numero2 = int(input("ingrese el segundo numero: "))
    if operacion == "+":
        rta = numero1 + numero2
    elif operacion == "-":
        rta = numero1 - numero2
    elif operacion == "*":
        rta = numero1 * numero2
    elif operacion == "/":
        if numero1 == 0 or numero2 == 0:
            print("No se puede usar el 0 en una division:")
            rta = 0
        rta = numero1 / numero2
    elif operacion == "**":
        rta = numero1 ** numero2
    print(rta)
    rtaanterior = input("quieres usar el resultado de esta operacion ahora? ")
    if rtaanterior == "si":
        rtaante = True
    else:
        rtaante = False    
    salir = input ("Quieres realizar otra operacion? ")
    if salir == "si":
        print("Sigamos!!")
    else:
        print("Hasta pronto ")
        break  
    