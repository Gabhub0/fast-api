from fastapi import FastAPI #importamos a la clase fastapi que define nuestra app

app = FastAPI() #definimos este objeto que va a llamar al constructor de la clase fastapi

#luego a este objeto le agregamos las rutas que queremos manejar con esta app
#para ello llamamos el decorador app con una ruta

@app.get("/")

#es una buena practica en general definir una ruta con un mensaje de bienvenida en la direccion /

#luego definimos una funcion

def read_root():
    return {"mesaje":"Hola comunidad Humai"}
