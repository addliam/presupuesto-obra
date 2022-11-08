import tkinter as tk
from tkinter import messagebox
# ventana principal
root = tk.Tk()
root.title("Calcular presupuesto de obra")
# establecer el color de fondo de toda la ventana
root.configure(bg="white")
root.geometry("1000x680")
root.resizable(width=0, height=0)

def show_datos_basicos_entry():
    pass

def show_listado_proveedores():
    proveedores_lista = tk.Toplevel(root)
    proveedores_lista.title("Listado general de proveedores")
    proveedores_lista.configure(bg="white")
    proveedores_lista.geometry("1000x680")
    containerlist = tk.Frame(proveedores_lista, padx="40", pady="20")
    containerlist.configure(bg="white")
    containerlist.grid(column=0, row=0, sticky=('NWE'))    

    title_proveedores_lista = tk.Label(proveedores_lista, text="LISTADO DE PROVEEDORES", font="Segoe 14 bold"  )

def show_reporte():
    reporte = tk.Toplevel(root)
    reporte.title("Reporte de resumen")
    reporte.configure(bg="white")
    reporte.geometry("500x400")
    containerframe = tk.Frame(reporte, padx="40", pady="20")
    containerframe.configure(bg="white")
    containerframe.grid(column=0, row=0, sticky=('NWE'))

    r_texto_usuario = tk.Label(containerframe, text="Usuario: ", font="Segoe 10 bold").grid(column=0, row=0, sticky=('W','E'))
    r_usuario = tk.Label(containerframe, text="Default usuario")
    r_usuario.grid(column=1, row=0, sticky=('W','E'))
    r_texto_obra = tk.Label(containerframe, text="Nombre obra: ", font="Segoe 10 bold").grid(column=0, row=1, sticky=('W','E'))
    r_obra = tk.Label(containerframe, text="Default nombre obra")
    r_obra.grid(column=1, row=1, sticky=('W','E'))    
    r_texto_descripcion = tk.Label(containerframe, text="Descripcion: ", font="Segoe 10 bold").grid(column=0, row=2, sticky=('W','E'))
    r_descripcion = tk.Label(containerframe, text="Esta es la descripcion de la obra para elaborar el presupuesto")
    r_descripcion.grid(column=0, row=3, sticky=('W','E'), columnspan=3)
    r_subt_fase1 = tk.Label(containerframe, text="Subtotal Fase 1: ", font="Segoe 10 bold").grid(column=0, row=4, sticky=('W','E'))
    r_subt1 = tk.Label(containerframe, text="Default subtotal1")
    r_subt1.grid(column=0, row=5, sticky=('W','E'), columnspan=2)
    r_subt_fase2 = tk.Label(containerframe, text="Subtotal Fase 2: ", font="Segoe 10 bold").grid(column=0, row=6, sticky=('W','E'))
    r_subt2 = tk.Label(containerframe, text="Default subtotal2")
    r_subt2.grid(column=0, row=7, sticky=('W','E'), columnspan=2)    
    r_subt_fase3 = tk.Label(containerframe, text="Subtotal Fase 3: ", font="Segoe 10 bold").grid(column=0, row=8, sticky=('W','E'))
    r_subt3 = tk.Label(containerframe, text="Default subtotal3")
    r_subt3.grid(column=0, row=9, sticky=('W','E'), columnspan=2)
    r_text_total = tk.Label(containerframe, text="Total: ", font="Segoe 10 bold").grid(column=0, row=10, sticky=('W','E'))
    r_total = tk.Label(containerframe, text="Default total")
    r_total.grid(column=0, row=11, sticky=('W','E'), columnspan=2)

    for child in containerframe.winfo_children():
        child.configure(bg="white")
        child.grid_configure(pady="2")

    # establecer los valores previamente calculados
    # r_usuario.config(text=nombreusuario.get())
    # r_obra.config(text=nombreobra.get())
    # r_descripcion.config(text=descripcion.get())

    r_subt1.config(text=str(float_subtotal_fase1))
    r_subt2.config(text=str(float_subtotal_fase2))
    r_subt3.config(text=str(float_subtotal_fase3))
    r_total.config(text=str(float_total))

def show_error_message():
    messagebox.showwarning("Error de validacion", "Verifica que todos los campos sean entradas validas")

def limpiar_campos_entradas(*args):
    # limpiar entries
    # nombreobra.set("")
    # nombreusuario.set("")
    # descripcion.set("")
    # limpiar cantidades y precios unitarios
    cant_tramite_municipal.set("")
    p_unitario_tramite_municipal.set("")
    cant_aplanamiento_terreno.set("")
    p_unitario_aplanamiento_terreno.set("")
    cant_varios.set("")
    p_unitario_varios.set("")
    cant_cemento.set("")
    p_unitario_cemento.set("")
    cant_varillas.set("")
    p_unitario_varillas.set("")
    cant_arena.set("")
    p_unitario_arena.set("")
    cant_lamparas.set("")
    p_unitario_lamparas.set("")
    cant_ceramicas.set("")
    p_unitario_ceramicas.set("")
    cant_pegamento.set("")
    p_unitario_pegamento.set("")    

    subtotal_tramite_municipal.config(text="0.00")
    subtotal_aplanamiento_terreno.config(text="0.00")
    subtotal_varios.config(text="0.00")
    subtotal_cemento.config(text="0.00")
    subtotal_varillas.config(text="0.00")
    subtotal_arenas.config(text="0.00")
    subtotal_lampara.config(text="0.00")
    subtotal_ceramica.config(text="0.00")
    subtotal_pegamentos.config(text="0.00")
    # limpiar por subfases
    subtotal_fase_1.config(text="0.00")
    subtotal_fase_2.config(text="0.00")
    subtotal_fase_3.config(text="0.00")
    # limpiar en el campo total
    total.config(text="00.00")

def calcular(*args):
    global float_subtotal_fase1
    global float_subtotal_fase2
    global float_subtotal_fase3
    global float_total    
    try:
        float_subtotal1 = float(cant_tramite_municipal.get()) * float(p_unitario_tramite_municipal.get())
        float_subtotal2 = float(cant_aplanamiento_terreno.get()) * float(p_unitario_aplanamiento_terreno.get())
        float_subtotal3 = float(cant_varios.get()) * float(p_unitario_varios.get())
        float_subtotal4 = float(cant_cemento.get()) * float(p_unitario_cemento.get())
        float_subtotal5 = float(cant_varillas.get()) * float(p_unitario_varillas.get())
        float_subtotal6 = float(cant_arena.get()) * float(p_unitario_arena.get())
        float_subtotal7 = float(cant_lamparas.get()) * float(p_unitario_lamparas.get())
        float_subtotal8 = float(cant_ceramicas.get()) * float(p_unitario_ceramicas.get())
        float_subtotal9 = float(cant_pegamento.get()) * float(p_unitario_pegamento.get())

        float_subtotal_fase1 = float_subtotal1 + float_subtotal2 + float_subtotal3
        float_subtotal_fase2 = float_subtotal4 + float_subtotal5 + float_subtotal6
        float_subtotal_fase3 = float_subtotal7 + float_subtotal8 + float_subtotal9

        float_total = float_subtotal_fase1 + float_subtotal_fase2 + float_subtotal_fase3
        # poner los resultados en los campos de texto   
        subtotal_tramite_municipal.config(text=str(float_subtotal1))
        subtotal_aplanamiento_terreno.config(text=str(float_subtotal2))
        subtotal_varios.config(text=str(float_subtotal3))
        subtotal_cemento.config(text=str(float_subtotal4))
        subtotal_varillas.config(text=str(float_subtotal5))
        subtotal_arenas.config(text=str(float_subtotal6))
        subtotal_lampara.config(text=str(float_subtotal7))
        subtotal_ceramica.config(text=str(float_subtotal8))
        subtotal_pegamentos.config(text=str(float_subtotal9))
        # resultado por subfases
        subtotal_fase_1.config(text=str(float_subtotal_fase1))
        subtotal_fase_2.config(text=str(float_subtotal_fase2))
        subtotal_fase_3.config(text=str(float_subtotal_fase3))
        # resultado en el campo total
        total.config(text=str(float_total))
    except:
        show_error_message()

# frame que contendra el titulo y datos basicos sobre la obra y usuario
headerframe = tk.Frame(root, padx="100", pady="20", bg="white", height=100)
headerframe.grid(column=0, row=0, sticky=('NWE'))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

maintitle = tk.Label(headerframe, text="PRESUPUESTO DE OBRA", font="Segoe 18 bold")
maintitle.grid(column=2, row=1, sticky=('W', 'E'))

text_indicacion = tk.Label(headerframe, text="Bienvenido usuario, completa el nombre de proveedor y los costos para agregar el elemento a la lista de proveedores.", pady=10)
# text_indicacion.place(x=4, y=4)
text_indicacion.grid(column=0, row=2, sticky=('W'), columnspan=6)

label_nombreproveedor = tk.Label(headerframe, text="Nombre del proveedor: ", padx=20).grid(column=1, row=3, sticky=('W'))
nombreproveedor = tk.StringVar()
entry_nombreproveedor = tk.Entry(headerframe, width=40, textvariable=nombreproveedor).grid(column=2, row=3, sticky=('W'))

# label_nombreusuario = tk.Label(headerframe, text="Nombre del usuario", padx=20).grid(column=1, row=2, sticky=('W'))
# nombreusuario = tk.StringVar()
# entry_nombreusuario = tk.Entry(headerframe, width=40, textvariable=nombreusuario).grid(column=2, row=2, sticky=('W'))

# label_nombreobra = tk.Label(headerframe, text="Nombre de la obra", padx=20).grid(column=1, row=3, sticky=('W'))
# nombreobra = tk.StringVar()
# entry_nombreobra = tk.Entry(headerframe, width=40, textvariable=nombreobra).grid(column=2, row=3, sticky=('W'))

# label_descripcion = tk.Label(headerframe, text="Descripcion", padx=20).grid(column=1, row=4, sticky=('W'))
# descripcion = tk.StringVar()
# entry_descripcion = tk.Entry(headerframe, width=40, textvariable=descripcion).grid(column=2, row=4, sticky=('W'))

# padding para todos los elementos  del headerframe
for child in headerframe.winfo_children():
    child.grid_configure(pady=2)
    child.configure(bg="white")

maintitle.grid(pady=10)

# frame que contendra la tabla
contentframe = tk.Frame(root, padx="80", bg="white")
contentframe.grid(column=0, row=1, sticky=('NWE'), pady=30)
# nombre de las columnas de la tabla
label_fases = tk.Label(contentframe, text="FASES", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=0, row=0, sticky=('W', 'E'))
label_material = tk.Label(contentframe, text="MATERIAL / ACTIVIDAD", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=1, row=0, sticky=('W', 'E'))
label_cantidad = tk.Label(contentframe, text="CANTIDAD", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=2, row=0, sticky=('W', 'E'))
# label_unidadmedida = tk.Label(contentframe, text="U. MEDIDA", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=3, row=0, sticky=('W', 'E'))
label_preciounitario = tk.Label(contentframe, text="PRECIO U.", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=4, row=0, sticky=('W', 'E'))
label_subtotal = tk.Label(contentframe, text="Subtotal", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=5, row=0, sticky=('W', 'E'))
label_subtotal_fase = tk.Label(contentframe, text="Por fase", font="Segoe 10 bold", fg="#243c5c", padx=20).grid(column=6, row=0, sticky=('W', 'E'))
# nombre de las 3 fases
label_trabajoinicial = tk.Label(contentframe, text="1. Trabajo inicial", fg="black", padx=4).grid(column=0, row=1, sticky=('W', 'E'))
label_estructura = tk.Label(contentframe, text="2. Estructura", fg="black", padx=4).grid(column=0, row=4, sticky=('W', 'E'))
label_trabajoinicial = tk.Label(contentframe, text="3. Acabados", fg="black", padx=4).grid(column=0, row=7, sticky=('W', 'E'))

# texto de material/actividad para la fase 1
label_tramitemunicipal = tk.Label(contentframe, text="Tramites municipales", fg="black", padx=4).grid(column=1, row=1, sticky=('W', 'E'))
label_aplanamientoterreno = tk.Label(contentframe, text="Aplanamiento Terreno", fg="black", padx=4).grid(column=1, row=2, sticky=('W', 'E'))
label_varios = tk.Label(contentframe, text="Varios", fg="black", padx=4).grid(column=1, row=3, sticky=('W', 'E'))
# texto de material/actividad para la fase 2
label_cemento = tk.Label(contentframe, text="Cemento", fg="black", padx=4).grid(column=1, row=4, sticky=('W', 'E'), pady=(10,0))
label_varillas = tk.Label(contentframe, text="Varillas", fg="black", padx=4).grid(column=1, row=5, sticky=('W', 'E'))
label_arena = tk.Label(contentframe, text="Arena", fg="black", padx=4).grid(column=1, row=6, sticky=('W', 'E'))
# texto de material/actividad para la fase 3
label_lamparas = tk.Label(contentframe, text="Lamparas", fg="black", padx=4).grid(column=1, row=7, sticky=('W', 'E'), pady=(10,0))
label_ceramicas = tk.Label(contentframe, text="Ceramicas", fg="black", padx=4).grid(column=1, row=8, sticky=('W', 'E'))
label_pegamento = tk.Label(contentframe, text="Pegamento", fg="black", padx=4).grid(column=1, row=9, sticky=('W', 'E'))

# 1. Entradas de datos: cantidad
# Fase 1
cant_tramite_municipal = tk.StringVar()
entry_cant_tramite_municipal = tk.Entry(contentframe, width=4, textvariable=cant_tramite_municipal).grid(column=2, row=1, sticky=('W', 'E'))
cant_aplanamiento_terreno = tk.StringVar()
entry_cant_aplanamiento_terreno = tk.Entry(contentframe, width=4, textvariable=cant_aplanamiento_terreno).grid(column=2, row=2, sticky=('W', 'E'))
cant_varios = tk.StringVar()
entry_cant_varios = tk.Entry(contentframe, width=4, textvariable=cant_varios).grid(column=2, row=3, sticky=('W', 'E'))
# Fase 2
cant_cemento = tk.StringVar()
entry_cant_cemento = tk.Entry(contentframe, width=4, textvariable=cant_cemento).grid(column=2, row=4, sticky=('W', 'E'), pady=(10,0))
cant_varillas = tk.StringVar()
entry_cant_varillas = tk.Entry(contentframe, width=4, textvariable=cant_varillas).grid(column=2, row=5, sticky=('W', 'E'))
cant_arena = tk.StringVar()
entry_cant_arena = tk.Entry(contentframe, width=4, textvariable=cant_arena).grid(column=2, row=6, sticky=('W', 'E'))
# Fase 3
cant_lamparas = tk.StringVar()
entry_cant_lamparas = tk.Entry(contentframe, width=4, textvariable=cant_lamparas).grid(column=2, row=7, sticky=('W', 'E'), pady=(10,0))
cant_ceramicas = tk.StringVar()
entry_cant_ceramicas = tk.Entry(contentframe, width=4, textvariable=cant_ceramicas).grid(column=2, row=8, sticky=('W', 'E'))
cant_pegamento = tk.StringVar()
entry_cant_pegamento = tk.Entry(contentframe, width=4, textvariable=cant_pegamento).grid(column=2, row=9, sticky=('W', 'E'))

# 2.Entradas de datos: unidad de medida
# Fase 1
# umedida_tramite_municipal = tk.StringVar()
# entry_umedida_tramite_municipal = tk.Entry(contentframe, width=4, textvariable=umedida_tramite_municipal).grid(column=3, row=1, sticky=('W', 'E'))
# umedida_aplanamiento_terreno = tk.StringVar()
# entry_umedida_aplanamiento_terreno = tk.Entry(contentframe, width=4, textvariable=umedida_aplanamiento_terreno).grid(column=3, row=2, sticky=('W', 'E'))
# umedida_varios = tk.StringVar()
# entry_umedida_varios = tk.Entry(contentframe, width=4, textvariable=umedida_varios).grid(column=3, row=3, sticky=('W', 'E'))
# # Fase 2
# umedida_cemento = tk.StringVar()
# entry_umedida_cemento = tk.Entry(contentframe, width=4, textvariable=umedida_cemento).grid(column=3, row=4, sticky=('W', 'E'))
# umedida_varillas = tk.StringVar()
# entry_umedida_varillas = tk.Entry(contentframe, width=4, textvariable=umedida_varillas).grid(column=3, row=5, sticky=('W', 'E'))
# umedida_arenas = tk.StringVar()
# entry_umedida_arenas = tk.Entry(contentframe, width=4, textvariable=umedida_arenas).grid(column=3, row=6, sticky=('W', 'E'))
# # Fase 3
# umedida_lamparas = tk.StringVar()
# entry_umedida_lamparas = tk.Entry(contentframe, width=4, textvariable=umedida_lamparas).grid(column=3, row=7, sticky=('W', 'E'))
# umedida_ceramicas = tk.StringVar()
# entry_umedida_ceramicas = tk.Entry(contentframe, width=4, textvariable=umedida_ceramicas).grid(column=3, row=8, sticky=('W', 'E'))
# umedida_pegamento = tk.StringVar()
# entry_umedida_pegamento = tk.Entry(contentframe, width=4, textvariable=umedida_pegamento).grid(column=3, row=9, sticky=('W', 'E'))

# 3. Entradas de datos: precio unitario
# Fase 1
p_unitario_tramite_municipal = tk.StringVar()
entry_p_unitario_tramite_municipal = tk.Entry(contentframe, width=4, textvariable=p_unitario_tramite_municipal).grid(column=4, row=1, sticky=('W', 'E'))
p_unitario_aplanamiento_terreno = tk.StringVar()
entry_p_unitario_aplanamiento_terreno = tk.Entry(contentframe, width=4, textvariable=p_unitario_aplanamiento_terreno).grid(column=4, row=2, sticky=('W', 'E'))
p_unitario_varios = tk.StringVar()
entry_p_unitario_varios = tk.Entry(contentframe, width=4, textvariable=p_unitario_varios).grid(column=4, row=3, sticky=('W', 'E'))
# Fase 2
p_unitario_cemento = tk.StringVar()
entry_p_unitario_cemento = tk.Entry(contentframe, width=4, textvariable=p_unitario_cemento).grid(column=4, row=4, sticky=('W', 'E'))
p_unitario_varillas = tk.StringVar()
entry_p_unitario_varillas = tk.Entry(contentframe, width=4, textvariable=p_unitario_varillas).grid(column=4, row=5, sticky=('W', 'E'))
p_unitario_arena = tk.StringVar()
entry_p_unitario_arena = tk.Entry(contentframe, width=4, textvariable=p_unitario_arena).grid(column=4, row=6, sticky=('W', 'E'))
# Fase 3
p_unitario_lamparas = tk.StringVar()
entry_p_unitario_lamparas = tk.Entry(contentframe, width=4, textvariable=p_unitario_lamparas).grid(column=4, row=7, sticky=('W', 'E'))
p_unitario_ceramicas = tk.StringVar()
entry_p_unitario_ceramicas = tk.Entry(contentframe, width=4, textvariable=p_unitario_ceramicas).grid(column=4, row=8, sticky=('W', 'E'))
p_unitario_pegamento = tk.StringVar()
entry_p_unitario_pegamento = tk.Entry(contentframe, width=4, textvariable=p_unitario_pegamento).grid(column=4, row=9, sticky=('W', 'E'))

# 4. Datos calculados: subtotal
# Fase 1
subtotal_tramite_municipal = tk.Label(contentframe, text="0.00", width=5 )
subtotal_tramite_municipal.grid(column=5, row=1, sticky=('W', 'E'))
subtotal_aplanamiento_terreno = tk.Label(contentframe, text="0.00", width=5 )
subtotal_aplanamiento_terreno.grid(column=5, row=2, sticky=('W', 'E'))
subtotal_varios = tk.Label(contentframe, text="0.00", width=5 )
subtotal_varios.grid(column=5, row=3, sticky=('W', 'E'))
# Fase 2
subtotal_cemento = tk.Label(contentframe, text="0.00", width=5 )
subtotal_cemento.grid(column=5, row=4, sticky=('W', 'E'))
subtotal_varillas = tk.Label(contentframe, text="0.00", width=5 )
subtotal_varillas.grid(column=5, row=5, sticky=('W', 'E'))
subtotal_arenas = tk.Label(contentframe, text="0.00", width=5 )
subtotal_arenas.grid(column=5, row=6, sticky=('W', 'E'))
# Fase 3
subtotal_lampara = tk.Label(contentframe, text="0.00", width=5 )
subtotal_lampara.grid(column=5, row=7, sticky=('W', 'E'))
subtotal_ceramica = tk.Label(contentframe, text="0.00", width=5 )
subtotal_ceramica.grid(column=5, row=8, sticky=('W', 'E'))
subtotal_pegamentos = tk.Label(contentframe, text="0.00", width=5 )
subtotal_pegamentos.grid(column=5, row=9, sticky=('W', 'E'))

# 5. Datos calculados: subtotal por fases
texto_subtotal_fase_1 = tk.Label(contentframe, text="Subtotal 1", width=4 ).grid(column=6, row=2, sticky=('W', 'E'))
subtotal_fase_1 = tk.Label(contentframe, text="0.00", width=5 )
subtotal_fase_1.grid(column=6, row=3, sticky=('W', 'E'))
texto_subtotal_fase_2 = tk.Label(contentframe, text="Subtotal 2", width=4 ).grid(column=6, row=5, sticky=('W', 'E'))
subtotal_fase_2 = tk.Label(contentframe, text="0.00", width=5 )
subtotal_fase_2.grid(column=6, row=6, sticky=('W', 'E'))
texto_subtotal_fase_3 = tk.Label(contentframe, text="Subtotal 3", width=4 ).grid(column=6, row=8, sticky=('W', 'E'))
subtotal_fase_3 = tk.Label(contentframe, text="0.00", width=5 )
subtotal_fase_3.grid(column=6, row=9, sticky=('W', 'E'))
# 6. Total general
texto_total = tk.Label(contentframe, text="Total", width=5, font="Segoe 10 bold").grid(column=5, row=10, sticky=('W', 'E'))
total = tk.Label(contentframe, text="00.00", width=5, background="yellow", font="Segoe 10 bold")
total.grid(column=6, row=10, sticky=('W', 'E'))

# configurar padding y color del fondo
for child in contentframe.winfo_children():
    child.grid_configure(padx=3, pady=2)
    child.configure(bg="white")

# frame que contendra los botones
buttonsframe = tk.Frame(root, padx="100", pady="20", bg="white")
buttonsframe.grid(column=0, row=2, sticky=('NWE'))
button_calcular = tk.Button(buttonsframe, text="Calcular", width=24, bg="#2d78d6", fg="white", activebackground="#1f5aa2", activeforeground="white", command=calcular).grid(column=0, row=0, sticky=('E'), pady=4, padx=(620,0))
button_agregar_a_lista = tk.Button(buttonsframe, text="Agregar a lista", width=24, bg="#FF4E4E", fg="white", activebackground="#D34444", activeforeground="white", command=show_reporte).grid(column=0, row=1, sticky=('W', 'E'), pady=4, padx=(620,0) )
button_limpiar = tk.Button(buttonsframe, text="Limpiar", width=24, bg="#3091e2", fg="white", activebackground="#1f5aa2", activeforeground="white", command=limpiar_campos_entradas).grid(column=0, row=2, sticky=('W', 'E'), pady=4, padx=(620,0) )

root.mainloop()