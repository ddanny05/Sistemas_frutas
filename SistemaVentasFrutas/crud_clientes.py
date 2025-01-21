import tkinter as tk
from tkinter import messagebox
from conexion import conectar_bd

def ventana_clientes():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Clientes")
    ventana.geometry("400x300")

    menu = tk.Menu(ventana)
    ventana.config(menu=menu)

    menu_archivo = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=ventana.destroy)

    menu_ayuda = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Sistema de Ventas de Frutas v1.0"))

    tk.Label(ventana, text="Cédula Cliente:").grid(row=0, column=0)
    entry_cedula = tk.Entry(ventana)
    entry_cedula.grid(row=0, column=1)

    tk.Label(ventana, text="Nombre Cliente:").grid(row=1, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=1, column=1)

    tk.Label(ventana, text="Email Cliente:").grid(row=2, column=0)
    entry_email = tk.Entry(ventana)
    entry_email.grid(row=2, column=1)

    tk.Label(ventana, text="Teléfono Cliente:").grid(row=3, column=0)
    entry_telefono = tk.Entry(ventana)
    entry_telefono.grid(row=3, column=1)

    def agregar_cliente():
        cedula = entry_cedula.get()
        nombre = entry_nombre.get()
        email = entry_email.get()
        telefono = entry_telefono.get()

        if cedula and nombre and email and telefono:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ventas_cliente (cedula, nombre, email, telefono) VALUES (%s, %s, %s, %s)",
                           (cedula, nombre, email, telefono))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Cliente agregado correctamente")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    btn_agregar = tk.Button(ventana, text="Agregar Cliente", command=agregar_cliente)
    btn_agregar.grid(row=4, column=1)
