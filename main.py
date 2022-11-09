import tkinter as tk
from tkinter import messagebox
# ventana principal
root = tk.Tk()
root.title("Calcular presupuesto de obra")
# establecer el color de fondo de toda la ventana
root.configure(bg="white")
root.geometry("1000x680")
root.resizable(width=0, height=0)

def raise_frame(frame):
    frame.tkraise()

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

    title_proveedores_lista = tk.Label(proveedores_lista, text="LISTADO DE PROVEEDORES", font="Segoe 18 bold" ).grid(column=0, row=0, sticky=('W','E'))

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

def volver_al_menu():
    raise_frame(f2)

def volver_agregar_proveedor():
    raise_frame(f1)

def mostrar_mejor_opcion():
    pass

# Frame 1 para la ventana de nombre proveedor, tabla de costos y botones
f1 = tk.Frame(root)
f1.grid(column=0, row=0, sticky='NEW')
f1.configure(bg="white")
headerframe = tk.Frame(f1, padx="100", pady="20", bg="white", height=160)
headerframe.grid(column=0, row=0, sticky=('NEW'))

maintitle = tk.Label(headerframe, text="PRESUPUESTO DE OBRA", font="Segoe 18 bold", bg="white")
maintitle.place(x=240,y=10)
# boton de volver al menu
button_volver_menu = tk.Button(headerframe, text="Volver al menu", fg="white", bg="#434343", activebackground="#646464", activeforeground="white", command=volver_al_menu, cursor="hand2")
button_volver_menu.place(x=-60, y=10)

text_indicacion = tk.Label(headerframe, text="Bienvenido usuario, completa el nombre de proveedor y los costos para agregar el elemento a la lista de proveedores.", font="Segoe 10", pady=10, bg="white")
text_indicacion.place(x=20,y=54)

label_nombreproveedor = tk.Label(headerframe, text="Nombre del proveedor: ", padx=20, bg="white")
label_nombreproveedor.place(x=100,y=110)
nombreproveedor = tk.StringVar()
entry_nombreproveedor = tk.Entry(headerframe, width=40, textvariable=nombreproveedor)
entry_nombreproveedor.place(x=300,y=110)

# padding para todos los elementos  del headerframe
# for child in headerframe.winfo_children():
#     child.grid_configure(pady=2)
    # child.configure(bg="white")

# maintitle.grid(pady=10)

# frame que contendra la tabla
contentframe = tk.Frame(f1, padx="80", bg="white")
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
total = tk.Label(contentframe, text="00.00", width=5, background="#F2F2F2", font="Segoe 10 bold")
total.grid(column=6, row=10, sticky=('W', 'E'))

# configurar padding y color del fondo
for child in contentframe.winfo_children():
    child.grid_configure(padx=3, pady=2)
    child.configure(bg="white")

# frame que contendra los botones
buttonsframe = tk.Frame(f1, padx="100", pady="20", bg="white")
buttonsframe.grid(column=0, row=2, sticky=('NWE'))
button_calcular = tk.Button(buttonsframe, text="Calcular", width=24, bg="#2d78d6", fg="white", activebackground="#1f5aa2", activeforeground="white", command=calcular, cursor="hand2").grid(column=0, row=0, sticky=('E'), pady=4, padx=(620,0))
button_agregar_a_lista = tk.Button(buttonsframe, text="Agregar a lista", width=24, bg="#FF4E4E", fg="white", activebackground="#D34444", activeforeground="white", command=show_reporte, cursor="hand2").grid(column=0, row=1, sticky=('W', 'E'), pady=4, padx=(620,0) )
button_limpiar = tk.Button(buttonsframe, text="Limpiar", width=24, bg="#3091e2", fg="white", activebackground="#1f5aa2", activeforeground="white", command=limpiar_campos_entradas, cursor="hand2").grid(column=0, row=2, sticky=('W', 'E'), pady=4, padx=(620,0) )


# ------------------------- FRAME 2 --------------------------------
# Frame 2 para listado de proveedores, datos basicos de la obra y el usuario
f2 = tk.Frame(root)
f2.grid(column=0, row=0, sticky='NEW')
f2.configure(bg="white")
headerframe2 = tk.Frame(f2, padx='100', pady="10", bg="white", height=70, width=1000)
headerframe2.grid(column=0, row=0, sticky="NEW")
title_frame2 = tk.Label(headerframe2, text="LISTADO DE PROVEEDORES", font="Segoe 18 bold", bg="white")
title_frame2.place(x=220,y=10)
formframe2 = tk.Frame(f2, padx="240", pady="10", bg="white", height=300, width=1000)
formframe2.grid(column=0, row=1, sticky="NEW")

label_nombreusuario = tk.Label(formframe2, text="Nombre del usuario", padx=20).grid(column=1, row=2, sticky=('W'))
nombreusuario = tk.StringVar()
entry_nombreusuario = tk.Entry(formframe2, width=40, textvariable=nombreusuario).grid(column=2, row=2, sticky=('W'))
label_nombreobra = tk.Label(formframe2, text="Nombre de la obra", padx=20).grid(column=1, row=3, sticky=('W'))
nombreobra = tk.StringVar()
entry_nombreobra = tk.Entry(formframe2, width=40, textvariable=nombreobra).grid(column=2, row=3, sticky=('W'))
label_descripcion = tk.Label(formframe2, text="Descripcion", padx=20).grid(column=1, row=4, sticky=('W'))
descripcion = tk.StringVar()
entry_descripcion = tk.Entry(formframe2, width=40, textvariable=descripcion).grid(column=2, row=4, sticky=('W'))

for child in formframe2.winfo_children():
    child.configure(bg="white")
    child.grid_configure(pady="2")

frame_lista_container = tk.Frame(f2, padx="10", pady="10", bg="#F2F2F2", height=420, width=1000)
frame_lista_container.grid(column=0, row=2, sticky="WES")

frame_lista_proveedores = tk.Frame(frame_lista_container, padx="180", pady="10", bg="#F2F2F2", height=420, width=1400)
# frame_lista_proveedores.grid(column=0, row=0, sticky="WES", rowspan=1)
frame_lista_proveedores.place(x=2,y=2)

def spawn_item_proveedor(col, row):
    item_proveedor = tk.Frame(frame_lista_proveedores, padx="2", pady="2", height=80, width=300, bg="white")
    item_proveedor.grid(column=col, row=row, sticky="NEW", padx=8, pady=8)
    texto_proveedor_n = tk.Label(item_proveedor, text="Proveedor 01", pady="4", font="Segoe 10 bold", bg="white")
    texto_proveedor_n.place(x=6, y=5)
    texto_prov_nombre = tk.Label(item_proveedor, text="Nombre:", pady="4", font="Segoe 10", fg="#0057C8", bg="white")
    texto_prov_nombre.place(x=6, y=36)
    texto_prov_nombre = tk.Label(item_proveedor, text="Constructora Las Casaruinas", pady="4", font="Segoe 10", fg="black", bg="white")
    texto_prov_nombre.place(x=70, y=36)


spawn_item_proveedor(0,0)
spawn_item_proveedor(1,0)
spawn_item_proveedor(0,1)
spawn_item_proveedor(1,1)

frame2_buttons = tk.Frame(f2, padx="200", pady="30", bg="white", height=60, width=1000)
frame2_buttons.grid(column=0, row=3, sticky="WES")
# boton de volver a agregar proveedor
button_volver_agregar_prov = tk.Button(frame2_buttons, text="AGREGAR PRESUPUESTO", fg="white", bg="#FF4E4E", activebackground="#D34444", activeforeground="white", command=volver_agregar_proveedor, font="Segoe 11", cursor="hand2")
button_volver_agregar_prov.grid(column=0, row=0, sticky="NEW", padx=(300,0))
# boton de mostrar mejor opcion
button_mostrar_mejor_opcion = tk.Button(frame2_buttons, text="MOSTRAR MEJOR OPCION", fg="white", bg="#2D77D6", activebackground="#266BC3", activeforeground="white", command=mostrar_mejor_opcion, font="Segoe 11", cursor="hand2")
button_mostrar_mejor_opcion.grid(column=1, row=0, sticky="NEW", padx="20")

raise_frame(f2)
root.mainloop()