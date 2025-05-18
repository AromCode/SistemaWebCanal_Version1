import tkinter as tk
from tkinter import messagebox
import os


# Código preestablecido
CODIGO_PREESTABLECIDO = "mc45"

# Función para guardar los datos del usuario en un archivo de texto
def registrar_usuario():
    usuario = entry_usuario.get()
    contrasena = entry_contrasena.get()
    correo = entry_correo.get()

    # Validar que los campos no estén vacíos
    if not usuario or not contrasena or not correo:
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return

    # Guardar los datos en un archivo de texto (formato: usuario,contraseña,correo)
    with open('usuarios.txt', 'a') as archivo:
        archivo.write(f"{usuario},{contrasena},{correo}\n")
    
    messagebox.showinfo("Éxito", "Usuario registrado exitosamente")
    mostrar_login()  # Después de registrarse, mostramos el formulario de login

# Función para validar el login
def login_usuario():
    usuario = entry_usuario_login.get()
    contrasena = entry_contrasena_login.get()

    # Verificar si los campos no están vacíos
    if not usuario or not contrasena:
        messagebox.showerror("Error", "Por favor ingrese ambos campos")
        return

    # Verificar si el archivo de usuarios existe
    if not os.path.exists('usuarios.txt'):
        messagebox.showerror("Error", "No hay usuarios registrados")
        return

    # Leer el archivo y verificar si las credenciales coinciden
    with open('usuarios.txt', 'r') as archivo:
        usuarios = archivo.readlines()

    for linea in usuarios:
        datos = linea.strip().split(',')
        if datos[0] == usuario and datos[1] == contrasena:
            mostrar_bienvenido(usuario)  # Mostrar mensaje de bienvenida si es correcto
            return
    
    # Si no encuentra las credenciales
    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Función para mostrar la interfaz para ingresar el código
def mostrar_codigo_verificacion():
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    # Mostrar campo para ingresar el código
    tk.Label(frame_principal, text="Ingrese el código de verificación:").grid(row=0, column=0)

    global entry_codigo
    entry_codigo = tk.Entry(frame_principal, show="*")
    entry_codigo.grid(row=0, column=1)

    # Botón para verificar el código
    tk.Button(frame_principal, text="Verificar Código", command=verificar_codigo).grid(row=1, columnspan=2)

    # Agregar la imagen solo en el login
    etiqueta_imagen = tk.Label(frame_principal, image=imagen)
    etiqueta_imagen.image = imagen  # Para evitar que Python borre la imagen
    etiqueta_imagen.grid(row=5, columnspan=2, pady=10)  # Usamos grid en lugar de pack para mayor control


    # Botón circular de "Atrás" para volver al login, ahora en una fila más baja (fila 2)
    tk.Button(frame_principal, text="⬅️", command=mostrar_login, font=("Helvetica", 14), width=3, height=1, relief="solid", borderwidth=2).grid(row=8, column=1, sticky="e")

# Función para verificar el código ingresado
def verificar_codigo():
    codigo_ingresado = entry_codigo.get()

    if codigo_ingresado == CODIGO_PREESTABLECIDO:
        mostrar_registro()  # Si el código es correcto, mostrar el formulario de registro
    else:
        messagebox.showerror("Error", "Código incorrecto. Intenta nuevamente.")

# Función para mostrar el formulario de registro
def mostrar_registro():
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    # Mostrar campos para registro
    tk.Label(frame_principal, text="Nombre de Usuario:").grid(row=0, column=0)
    tk.Label(frame_principal, text="Contraseña:").grid(row=1, column=0)
    tk.Label(frame_principal, text="Correo Electrónico:").grid(row=2, column=0)

    global entry_usuario, entry_contrasena, entry_correo
    entry_usuario = tk.Entry(frame_principal)
    entry_contrasena = tk.Entry(frame_principal, show="*")
    entry_correo = tk.Entry(frame_principal)

    entry_usuario.grid(row=0, column=1)
    entry_contrasena.grid(row=1, column=1)
    entry_correo.grid(row=2, column=1)

    tk.Button(frame_principal, text="Registrar", command=registrar_usuario).grid(row=3, columnspan=2)
    tk.Button(frame_principal, text="Ya tengo cuenta, Iniciar sesión", command=mostrar_login).grid(row=4, columnspan=2)

    # Agregar la imagen solo en el login
    etiqueta_imagen = tk.Label(frame_principal, image=imagen)
    etiqueta_imagen.image = imagen  # Para evitar que Python borre la imagen
    etiqueta_imagen.grid(row=5, columnspan=2, pady=10)  # Usamos grid en lugar de pack para mayor control


    # Botón circular de "Atrás" para volver al login, ahora en una fila más baja (fila 5)
    tk.Button(frame_principal, text="⬅️", command=mostrar_login, font=("Helvetica", 14), width=3, height=1, relief="solid", borderwidth=2).grid(row=15, column=2, sticky="e")

# Función para mostrar el formulario de login
def mostrar_login():
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    tk.Label(frame_principal, text="*SISTEMA REGISTRO*", font=("Helvetica", 18, "bold")).grid(row=0, columnspan=2)
    # Mostrar campos para login
    tk.Label(frame_principal, text="Nombre de Usuario:").grid(row=1, column=0)
    tk.Label(frame_principal, text="Contraseña:").grid(row=2, column=0)

    global entry_usuario_login, entry_contrasena_login
    entry_usuario_login = tk.Entry(frame_principal)
    entry_contrasena_login = tk.Entry(frame_principal, show="*")

    entry_usuario_login.grid(row=1, column=1)
    entry_contrasena_login.grid(row=2, column=1)

    tk.Button(frame_principal, text="Iniciar sesión", command=login_usuario).grid(row=3, columnspan=2)
    tk.Button(frame_principal, text="No tengo cuenta, Registrarme", command=mostrar_codigo_verificacion).grid(row=4, columnspan=2)

     # Agregar la imagen solo en el login
    etiqueta_imagen = tk.Label(frame_principal, image=imagen)
    etiqueta_imagen.image = imagen  # Para evitar que Python borre la imagen
    etiqueta_imagen.grid(row=5, columnspan=2, pady=10)  # Usamos grid en lugar de pack para mayor control


   

# Función para mostrar la pantalla de bienvenida
def mostrar_bienvenido(usuario):
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    root.geometry("650x400")  # Aquí defines el nuevo tamaño de la ventana    

    # Crear un contenedor central para alinear todo el contenido
    contenedor = tk.Frame(frame_principal)
    contenedor.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Configurar la cuadrícula para que el contenedor ocupe todo el espacio disponible
    frame_principal.grid_rowconfigure(0, weight=1)  # Permite que el contenedor se expanda verticalmente
    frame_principal.grid_columnconfigure(0, weight=1)  # Permite que el contenedor se expanda horizontalmente

    # Agregar widgets al contenedor central (todo centrado)
    tk.Label(contenedor, text=f"¡BIENVENIDO A MEGAVISIÓN CANAL 45!", font=("Helvetica", 14)).grid(row=0, columnspan=4, pady=20)  # Se movió de row=0 a row=2

    tk.Label(contenedor, text="** Megavision Canal 45 **", font=("Helvetica", 12, "bold")).grid(row=1, columnspan=4, pady=10)  # Se movió de row=1 a row=3
    
    tk.Button(contenedor, text="Registro Programas", width=15, command=lambda: mostrar_registro_programas(usuario)).grid(row=2, column=0, pady=10)  # Se movió de row=2 a row=4
    tk.Button(contenedor, text="Ver Programas", width=15, command=lambda: mostrar_ver_programas(usuario)).grid(row=2, column=1, pady=10)  # Se movió de row=2 a row=4
    tk.Button(contenedor, text="Usuarios", width=15, command=lambda: mostrar_lista_usuarios(usuario)).grid(row=2, column=2, pady=10)  # Nuevo botón

    tk.Label(contenedor, text="**Formulario de Registro de Programa**", font=("Helvetica", 12, "bold")).grid(row=3, columnspan=4, pady=10)  # Se movió de row=3 a row=5

    # Crear el tercer contenedor a la izquierda (Información de Transmisión)
    #frame_izquierda3 = tk.Frame(contenedor)
    #frame_izquierda3.grid(row=5, column=0, padx=20, pady=10, sticky="nw")  

    # Asegurarnos de que la imagen no esté visible en esta vista
    for widget in contenedor.winfo_children():
        if isinstance(widget, tk.Label) and widget.image == imagen:
            widget.grid_forget()  # Esto oculta la imagen

def mostrar_lista_usuarios(usuario):
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    root.geometry("800x700")  # Ajustar el tamaño de la ventana

    # Crear un contenedor central para alinear todo el contenido
    contenedor = tk.Frame(frame_principal)
    contenedor.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

    # Crear el botón "Atrás" para regresar a la pantalla de bienvenida
    # Solo pasar el nombre del usuario (es decir, datos_usuario[0])
    tk.Button(frame_principal, text="Atrás", command=lambda: mostrar_bienvenido(usuario), width=15).grid(row=1, column=0, pady=20, padx=20)

    # Configurar la cuadrícula para que el contenedor se expanda
    frame_principal.grid_rowconfigure(0, weight=1)
    frame_principal.grid_columnconfigure(0, weight=1)

    # Agregar título
    tk.Label(contenedor, text="Lista de usuarios registrados", font=("Helvetica", 16)).grid(row=0, columnspan=4, pady=20)

    # Crear los encabezados de la tabla
    encabezados = ["Usuario", "Contraseña", "Correo", "Eliminar"]
    for col_idx, encabezado in enumerate(encabezados):
        tk.Label(contenedor, text=encabezado, font=("Helvetica", 12, "bold"), width=16, relief="solid", fg="blue").grid(row=1, column=col_idx, padx=5, pady=5)

    # Función para eliminar un usuario
    def eliminar_usuario(i, usuario_datos):
        try:
            # Leer el archivo de usuarios
            with open('usuarios.txt', 'r') as archivo:
                usuarios = archivo.readlines()

            # Eliminar el usuario correspondiente
            usuarios.pop(i)

            # Guardar los cambios de nuevo en el archivo
            with open('usuarios.txt', 'w') as archivo:
                archivo.writelines(usuarios)

            # Verificar si el archivo está vacío después de la eliminación
            if not usuarios:
                tk.messagebox.showinfo("Información", "Todos los usuarios han sido eliminados.")
                mostrar_bienvenido(None)  # Redirigir a la pantalla de bienvenida o login sin usuario

            # Recargar la lista de usuarios
            else:
                mostrar_lista_usuarios(usuario)

        except FileNotFoundError:
            tk.messagebox.showerror("Error", "No se encontró el archivo de usuarios.")

    # Cargar los usuarios desde el archivo
    try:
        with open('usuarios.txt', 'r') as archivo:
            usuarios = archivo.readlines()

        if not usuarios:
            tk.Label(contenedor, text="No hay usuarios registrados.", font=("Helvetica", 12)).grid(row=2, columnspan=4, pady=10)
        else:
            # Mostrar los datos de los usuarios en las filas de la tabla
            for i, usuario in enumerate(usuarios):
                datos_usuario = usuario.strip().split(",")  # Suponiendo que los datos están separados por comas
                tk.Label(contenedor, text=datos_usuario[0], font=("Helvetica", 12), width=18, relief="solid").grid(row=i + 2, column=0, padx=5, pady=5)
                tk.Label(contenedor, text=datos_usuario[1], font=("Helvetica", 12), width=18, relief="solid").grid(row=i + 2, column=1, padx=5, pady=5)
                tk.Label(contenedor, text=datos_usuario[2], font=("Helvetica", 12), width=18, relief="solid").grid(row=i + 2, column=2, padx=5, pady=5)

                # Crear el botón de eliminar en la última columna
                eliminar_button = tk.Button(contenedor, text="Eliminar", command=lambda i=i, usuario_datos=datos_usuario: eliminar_usuario(i, usuario_datos))
                eliminar_button.grid(row=i + 2, column=3, padx=5, pady=5)

    except FileNotFoundError:
        tk.Label(contenedor, text="No se encontró el archivo de usuarios.", font=("Helvetica", 12)).grid(row=2, columnspan=4, pady=10)

   

            

def mostrar_registro_programas(usuario):
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    root.geometry("1000x700")  # Establecer el tamaño de la ventana a 1000x1000

    # Crear el primer contenedor a la izquierda (Identificación del Programa)
    frame_izquierda = tk.Frame(frame_principal)
    frame_izquierda.grid(row=4, column=0, padx=20, pady=10, sticky="nw")

    # Crear botón de retroceso para regresar a la pantalla anterior
    tk.Button(frame_principal, text="Retroceder", command=lambda: mostrar_bienvenido(usuario)).grid(row=1, columnspan=4, pady=10)

    # Títulos y campos para el contenedor de la izquierda
    tk.Label(frame_izquierda, text="**1. Identificación del Programa**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_izquierda, text="ID del Programa:").grid(row=1, column=0, sticky="w")
    entry_id_programa = tk.Entry(frame_izquierda, width=40)  # Guardamos la referencia en una variable
    entry_id_programa.grid(row=1, column=1)

    tk.Label(frame_izquierda, text="Nombre del Programa:").grid(row=2, column=0, sticky="w")
    entry_nombre_programa = tk.Entry(frame_izquierda, width=40)
    entry_nombre_programa.grid(row=2, column=1)

    tk.Label(frame_izquierda, text="Descripción:").grid(row=3, column=0, sticky="w")
    entry_descripcion = tk.Entry(frame_izquierda, width=40)
    entry_descripcion.grid(row=3, column=1)

    # Crear el segundo contenedor a la derecha (Detalles del Programa)
    frame_derecha = tk.Frame(frame_principal)
    frame_derecha.grid(row=4, column=1, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la derecha
    tk.Label(frame_derecha, text="**2. Detalles del Programa**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_derecha, text="Categoría:").grid(row=1, column=0, sticky="w")
    entry_categoria = tk.Entry(frame_derecha, width=40)
    entry_categoria.grid(row=1, column=1)

    tk.Label(frame_derecha, text="Duración:").grid(row=2, column=0, sticky="w")
    entry_duracion = tk.Entry(frame_derecha, width=40)
    entry_duracion.grid(row=2, column=1)


    tk.Label(frame_derecha, text="Día y Hora de Emisión:").grid(row=4, column=0, sticky="w")
    entry_dia_hora = tk.Entry(frame_derecha, width=40)
    entry_dia_hora.grid(row=4, column=1)

    # Crear el tercer contenedor a la izquierda (Información de Transmisión)
    frame_izquierda3 = tk.Frame(frame_principal)
    frame_izquierda3.grid(row=5, column=0, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la izquierda (Información de Transmisión)
    tk.Label(frame_izquierda3, text="**3. Información de Transmisión**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_izquierda3, text="Tipo de Emisión:").grid(row=1, column=0, sticky="w")
    tipo_emision = tk.StringVar(value="En vivo")
    tk.Radiobutton(frame_izquierda3, text="En vivo", variable=tipo_emision, value="En vivo").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(frame_izquierda3, text="Grabado", variable=tipo_emision, value="Grabado").grid(row=1, column=2, sticky="w")

    tk.Label(frame_izquierda3, text="Plataforma:").grid(row=3, column=0, sticky="w")
    entry_plataforma = tk.Entry(frame_izquierda3, width=40)  # Guardamos la referencia en una variable
    entry_plataforma.grid(row=3, column=1)

    # Crear el cuarto contenedor a la derecha (Equipo del Programa)
    frame_derecha4 = tk.Frame(frame_principal)
    frame_derecha4.grid(row=5, column=1, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la derecha (Equipo del Programa)
    tk.Label(frame_derecha4, text="**4. Equipo del Programa**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_derecha4, text="Presentador(es):").grid(row=1, column=0, sticky="w")
    entry_presentadores = tk.Entry(frame_derecha4, width=40)  # Guardamos la referencia en una variable
    entry_presentadores.grid(row=1, column=1)

    tk.Label(frame_derecha4, text="Productor(es):").grid(row=3, column=0, sticky="w")
    entry_productores = tk.Entry(frame_derecha4, width=40)  # Guardamos la referencia en una variable
    entry_productores.grid(row=3, column=1)

    tk.Label(frame_derecha4, text="Técnico(s):").grid(row=4, column=0, sticky="w")
    entry_tecnicos = tk.Entry(frame_derecha4, width=40)  # Guardamos la referencia en una variable
    entry_tecnicos.grid(row=4, column=1)

    # Crear el quinto contenedor a la izquierda (Contenido del Programa)
    frame_izquierda5 = tk.Frame(frame_principal)
    frame_izquierda5.grid(row=6, column=0, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la izquierda (Contenido del Programa)
    tk.Label(frame_izquierda5, text="**5. Contenido del Programa**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_izquierda5, text="Temas:").grid(row=1, column=0, sticky="w")
    entry_temas = tk.Entry(frame_izquierda5, width=40)  # Referencia para el campo de Temas
    entry_temas.grid(row=1, column=1)

    tk.Label(frame_izquierda5, text="Música:").grid(row=3, column=0, sticky="w")
    entry_musica = tk.Entry(frame_izquierda5, width=40)  # Referencia para el campo de Música
    entry_musica.grid(row=3, column=1)

    # Crear el sexto contenedor a la derecha (Estadísticas y Audiencia)
    frame_derecha6 = tk.Frame(frame_principal)
    frame_derecha6.grid(row=6, column=1, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la izquierda (Enlaces y Material Adicional)
    tk.Label(frame_derecha6, text="**6. Enlaces y Material Adicional**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_derecha6, text="Grabación del Programa:").grid(row=1, column=0, sticky="w")
    entry_grabacion = tk.Entry(frame_derecha6, width=40)  # Referencia para el campo de Grabación
    entry_grabacion.grid(row=1, column=1)

    tk.Label(frame_derecha6, text="Material Promocional:").grid(row=3, column=0, sticky="w")
    entry_material_promocional = tk.Entry(frame_derecha6, width=40)  # Referencia para el campo de Material Promocional
    entry_material_promocional.grid(row=3, column=1)

    # Crear el séptimo contenedor a la izquierda (Enlaces y Material Adicional)
    frame_izquierda7 = tk.Frame(frame_principal)
    frame_izquierda7.grid(row=7, column=0, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la derecha (Fecha y Modificaciones)
    tk.Label(frame_izquierda7, text="**7. Fecha y Modificaciones**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_izquierda7, text="Fecha de Creación:").grid(row=1, column=0, sticky="w")
    entry_fecha_creacion = tk.Entry(frame_izquierda7, width=40)  # Referencia para el campo de Fecha de Creación
    entry_fecha_creacion.grid(row=1, column=1)

    # Crear el octavo contenedor a la derecha (Fecha y Modificaciones)
    frame_derecha8 = tk.Frame(frame_principal)
    frame_derecha8.grid(row=7, column=1, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la izquierda (Estado del Programa)
    tk.Label(frame_derecha8, text="**8. Estado del Programa**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_derecha8, text="Estado:").grid(row=1, column=0, sticky="w")
    estado_programa = tk.StringVar(value="Activo")
    tk.Radiobutton(frame_derecha8, text="Activo", variable=estado_programa, value="Activo").grid(row=1, column=1, sticky="w")
    tk.Radiobutton(frame_derecha8, text="Inactivo", variable=estado_programa, value="Inactivo").grid(row=1, column=2, sticky="w")

    # Crear el noveno contenedor a la izquierda (Estado del Programa)
    frame_izquierda9 = tk.Frame(frame_principal)
    frame_izquierda9.grid(row=8, column=0, padx=20, pady=10, sticky="nw")

    # Títulos y campos para el contenedor de la derecha (Notas Adicionales)
    tk.Label(frame_izquierda9, text="**9. Notas Adicionales**", font=("Helvetica", 10, "bold")).grid(row=0, columnspan=2, sticky="w")
    tk.Label(frame_izquierda9, text="Observaciones:").grid(row=1, column=0, sticky="w")
    entry_observaciones = tk.Entry(frame_izquierda9, width=40)  # Referencia para el campo de Observaciones
    entry_observaciones.grid(row=1, column=1)

    # Crear el décimo contenedor a la derecha (Notas Adicionales)
    frame_derecha10 = tk.Frame(frame_principal)
    frame_derecha10.grid(row=8, column=1, padx=20, pady=10, sticky="nw")

    

    # Función para guardar la información en el archivo de texto
    def registrar_programa():
        # Obtener los valores de los entrys
        id_programa = entry_id_programa.get()
        nombre_programa = entry_nombre_programa.get()
        descripcion = entry_descripcion.get()
        categoria = entry_categoria.get()
        duracion = entry_duracion.get()
        dia_hora = entry_dia_hora.get()
    
        # Obtener los nuevos valores de los entrys
        tipo_emision_val = tipo_emision.get()
        plataforma = entry_plataforma.get()
        presentadores = entry_presentadores.get()
        productores = entry_productores.get()
        tecnicos = entry_tecnicos.get()

        temas = entry_temas.get()
        musica = entry_musica.get()
    
        grabacion = entry_grabacion.get()
        material_promocional = entry_material_promocional.get()
        fecha_creacion = entry_fecha_creacion.get()

        estado_programa_val = estado_programa.get()
        observaciones = entry_observaciones.get()

        # Validar que los campos no estén vacíos
        if not id_programa or not nombre_programa or not descripcion or not categoria or not duracion or not dia_hora or not plataforma or not presentadores or not productores or not tecnicos or not temas or not musica or not grabacion or not material_promocional or not fecha_creacion or not estado_programa_val or (estado_programa_val == "Cancelado") or not observaciones:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Guardar los datos en un archivo de texto (formato con todos los campos nuevos)
        with open('programas.txt', 'a') as archivo:
            archivo.write(f"{id_programa},{nombre_programa},{descripcion},{categoria},{duracion},{dia_hora},{tipo_emision_val},{plataforma},{presentadores},{productores},{tecnicos},{temas},{musica},{grabacion},{material_promocional},{fecha_creacion},{estado_programa_val},{observaciones}\n")
    
        messagebox.showinfo("Éxito", "Programa registrado exitosamente")

    # Botón para registrar el programa
    tk.Button(frame_principal, text="Registrar Programa", command=registrar_programa).grid(row=9, columnspan=2, pady=10)
    # Asegúrate de que el botón "Cerrar sesión" esté en la fila 10 y la columna correcta
    tk.Button(frame_principal, text="Cerrar sesión", command=cerrar_sesion, width=15).grid(row=10, column=0, columnspan=2, pady=20)

def mostrar_ver_programas(usuario):
    # Limpiar el frame actual
    for widget in frame_principal.winfo_children():
        widget.grid_forget()

    root.geometry("1950x1000")  # Establecer el tamaño de la ventana a 1000x1000

    # Mostrar mensaje y los botones para ver programas
    tk.Label(frame_principal, text="Programas Registrados!!", font=("Helvetica", 16)).grid(row=0, columnspan=4, pady=20)

    # Crear botón de retroceso para regresar a la pantalla anterior
    tk.Button(frame_principal, text="Retroceder", command=lambda: mostrar_bienvenido(usuario)).grid(row=1, columnspan=4, pady=10)

    # Aquí puedes agregar una lista o los detalles para ver los programas registrados si lo deseas

    # Función para leer los programas desde el archivo
    def cargar_programas():
        try:
            with open('programas.txt', 'r') as archivo:
                programas = archivo.readlines()

            if not programas:
                messagebox.showinfo("Información", "No hay programas registrados.")
                return

            # Crear un Frame para mostrar los programas
            frame_programas = tk.Frame(frame_principal)
            frame_programas.grid(row=2, columnspan=4, padx=20, pady=10)

             # Encabezados de las columnas
            columnas = [
                "ID", "Nombre", "Descripción", "Categoria", "Duración", "Dia-Hora", "Tipo-Emisión", "Plataforma",
                "Presentadores", "Productores", "Tecnicos", "Temas", "Musica","Grabacion", "Material Prom.", 
                "Fecha Creacion", "Estado", "Obs", "Eliminar", "Editar"
            ]
            for col_idx, columna in enumerate(columnas):
                tk.Label(frame_programas, text=columna, width=12, anchor="center", relief="solid",  fg="blue").grid(row=0, column=col_idx)

            # Función para eliminar un programa
            def eliminar_programa(i, datos_programa):
                # Eliminar la fila del archivo
                with open('programas.txt', 'r') as archivo:
                    programas = archivo.readlines()

                # Eliminar la línea correspondiente
                programas.pop(i)

                with open('programas.txt', 'w') as archivo:
                    archivo.writelines(programas)

                # Actualizar la vista
                for widget in frame_programas.winfo_children():
                    widget.grid_forget()

                cargar_programas()

            # Función para editar un programa
            def editar_programa(i, datos_programa):
                # Eliminar la fila actual para mostrar campos de edición
                for widget in frame_programas.winfo_children():
                    widget.grid_forget()


                # Mostrar las entradas (Entry) para cada campo, pero en forma vertical
                entradas = []
                for row_idx, (columna, dato) in enumerate(zip(columnas, datos_programa[:22])):  # Primero las columnas y los datos
                    tk.Label(frame_programas, text=columna, width=20, anchor="w", relief="solid", fg="blue").grid(row=row_idx, column=0)  # Mostrar nombre de la columna
                    entrada = tk.Entry(frame_programas, width=50)
                    entrada.grid(row=row_idx, column=1)  # Cada campo de entrada en la columna 1
                    entrada.insert(0, dato)
                    entradas.append(entrada)

                # Función para guardar los cambios
                def guardar_cambios():
                    # Obtener los nuevos datos
                    nuevos_datos = [entrada.get() for entrada in entradas]

                    # Volver a cargar los programas y actualizar el archivo
                    with open('programas.txt', 'r') as archivo:
                        programas = archivo.readlines()

                    # Reemplazar la línea editada con los nuevos datos
                    programas[i] = ",".join(nuevos_datos) + "\n"

                    with open('programas.txt', 'w') as archivo:
                        archivo.writelines(programas)

                    # Recargar la tabla con los datos actualizados
                    for widget in frame_programas.winfo_children():
                        widget.grid_forget()

                    cargar_programas()

                # Función para cancelar la edición y volver a la tabla
                def cancelar_edicion():
                    # Recargar la tabla sin guardar cambios
                    for widget in frame_programas.winfo_children():
                        widget.grid_forget()

                    cargar_programas()

                # Botón para guardar los cambios
                tk.Button(frame_programas, text="Guardar", command=guardar_cambios).grid(row=len(columnas), columnspan=2, pady=10)

                # Botón para cancelar la edición y volver a la tabla
                tk.Button(frame_programas, text="Cancelar", command=cancelar_edicion).grid(row=len(columnas) + 1, columnspan=2, padx=10)

            # Mostrar los programas registrados
            for i, programa in enumerate(programas):
                datos_programa = programa.strip().split(",")  # Divide los datos por comas
                for j, dato in enumerate(datos_programa[:22]):  # Aseguramos que solo haya 22 columnas de datos
                    tk.Label(frame_programas, text=dato, width=12, anchor="w", relief="solid").grid(row=i + 1, column=j)

                # Crear el botón de eliminar en la última columna
                eliminar_button = tk.Button(frame_programas, text="Eliminar", command=lambda i=i, datos_programa=datos_programa: eliminar_programa(i, datos_programa))
                eliminar_button.grid(row=i + 1, column=18, padx=5, pady=5)

                # Crear el botón de editar al lado del botón eliminar
                editar_button = tk.Button(frame_programas, text="Editar", command=lambda i=i, datos_programa=datos_programa: editar_programa(i, datos_programa))
                editar_button.grid(row=i + 1, column=19, padx=5, pady=5)

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo de programas no existe.")

    # Botón para cargar los programas
    tk.Button(frame_principal, text="Cargar Programas", command=cargar_programas).grid(row=2, columnspan=4, pady=10)



# Función para cerrar sesión y volver al login
def cerrar_sesion():
    # Restablecer el tamaño de la ventana al tamaño original
    root.geometry("500x600")  # Tamaño original de la ventana
    mostrar_login()  # Volver a la pantalla de login

# Ventana principal
root = tk.Tk()
root.title("Registro de Programas")
root.geometry("500x600")
root.resizable(False, False)

# Cargar y mostrar la imagen
imagen = tk.PhotoImage(file="images/imagen.png")  # Ruta a tu imagen PNG

# Crear un frame dentro de la ventana principal
frame_principal = tk.Frame(root)
frame_principal.pack(padx=20, pady=20)

# Mostrar el formulario de login inicialmente
mostrar_login()

root.mainloop()
