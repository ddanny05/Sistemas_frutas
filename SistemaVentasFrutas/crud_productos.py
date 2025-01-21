import tkinter as tk
from tkinter import messagebox
from conexion import conectar_bd

def ventana_productos():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")
    ventana.geometry("400x300")

    menu = tk.Menu(ventana)
    ventana.config(menu=menu)

    menu_archivo = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=ventana.destroy)

    menu_ayuda = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Sistema de Ventas de Frutas v1.0"))


    tk.Label(ventana, text="Código Producto:").grid(row=0, column=0)
    entry_codigo_prod = tk.Entry(ventana)
    entry_codigo_prod.grid(row=0, column=1)

    tk.Label(ventana, text="Nombre Producto:").grid(row=1, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=1, column=1)

    tk.Label(ventana, text="Precio Producto:").grid(row=2, column=0)
    entry_precio = tk.Entry(ventana)
    entry_precio.grid(row=2, column=1)

    tk.Label(ventana, text="Stock Producto:").grid(row=3, column=0)
    entry_stock = tk.Entry(ventana)
    entry_stock.grid(row=3, column=1)
    
    

    def agregar_producto():
        codigo_prod = entry_codigo_prod.get()
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        stock = entry_stock.get()

        if codigo_prod and nombre and precio and stock:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO ventas_producto (codigo_prod, nombre, precio, stock) VALUES (%s, %s, %s, %s)",
                           (codigo_prod, nombre, precio, stock))
            conn.commit()
            conn.close()
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto)
    btn_agregar.grid(row=4, column=1)