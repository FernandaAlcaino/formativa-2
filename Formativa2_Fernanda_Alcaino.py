
valor_total = 0 
pikachu = 0
otaku = 0
pulpo = 0
anguila = 0
descuento = 0

while True:
    try:
        print(f"carrito: ${valor_total}")
        print("1) pikachu roll, 4.500")
        print("2) otaku roll, 5.000")
        print("3) pulpo venenoso roll, 5.200")
        print("4) anguila electrica roll, 4.800")
        print("5) terminar mi pedido")

        opc =int(input("ingrese una opcion: "))
        
        if opc == 1:
            valor_total += 4500
            pikachu += 1
            print("has agregado un pikachu roll")
        elif opc == 2:
            valor_total += 5000
            otaku += 1
            print("has agregado un otaku roll")
        elif opc == 3:
            valor_total += 5200
            pulpo += 1
            print("has agregado un pulpo venenoso roll")
        elif opc == 4:
            valor_total += 4800
            anguila += 1
            print("has agregado un anguila electrica roll")
        elif opc == 5:
            print("has terminado tu pedido")
            break
    except:
        print("ha ocurrido un error, ingrese nuevamente")

print("1) si")
print("2) no")
tienecodigo =int(input("tienes un codigo de descuento?"))

if tienecodigo == 1:
    while True:
        try:
            codigo = str (input("ingrese su codigo")) 
            if codigo == "soyotaku":
                descuento += 10
                print("obtuviste un descuento del 10%")
                break
            elif codigo == "x":
                print("has salido")
                break
            else:  
                print("codigo no valido")
                print("x) salir")
            
        except:
            print("ha ocurrido un error, ingrese nuevamente")
        
elif tienecodigo == 2:
    print("no tienes descuento")

descuento_final = descuento * valor_total / 100

print(f""" 
Pikachu Roll : {pikachu}  Otaku Roll : {otaku} 
Pulpo Venenoso Roll: {pulpo}   Anguila Eléctrica Roll: {anguila} 
****************************** 
Total de productos: {pikachu + otaku + pulpo +anguila}
Subtotal por pagar: ${valor_total}
Descuento por código: ${descuento_final}
TOTAL: ${valor_total - descuento_final}
      """)
    
        
    