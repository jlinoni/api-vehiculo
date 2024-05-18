from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# Conexión a la base de datos
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="bd_api_vehiculos"
)
mycursor = mydb.cursor()


# Definición del modelo de vehículo
class Vehiculo(BaseModel):
    id: int
    conductor_id: int
    marca: str
    modelo: str
    ano: int
    placa: str


# Rutas del API

# Consultar vehículo por ID
@app.get("/vehiculo/{vehiculo_id}")
def get_vehiculo(vehiculo_id: int):
    mycursor.execute("SELECT * FROM vehiculo WHERE id = %s", (vehiculo_id,))
    vehiculo = mycursor.fetchone()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return dict(vehiculo)


# Historial de accidentes de un vehículo por ID
@app.get("/vehiculo/{vehiculo_id}/accidentes")
def get_accidentes(vehiculo_id: int):
    mycursor.execute("SELECT * FROM accidente WHERE vehiculo_id = %s", (vehiculo_id,))
    accidentes = mycursor.fetchall()
    return {"accidentes": accidentes}


# Historial de robos de un vehículo por ID
@app.get("/vehiculo/{vehiculo_id}/robos")
def get_robos(vehiculo_id: int):
    mycursor.execute("SELECT * FROM robo WHERE vehiculo_id = %s", (vehiculo_id,))
    robos = mycursor.fetchall()
    return {"robos": robos}


# Historial de papeletas de un vehículo por ID
@app.get("/vehiculo/{vehiculo_id}/papeletas")
def get_papeletas(vehiculo_id: int):
    mycursor.execute("SELECT * FROM papeleta WHERE vehiculo_id = %s", (vehiculo_id,))
    papeletas = mycursor.fetchall()
    return {"papeletas": papeletas}


# Historial de deudas de un vehículo por ID
@app.get("/vehiculo/{vehiculo_id}/deudas")
def get_deudas(vehiculo_id: int):
    mycursor.execute("SELECT * FROM deuda WHERE vehiculo_id = %s", (vehiculo_id,))
    deudas = mycursor.fetchall()
    return {"deudas": deudas}