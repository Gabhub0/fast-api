from fastapi import FastAPI 

app = FastAPI() 


@app.get("/")
def read_index():
    return 'Este es el Index'

@app.get("/saludo")
def read_item():
    return "Hola, FastAPI"


