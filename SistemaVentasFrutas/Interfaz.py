import tkinter as tk
from crud_productos import ventana_productos
from crud_clientes import ventana_clientes
from crud_ventas import ventana_ventas

def menu_principal():
    root = tk.Tk()
    root.title("Sistema de Ventas de Frutas")
    root.geometry("300x250")

    btn_productos = tk.Button(root, text="Gestión de Productos", command=ventana_productos)
    btn_productos.pack(pady=10)

    btn_clientes = tk.Button(root, text="Gestión de Clientes", command=ventana_clientes)
    btn_clientes.pack(pady=10)

    btn_ventas = tk.Button(root, text="Gestión de Ventas", command=ventana_ventas)
    btn_ventas.pack(pady=10)

    root.mainloop()

menu_principal()