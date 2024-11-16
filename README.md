# Proyecto de Detección de Objetos en Tiempo Real

Este proyecto utiliza OpenCV para la detección de objetos en tiempo real a través de la cámara web. El sistema detecta cambios en la escena y registra los tiempos de inicio y fin en los que un objeto es detectado. Este proyecto fue realizado con el propósito de practicar Python y las bibliotecas que utilicé.

## Descripción del proyecto

El código captura imágenes en tiempo real desde la cámara web y las procesa para detectar movimientos o cambios significativos en la escena. Cuando se detecta un objeto en movimiento, se guarda el tiempo de inicio y fin de la detección en un archivo CSV. El proyecto emplea técnicas de procesamiento de imágenes como la conversión a escala de grises, la difuminación gaussiana, y la detección de contornos para identificar y resaltar los objetos en movimiento.

## Requisitos

Para ejecutar este proyecto, necesitas tener instaladas las siguientes librerías:

* ```OpenCV```: para el procesamiento de imágenes y la captura de video.
* ```Pandas```: para almacenar los tiempos de detección en un archivo CSV.

Puedes instalar las dependencias con:

    pip install opencv-python pandas

## Funcionamiento

El programa captura video desde la cámara web.
Convierte cada cuadro a escala de grises y aplica un desenfoque para reducir el ruido.
Calcula la diferencia entre el primer cuadro (cuadro de referencia) y los cuadros posteriores.
Detecta los contornos en las diferencias de las imágenes y resalta los objetos en movimiento con un rectángulo verde.
Cuando se detecta un objeto en movimiento, se registran los tiempos de inicio y fin de la detección.
Los tiempos de inicio y fin de cada detección se almacenan en un archivo ```Times.csv```.

## Uso

1. Ejecuta el script en tu entorno local.
2. La ventana de video mostrará cuatro vistas:
    * "Gray Frame": Imagen en escala de grises.
    * "Delta Frame": Diferencia entre el cuadro actual y el cuadro de referencia.
    * "Threshold Frame": Imagen binaria para detectar los cambios.
    * "Color Frame": Imagen con los contornos dibujados alrededor de los objetos detectados.
3. Cuando desees terminar la ejecución del programa, presiona la tecla q. Si hay un objeto detectado, se guardará la hora final de la detección.

## Resultados

Los tiempos de detección se guardarán en un archivo CSV llamado Times.csv, en el que cada fila contiene:

* Inicio: El momento en que se detecta un objeto.
* Fin: El momento en que el objeto deja de ser detectado.

Ejemplo de un archivo CSV generado:
    
    Inicio,Fin
    2024-11-15 12:00:01,2024-11-15 12:00:05
    2024-11-15 12:02:15,2024-11-15 12:02:30

