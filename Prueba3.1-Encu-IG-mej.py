import sqlite3
import tkinter as tk
from tkinter import messagebox

# Función para conectar y consultar la base de datos
def obtener_pokemon(tipo_enemigo, tipo_preferencia, nivel_preferencia, velocidad_preferencia):
    # Conectar a la base de datos
    conn = sqlite3.connect('pokemon_battle.db')
    cursor = conn.cursor()

    # Consultar los tipos fuertes contra el tipo enemigo
    cursor.execute("SELECT tipo_fuerte FROM relaciones WHERE tipo_debil = ?", (tipo_enemigo,))
    tipos_fuertes = cursor.fetchall()

    # Si no hay tipos fuertes contra el enemigo, devolver mensaje
    if not tipos_fuertes:
        return "No se encontraron Pokémon con ventaja contra este tipo."

    tipos_fuertes = [tipo[0] for tipo in tipos_fuertes]

    # Consultar los Pokémon que tienen esos tipos
    cursor.execute("SELECT nombre, tipo FROM pokemons WHERE tipo IN ({})".format(",".join("?" * len(tipos_fuertes))), tipos_fuertes)
    pokemons = cursor.fetchall()

    # Filtrar Pokémon según la preferencia de tipo (físico/especial), nivel y velocidad
    recomendados = []
    for pokemon in pokemons:
        nombre, tipo = pokemon
        recomendados.append(f"{nombre} ({tipo})")

    conn.close()

    # Si no hay Pokémon recomendados, indicar que no se encontró ninguno
    if not recomendados:
        return "No se encontraron Pokémon adecuados."

    return "\n".join(recomendados[:3])  # Mostrar solo 3 recomendaciones

# Función para manejar la entrada de la encuesta
def obtener_recomendaciones():
    tipo_enemigo = tipo_enemigo_var.get().lower()  # Convertir la entrada a minúsculas para mayor consistencia
    tipo_preferencia = tipo_preferencia_var.get().lower()
    nivel_preferencia = nivel_preferencia_var.get().lower()
    velocidad_preferencia = velocidad_preferencia_var.get().lower()

    if tipo_enemigo and tipo_preferencia and nivel_preferencia and velocidad_preferencia:
        recomendaciones = obtener_pokemon(tipo_enemigo, tipo_preferencia, nivel_preferencia, velocidad_preferencia)
        messagebox.showinfo("Recomendaciones", recomendaciones)
    else:
        messagebox.showwarning("Advertencia", "Por favor, responde todas las preguntas.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Experto Pokémon")
root.geometry("400x400")

# Etiquetas y campos de entrada
tk.Label(root, text="¿Cuál es el tipo de Pokémon enemigo? (fuego, agua, planta, etc.):").pack(pady=10)
tipo_enemigo_var = tk.StringVar()
tk.Entry(root, textvariable=tipo_enemigo_var).pack(pady=5)

tk.Label(root, text="¿Prefieres un Pokémon de tipo físico o especial? (físico/especial):").pack(pady=10)
tipo_preferencia_var = tk.StringVar()
tk.Entry(root, textvariable=tipo_preferencia_var).pack(pady=5)

tk.Label(root, text="¿Qué nivel de poder prefieres para el Pokémon? (bajo/medio/alto):").pack(pady=10)
nivel_preferencia_var = tk.StringVar()
tk.Entry(root, textvariable=nivel_preferencia_var).pack(pady=5)

tk.Label(root, text="¿Tienes alguna preferencia por la velocidad del Pokémon? (alta/media/baja):").pack(pady=10)
velocidad_preferencia_var = tk.StringVar()
tk.Entry(root, textvariable=velocidad_preferencia_var).pack(pady=5)

# Botón para obtener recomendaciones
tk.Button(root, text="Obtener Recomendaciones", command=obtener_recomendaciones).pack(pady=20)

# Iniciar la interfaz gráfica
root.mainloop()
