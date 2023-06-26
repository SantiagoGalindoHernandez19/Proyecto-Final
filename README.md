# Proyecto-Final

NOMBRE DE LOS INTEGRANTES:
---
-Santiago Diaz Devia 

-Santiago Galindo Hernandez 

NOMBRE DEL GRUPO: 
--
Los siembramaticas

PROYECTO: 
---
Ahorcado 

---


LOGO:
---
![LOGO](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/750f81e9-0183-4ed8-8109-a1c92f1d0dac)

---

FUNCIONAMIENTO
---
Ahorcado el cual cuenta con 4 paneles de inicio ( Jugar, Instrucciones, Ajustes, Salir). El banco de palabras es modificable, puesto que, cuenta con una base de datos en donde a partir de unos arhivos de texto, lee las palabras y te dara opciones para jugar con esas mismas palabras. En la accion de jugar tendra 6 intentos para adivinar la palabra y por correspondiente ganar el juego, antes de que el  hangman muera. El segundo panel explicara el funcionamiento a detalle de como ingresar en los diferentes grupos de palabras, puesto que el panel de ajustes sera el propiamente indicado para salvaguardar esta base de datos con una contraseña ya antes establecida, asimismo permite modificar, crear y eliminar dichos grupos anteriormente; y el ultimo panel permite terminar el programa. Al momento de iniciar el programa se tendran 10 segundos de preparacion para iniciar el juego, a su vez se tiene un contador del tiempo transcurrido en su juego.

---


DIAGRAMAS
---

![image (5)](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/91ce427a-5e82-479d-9630-f36c5450d094)
![image (9)](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/55087089-9a52-4944-92b7-d83c4aaa8f51)
![image (7)](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/d8c30fe2-16d0-46c9-abaf-472024e561b2)
![image (8)](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/aa51df31-1395-4e23-b017-e5fc796262bd)


PROCEDIMIENTO
---

FUNCION PRINCIPAL 

Esta es nuestra funcion principal la cual se encarga preparar el archivo de todos los grupos, lo que hace la funcion preparar el archivo esque si no existe el archivo lo abre y lo crea como una cadena vacia. La funcion de menu fue desarrollada con ayuda de condicionales y diferentes strings 

![FUNCION PRINCIPAL](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/521b618d-82b9-41b1-b8f2-72747d1329fd)
![PREPARAR ARCHIVO](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/0335c47d-ae71-4df6-aaeb-457b8b5c147e)
![Captura](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/e6c46ee8-7c47-4deb-9ae6-c8644faf8cfd)

---

La funcion declarar grupos lo que hace es declarar una lista vacia, abre el archivo quitandole el salto de linea y agregamos a grupos la linea, del mismo modo funciona la definición argumentos de grupo. En la funcion eliminar grupo de palabras por pantalla va a imprimir la lista de grupos y le pregunta al usuario cual va a escoger 

![ELIMINAR GRUPO DE PALABRAS](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/8dcffd8b-b5ff-49d2-9f0c-259a1943f916)


---

La definicion escribir grupos lo que hace es borrar todo lo que se, de esta manera cuando le enviemos el archivo de grupo ya modificados, volvera a escribir todo el arreglo dando impresion de que se ha eliminado. 

![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/f4aa692c-84ad-4096-a93a-9b44e9f0a704)

---

La definicion de jugar, en primera instancia se pondra en global las letras y los intentos para poder modificarlas, las letras escritas que ya probo el jugador se reinician a nada 

![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/36e3c608-3db4-4bf9-8c4c-239a1db02f02)

---

La definicion preparar palabra, lleva lo que lleva el usuario adivinado, por cada letra que haya en la palabra original, vamos agregarle a la palabra adivinada dos cosas un diccionario que contendra la letra y adivinada con false or true 

![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/491f02ef-e1e5-4e05-9cb5-078380cf904d)


---

Lo que hace imprimir palabra esque por cada letra compuesta por la palabra adivinada si ya esta adivinada esta en true entonces imprimimos lo que hay en letra y si no imprimimos el guion
![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/c8530de1-63ca-4aa4-bf2a-835d05f1adc9)

---

La definicion descubrir letra, lo que hace hace todo global para modificarlo, si la letra de usuario esta en las letras escritas regresa, porque ya lo habia intentando pues de esta manera no bajara vidas, si no le restamos un intento

![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/6f979521-b3d5-43ae-aab0-ee6c6d41e57c)

---

La definicion de ha ganado lo que hace es que recorre toda la palabra adivinada 

![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/59999aed-942b-462f-aa8d-d06696a3bd15)

---

El ultimo codigo a explicar es el muñeco de ahorcado segun los intentos realizados

![image](https://github.com/SantiagoGalindoHernandez19/Proyecto-Final/assets/124641609/615a9e38-b69c-4a82-b0e9-31ee9735bdf9)



