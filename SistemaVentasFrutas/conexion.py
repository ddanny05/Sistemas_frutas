# Archivo: conexion.py
import mysql.connector

def conectar_bd():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="088266619Da.di",
        database="frutas"
    )