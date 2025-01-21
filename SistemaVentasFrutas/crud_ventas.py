import tkinter as tk
from tkinter import messagebox
from conexion import conectar_bd
import datetime

def ventana_ventas():
    ventana = tk.Toplevel()
    ventana.title("Gestión de Ventas")
    ventana.geometry("400x300")

    menu = tk.Menu(ventana)
    ventana.config(menu=menu)

    menu_archivo = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Archivo", menu=menu_archivo)
    menu_archivo.add_command(label="Salir", command=ventana.destroy)

    menu_ayuda = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Acerca de", "Sistema de Ventas de Frutas v1.0"))

    tk.Label(ventana, text="Código Venta:").grid(row=0, column=0)
    entry_cod_venta = tk.Entry(ventana)
    entry_cod_venta.grid(row=0, column=1)

    tk.Label(ventana, text="Cédula Cliente:").grid(row=1, column=0)
    entry_cedula = tk.Entry(ventana)
    entry_cedula.grid(row=1, column=1)

    tk.Label(ventana, text="Código Producto:").grid(row=2, column=0)
    entry_codigo_prod = tk.Entry(ventana)
    entry_codigo_prod.grid(row=2, column=1)

    tk.Label(ventana, text="Cantidad:").grid(row=3, column=0)
    entry_cantidad = tk.Entry(ventana)
    entry_cantidad.grid(row=3, column=1)

    def agregar_venta():
        cod_venta = entry_cod_venta.get()
        cedula = entry_cedula.get()
        codigo_prod = entry_codigo_prod.get()
        cantidad = entry_cantidad.get()
        fecha = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        if cod_venta and cedula and codigo_prod and cantidad:
            try:
                conn = conectar_bd()
                cursor = conn.cursor()
                cursor.execute("SELECT precio FROM ventas_producto WHERE codigo_prod = %s", (codigo_prod,))
                precio = cursor.fetchone()

                if precio:
                    total = float(precio[0]) * int(cantidad)
                    cursor.execute("INSERT INTO ventas_venta (cod_venta, cliente_id, producto_id, cantidad, fecha, total) VALUES (%s, %s, %s, %s, %s, %s)",
                                   (cod_venta, cedula, codigo_prod, cantidad, fecha, total))
                    conn.commit()
                    messagebox.showinfo("Éxito", "Venta agregada correctamente")
                else:
                    messagebox.showerror("Error", "Producto no encontrado")
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"Error al registrar venta: {e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")

    btn_agregar = tk.Button(ventana, text="Agregar Venta", command=agregar_venta)
    btn_agregar.grid(row=4, column=1)
