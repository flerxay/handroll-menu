pedido = []
total_pedido = 0
descuento_aplicado = False

while True:
  print("-----DELIVERY SUSHI-----")
  print("""
     _________________________________________
    |    1.- Pikachu Roll      |$4500         |
    |    2.- Otaku Roll        |$5000         |
    |    3.- Pulpo Venenoso Roll |$5200       |
    |    4.- Anguila Eléctrica Roll |$4800    |
    |_________________________________________|
    """)
  opcion = input("Elija una opción (1-4): ")
    
    if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":

        if opcion == "1":
            total_pedido += 4500
        elif opcion == "2":
            total_pedido += 5000
        elif opcion == "3":
            total_pedido += 5200
        elif opcion == "4":
            total_pedido += 4800
        pedido.append(opcion)
    else:
        print("ERROR. Ingrese una opción válida (1-4)")

    sino = input("¿Desea agregar algo más? (si/no): ")
    if sino.lower() == "si":
        continue 
    elif sino.lower() == "no":
        break
    else:
        print("ERROR. Ingrese 'si' o 'no'")

codigo_descuento = input("¿Tiene un código de descuento? Ingrese el código: ")
if codigo_descuento.lower() == "soytuakki" and not descuento_aplicado:
    print("Código correcto. Se le aplicará un descuento del 10%")
    total_pedido *= 0.9
    descuento_aplicado = True
else:
    print("Código incorrecto o no ix    ngresado.")

print(f"El total de su pedido es: ${total_pedido}")
    
