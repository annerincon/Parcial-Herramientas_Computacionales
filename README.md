# Parcial-Herramientas_Computacionales
## **_Parcial 3 Corte - 2022-1_**  

_Anne Katherine Rincón Barrios_ 

## Contextualizacion del Parcial

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
## Documentacion de importancia
### Parte explicativa
#### ¿Que problema es?
Nos piden plantear una solucion, para simular la cafeteria de la universidad. Por lo que cada cliente debe dar las siguientes especificaciones
para cumplir con todos los parametros del problema:
- rol que cumple en la universidad.
- numero de documento.
- si pertenece al programa de becas en caso de ser estudiante.  
Luego le pide al usuario que digite cual es el producto que deseea, el codigo, el precio, y un total segun los procentajes que cumplan los parametros al cumplir con su rol estudiante o profesor:
* Estudiante con beca tiene un 50% descuento
* Estudiante normal tienen un 30%
* Los maestros tienen un 20%


## ¿Que modelo computacional lo resuelve?
Utilizamos python para resolver el problema

## ¿Que recibe como entrada?
El codigo es una funcion sin parametros donde el usuario del ingresar los datos, y se van a guardar en cada una de las variables asignadas.

## ¿cual es la salida?
El programa retorna como repuesta el recibo que se le va generar al cliente con toda su informacion y lo que debe pagar ya con los descuentos ya aplicados.

## ¿Como lo calcula?
A la variable se le asignan unas operaciones matematicas, donde se van a relacionar varias de las variables ya utilizadas en items mas arriba. 

## Preguntas frecuentes
### 1. ¿Qué tipo de errores se presentaron o se pueden presentar con su implementación al problema?  
Al plantear el problema en el código de Python pude encontrar algunos problemas de indentación, asignación de variables, o por lo menos de la posición en la que se encuentran las variables que se vayan a reiniciar una vez se terminen las iteraciones del ciclo. También tener muy presente las anidaciones, las variables que se van a retornar y lo que se debe imprimir. Hay que analizar que tanto trabajo realiza el programa, en cuestión de eficiencia y cuál es la magnitud de la cantidad de las líneas de código. Como programadores el punto clave es codificar de 15 a 20 líneas y abstenerse a una línea de ordenamiento lógico.

### 2. ¿Qué estrategias podría usar para solucionar estos errores?  
Personalmente recomendaría utilizar un editor, como guía para mejorar y depurar. Además de que hay que considerar la arquitectura del código, o puede que desde el mismo idle del lenguaje en cuestión, se logre desarrollar cierta habilidad para resolver esos problemas como práctica.  Así mismo, utilizar la denominada documentación de software para llevar un orden de lo que va a realizar el programa y ¿Por qué?
