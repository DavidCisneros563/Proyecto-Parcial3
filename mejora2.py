import sqlite3
import tkinter as tk
from tkinter import messagebox

# Función para conectar y consultar la base de datos
def obtener_pokemon(tipo_enemigo, tipo_preferencia, nivel_preferencia, velocidad_preferencia):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('pokemon_battle.db')
        cursor = conn.cursor()

        # Consultar los tipos fuertes contra el tipo enemigo
        cursor.execute("SELECT tipo_fuerte FROM relaciones WHERE tipo_debil = ?", (tipo_enemigo,))
        tipos_fuertes = cursor.fetchall()

        # Si no hay tipos fuertes contra el enemigo, devolver mensaje
        if not tipos_fuertes:
            return "No se encontraron Pokémon con ventaja contra este tipo."

        # Convertir la lista de resultados en una lista simple
        tipos_fuertes = [tipo[0] for tipo in tipos_fuertes]

        # Crear consulta para buscar Pokémon que coincidan con las preferencias
        placeholders = ",".join("?" for _ in tipos_fuertes)
        query = f'''
        SELECT nombre, tipo, tipo_ataque, nivel, velocidad
        FROM pokemons
        WHERE tipo IN ({placeholders}) AND tipo_ataque = ? AND nivel = ? AND velocidad = ?
        '''
        params = tipos_fuertes + [tipo_preferencia, nivel_preferencia, velocidad_preferencia]

        cursor.execute(query, params)
        pokemons = cursor.fetchall()

        conn.close()

        # Si no hay Pokémon recomendados, indicar que no se encontró ninguno
        if not pokemons:
            return "No se encontraron Pokémon adecuados."

        # Mostrar las tres primeras recomendaciones
        return "\n".join([f"{nombre} ({tipo}, {tipo_ataque}, {nivel}, {velocidad})" for nombre, tipo, tipo_ataque, nivel, velocidad in pokemons[:3]])

    except sqlite3.Error as e:
        return f"Error en la base de datos: {e}"

# Función para manejar la entrada de la encuesta
def obtener_recomendaciones():
    tipo_enemigo = tipo_enemigo_var.get().strip().lower()  # Convertir a minúsculas y quitar espacios
    tipo_preferencia = tipo_preferencia_var.get().strip().lower()
    nivel_preferencia = nivel_preferencia_var.get().strip().lower()
    velocidad_preferencia = velocidad_preferencia_var.get().strip().lower()

    # Validar que todos los campos estén completos
    if not (tipo_enemigo and tipo_preferencia and nivel_preferencia and velocidad_preferencia):
        messagebox.showwarning("Advertencia", "Por favor, responde todas las preguntas.")
        return

    # Obtener recomendaciones
    recomendaciones = obtener_pokemon(tipo_enemigo, tipo_preferencia, nivel_preferencia, velocidad_preferencia)
    messagebox.showinfo("Recomendaciones", recomendaciones)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Experto Pokémon")
root.geometry("500x500")
root.config(bg="#D8B6D9")  # Color de fondo morado claro (lavanda)

# Etiquetas y campos de entrada con colores morados
tk.Label(root, text="¿Cuál es el tipo de Pokémon enemigo? (fuego, agua, planta, etc.):", bg="#D8B6D9", fg="purple", font=("Arial", 12)).pack(pady=10)
tipo_enemigo_var = tk.StringVar()
tk.Entry(root, textvariable=tipo_enemigo_var, bg="white", font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="¿Prefieres un Pokémon de tipo físico o especial? (físico/especial):", bg="#D8B6D9", fg="purple", font=("Arial", 12)).pack(pady=10)
tipo_preferencia_var = tk.StringVar()
tk.Entry(root, textvariable=tipo_preferencia_var, bg="white", font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="¿Qué nivel de poder prefieres para el Pokémon? (bajo/medio/alto):", bg="#D8B6D9", fg="purple", font=("Arial", 12)).pack(pady=10)
nivel_preferencia_var = tk.StringVar()
tk.Entry(root, textvariable=nivel_preferencia_var, bg="white", font=("Arial", 10)).pack(pady=5)

tk.Label(root, text="¿Tienes alguna preferencia por la velocidad del Pokémon? (alta/media/baja):", bg="#D8B6D9", fg="purple", font=("Arial", 12)).pack(pady=10)
velocidad_preferencia_var = tk.StringVar()
tk.Entry(root, textvariable=velocidad_preferencia_var, bg="white", font=("Arial", 10)).pack(pady=5)

# Agregar botón con colores morados
tk.Button(root, text="Obtener Recomendaciones", command=obtener_recomendaciones, bg="#9B59B6", fg="white", font=("Arial", 12)).pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()
