import sqlite3

def elegir_pokemon(tipo_enemigo):
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
    
    # Consultar Pokémon con tipos fuertes contra el enemigo
    cursor.execute('''
    SELECT nombre FROM pokemons WHERE tipo IN ({})
    '''.format(','.join('?' * len(tipos_efectivos))), tuple(tipos_efectivos))
    
    candidatos = cursor.fetchall()
    
    if candidatos:
        print(f"Recomendados para la batalla contra un Pokémon de tipo {tipo_enemigo}: {', '.join([pokemon[0] for pokemon in candidatos])}")
    else:
        print(f"No se encontraron Pokémon con ventaja contra {tipo_enemigo}.")
    
    # Cerrar la conexión
    conn.close()

# Solicitar al usuario el tipo del Pokémon enemigo
tipo_enemigo = input("Ingresa el tipo del Pokémon enemigo (por ejemplo, fuego, agua, planta): ").lower()
elegir_pokemon(tipo_enemigo)
