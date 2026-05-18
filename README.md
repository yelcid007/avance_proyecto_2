# avance_proyecto_2

ASISTENTE EXPERTO BASADO EN RAG 

 

 

Se creo un agente de ia, con un modelo llama3.2:1b instalado localmente. 

<img width="452" height="462" alt="image" src="https://github.com/user-attachments/assets/859f3972-0a80-45a1-8c5e-46ad2cd46b32" />

Aqui tenemos en cuenta la distancia semantica para condicionarla respuesta, y adicional le damos contexto con un promp establecido en el archivo prompt.py 

<img width="595" height="521" alt="image" src="https://github.com/user-attachments/assets/84b88202-e886-4cdb-89e7-7eb7b5cc754e" />

Este es el prompt: 

 <img width="599" height="200" alt="image" src="https://github.com/user-attachments/assets/f972d948-5054-4bcb-8a9d-a2e5d041a877" />

En esta parte del codigo hacemos la vectorizacion, para convertir los caracteres en vectores: 

 <img width="596" height="214" alt="image" src="https://github.com/user-attachments/assets/abfdfd3a-0a2d-4345-a87f-2021507166f4" />


En esta parte del codigo almacenamos los vectopres en una base de datos vectorial llamada chroma_db 

<img width="590" height="510" alt="image" src="https://github.com/user-attachments/assets/2bf6544a-f2c8-419a-a135-9ceeb357e9d4" />

Aqui creamos los chunks para hacer mas facil la semantica del documento: 

<img width="524" height="376" alt="image" src="https://github.com/user-attachments/assets/8506d268-2505-4469-9af1-c25ef5d5d7db" />

Cuando corremos este archivo ingest.py, hacemos que se lean los pdf, se creen los chunks y se organice la informacion para luego consultarla cuando interactuemos con el modelo: 

 <img width="559" height="511" alt="image" src="https://github.com/user-attachments/assets/30839901-1858-4277-bffd-3d04a49ba40b" />

En este archivo creamos la simulacion del bot para poder interactuar con el modelo: 

<img width="601" height="536" alt="image" src="https://github.com/user-attachments/assets/3a75b783-2d03-4998-ad1f-52075fcea803" />

 
