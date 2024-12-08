import sqlite3  # Importar sqlite3

# Crear conexión con la base de datos (se crea el archivo si no existe)
conn = sqlite3.connect('pokemon_battle.db')
cursor = conn.cursor()

# Función para realizar la encuesta
def realizar_encuesta():
    print("¡Bienvenido al sistema experto de Pokémon!")
    print("Por favor, responde las siguientes preguntas:")
    
    tipo_enemigo = input("1. ¿Cuál es el tipo de Pokémon enemigo? (fuego, agua, planta, etc.): ").lower()
    estilo_lucha = input("2. ¿Prefieres un Pokémon de tipo físico o especial? (físico/especial): ").lower()
    importancia_defensa = input("3. ¿Te interesa que el Pokémon tenga habilidades de defensa o ataque? (defensa/ataque): ").lower()
    nivel_poder = input("4. ¿Qué nivel de poder prefieres para el Pokémon? (bajo/medio/alto): ").lower()
    velocidad_preferida = input("5. ¿Tienes alguna preferencia por la velocidad del Pokémon? (alta/media/baja): ").lower()

    # Almacenamos las respuestas en un diccionario
    respuestas = {
        "tipo_enemigo": tipo_enemigo,
        "estilo_lucha": estilo_lucha,
        "importancia_defensa": importancia_defensa,
        "nivel_poder": nivel_poder,
        "velocidad_preferida": velocidad_preferida
    }
    
    return respuestas

# Función para recomendar un Pokémon basado en el tipo enemigo y las respuestas de la encuesta
def elegir_pokemon(respuestas):
    tipo_enemigo = respuestas["tipo_enemigo"]
    
    # Conectar a la base de datos
    conn = sqlite3.connect('pokemon_battle.db')
    cursor = conn.cursor()

    # Consultar los tipos fuertes contra el tipo enemigo
    cursor.execute('''
    SELECT tipo_fuerte FROM relaciones WHERE tipo_debil = ?
    ''', (tipo_enemigo,))
    
    tipos_efectivos = [row[0] for row in cursor.fetchall()]
    
    if not tipos_efectivos:
        print(f"No se encontraron contra-efectos para el tipo {tipo_enemigo}.")
        conn.close()
        return
    
    print(f"Tipos fuertes contra {tipo_enemigo}: {', '.join(tipos_efectivos)}")
    
    # Basado en la encuesta, ajustamos la recomendación:
    # Si el usuario prefiere ataque o defensa, o si tiene una preferencia por la velocidad, se puede modificar
    if respuestas["importancia_defensa"] == "defensa":
        print("Buscaremos un Pokémon con más habilidades defensivas.")
    if respuestas["estilo_lucha"] == "físico":
        print("Buscando un Pokémon con más habilidades físicas.")
    if respuestas["velocidad_preferida"] == "alta":
        print("Buscando un Pokémon con alta velocidad.")
    
    # Consultar Pokémon con tipos fuertes contra el enemigo
    cursor.execute('''
    SELECT nombre, tipo FROM pokemons WHERE tipo IN ({})
    '''.format(','.join('?' * len(tipos_efectivos))), tuple(tipos_efectivos))
    
    candidatos = cursor.fetchall()
    
    if candidatos:
        print(f"Recomendados para la batalla contra un Pokémon de tipo {tipo_enemigo}:")
        for pokemon in candidatos:
            print(f"- {pokemon[0]} (Tipo: {pokemon[1]})")
    else:
        print(f"No se encontraron Pokémon con ventaja contra {tipo_enemigo}.")
    
    # Cerrar la conexión
    conn.close()

# Realizar la encuesta
respuestas = realizar_encuesta()

# Recomendación de Pokémon basada en las respuestas de la encuesta
elegir_pokemon(respuestas)
