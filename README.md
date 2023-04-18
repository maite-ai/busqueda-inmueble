# Práctica de Python

## Consigna/enunciado

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:
Zona A: precio = (metros _ 1000 + habitaciones _ 5000 + garaje _ 15000) _ (1-antiguedad/100)
Zona B: precio = (metros _ 1000 + habitaciones _ 5000 + garaje _ 15000) _ (1-antiguedad/100) \* 1.5

## Ejecución

Ingresá al [repl de este código](https://replit.com/@peirios/Juego-de-la-Ultima-Piedra) para probar cómo funciona.
