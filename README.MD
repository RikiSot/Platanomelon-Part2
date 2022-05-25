# PART 2 - ML Model Deployment

Take a look at this Jupyter Notebook.

It is a simple classification model experiment on the iris dataset. Our goal is to
convert this notebook experiment into a real python application, able to perform
predictions in real time, reading input features for the model via a HTTP request.
Read the last section of the notebook for further instructions on how to work with
serialized models and the format of the input request.

The application should use Flask micro web framework (or similar technology) for
reading the HTTPrequest.
The HTTP response for the /predict route should be a JSON serialized array with the
result of the prediction, in the same order as the array of input features

### Comentarios personales

He conseguido cumplir con los objetivos de este ejercicio. Si bien no he usado Flask tal y como se
proponía, he usado el framework FastAPI que funciona de forma similar pero con código más sencillo
y con la ventaja de que genera la documentación, gestiona los códigos de error y el tipado de los datos.

Como bien he dicho en el readme del ejercicio anterior, no quiero engañar a nadie: soy junior
y desconocía de antemano el framework que me había propuesto. Sin embargo, con esto creo que demuestro
que no tengo ningún problema en aprender nuevas tecnologías por mi cuenta y a ponerlas en práctica rápidamente.

En cualquier caso, si finalmente la evaluación no es positiva, me gustaría agradecer la oportunidad mostrada y
el haber aprendido de esta prueba técnica.

#### Puntos a tratar:
1. Se puede verificar el funcionamiento de la aplicación en el servidor local. Para ello, es necesario ejecutar el comando de terminal
en la carpeta en la que se encuentra el script de ejecución, o bien directamente ejecutar el script app.py
```
python uvicorn app:app --reload
```
or 
```
poetry run start
```
2. Si bien puede verificarse directamente el funcionamiento desde el endpoint /docs, existe un fichero de test que verifica
que la aplicación funciona correctamente.
3. Para instalar las librerías necesarias se ha hecho uso del paquete poetry

### Prueba de los resultados
