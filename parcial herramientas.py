def cafeteria():
        print("La boqueria")
        print("Bienvenido/a")
        print("¿Desea pedir algo?")
        respuesta= input()
        ans= True
        while respuesta == "si" and ans== True:
                
                print("¿Es usted profesor o estudiante?")
                rol= input()
                if rol == "estudiante":
                    print("¿Es del programa de becas?")
                    becas= input()
                    if becas == "si":
                         print("Ingrese su numero de documento:")
                         cedula= int(input())
                         print("Que desea pedir?")
                         producto= input()
                         print("Digite el codigo del producto")
                         codigo= input()
                         print("¿cuanto cuesta?")
                         costo= int(input())
                         print("¿cuantas unidades desea pedir?")
                         cantidad= int(input())
                         total= int((cantidad * costo)* 0.5)             
           
                    else:
                        print("Ingrese su numero de documento:")
                        cedula= int(input())
                        print("¿Que desea pedir?")
                        producto= input()
                        print("Digite el codigo del producto")
                        codigo= input()
                        print("¿cuanto cuesta?")
                        costo= int(input())
                        print("¿cuantas unidades desea pedir?")
                        cantidad= int(input())
                        total= int((cantidad * costo)* 0.7)                                      
                        
                else:
                      print("Ingrese su numero de documento:")
                      cedula=int(input())
                      print("¿Que desea pedir maestro/a?")
                      res= input()
                      print("Digite el codigo del producto")
                      codigo= input()
                      print("¿cuanto cuesta?")
                      costo= int(input())
                      print("¿cuantas unidades desea pedir?")
                      cantidad= int(input())
                      total= int((cantidad * costo)* 0.8)

                print("el",rol, "con cedula:", cedula, "debe pagar un total de:", total,"por el producto de codigo:", codigo)
                print("")
                print("siguiente en la fila por favor, ¡vuelva pronto!")
                print("")
                print("¿Desea pedir algo?")
                respuesta= input()                                
                        
        if respuesta== "no":
           ans= False
           print("Vuelva pronto")

cafeteria()
