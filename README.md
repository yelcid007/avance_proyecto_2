# avance_proyecto_2

ASISTENTE EXPERTO BASADO EN RAG 

 

 

Se creo un agente de ia, con un modelo llama3.2:1b instalado localmente. 

 

Aqui tenemos en cuenta la distancia semantica para condicionarla respuesta, y adicional le damos contexto con un promp establecido en el archivo prompt.py 

 

Este es el prompt: 
 

 

 

 

 

En esta parte del codigo hacemos la vectorizacion, para convertir los caracteres en vectores: 
 

En esta parte del codigo almacenamos los vectopres en una base de datos vectorial llamada chroma_db 

 

Aqui creamos los chunks para hacer mas facil la semantica del documento: 
 

Cuando corremos este archivo ingest.py, hacemos que se lean los pdf, se creen los chunks y se organice la informacion para luego consultarla cuando interactuemos con el modelo: 

 

En este archivo creamos la simulacion del bot para poder interactuar con el modelo: 
 
