# Parcial-Herramientas_Computacionales
## **_Parcial 3 Corte - 2022-1_**  

_Anne Katherine Rincón Barrios_  

_I semestre de ingenieria de sistemas y computación_ 
#### 1. **Ejercicio.py**
Planteamiento del problema:
las cafeterias de la universidad requieren automatizar el cobro de almuerzos brindados a la
comunidad estudiantil, por lo que han fijado precios y descuentos a cobrar dependiendo del
caso. Se desea saber entonces por cada compra cu´anto debe pagar el usuario en caja. Para ello:
Pida por teclado la siguiente información para el cliente: 
- Cédula y rol: profesor o estudiante  
- Si es estudiante pregunte si es del programa de becas  
- Registrar el producto a comprar: código producto, cantidad de unidades y precio del producto.
  (un solo producto, varias unidades, por ejemplo: producto 076: gaseosa, 3 unidades)
- Los descuentos están dados de la siguiente forma: los estudiantes tienen un 30% de descuento,
si tiene beca sería del 50% mientras que los profesores tienen un 20% de descuento.  

Al final el procedimiento por cada cliente debería _imprimir_ el valor a pagar por sus productos
de la forma: **_"El Rol con cedula Numero, debe pagar Valor por el producto Codigo"
Ejemplo: "El profesor con Cedula 1454898 debe pagar $12.900 por el producto 076"._**
Tenga en cuenta que este valor final a pagar corresponde al precio de cada producto por la
cantidad llevada menos el descuento otorgado, debe imprimir el rol y la cédula de cada cliente
y el código del producto llevado en el **mensaje**.

#### _Codigo del Ejercicio:_

```python
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

```

