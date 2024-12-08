import sqlite3  # Asegúrate de importar sqlite3 al inicio del código

# Crear conexión con la base de datos (se crea el archivo si no existe)
conn = sqlite3.connect('pokemon_battle.db')
cursor = conn.cursor()

# Crear la tabla de tipos de Pokémon
cursor.execute('''
CREATE TABLE IF NOT EXISTS tipos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL
)
''')

# Crear la tabla de Pokémon
cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL
)
''')

# Crear la tabla de relaciones de tipos (quién es fuerte contra quién)
cursor.execute('''
CREATE TABLE IF NOT EXISTS relaciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo_fuerte TEXT NOT NULL,
    tipo_debil TEXT NOT NULL,
    FOREIGN KEY (tipo_fuerte) REFERENCES tipos (nombre),
    FOREIGN KEY (tipo_debil) REFERENCES tipos (nombre)
)
''')

# Insertar los tipos de Pokémon
tipos = ['fuego', 'agua', 'planta', 'electrico', 'tierra', 'volador', 'hielo', 'bicho', 'roca', 'dragón', 'lucha', 'fantasma', 'hada']
for tipo in tipos:
    cursor.execute('INSERT OR IGNORE INTO tipos (nombre) VALUES (?)', (tipo,))

# Insertar algunos Pokémon y sus tipos
pokemons = [
    ('Charizard', 'fuego'),
    ('Blastoise', 'agua'),
    ('Venusaur', 'planta'),
    ('Pikachu', 'electrico'),
    ('Golem', 'tierra'),
    ('Dragonite', 'dragón'),
    ('Alakazam', 'psíquico'),
    ('Machamp', 'lucha'),
    ('Gardevoir', 'hada'),
    ('Tyranitar', 'roca')
]

for pokemon, tipo in pokemons:
    cursor.execute('INSERT OR IGNORE INTO pokemons (nombre, tipo) VALUES (?, ?)', (pokemon, tipo))

# Insertar relaciones de tipos
relaciones = [
    ('fuego', 'planta'), ('fuego', 'hielo'), ('fuego', 'bicho'), ('fuego', 'acero'),
    ('agua', 'fuego'), ('agua', 'tierra'), ('agua', 'roca'),
    ('planta', 'agua'), ('planta', 'tierra'), ('planta', 'roca'),
    ('electrico', 'agua'), ('electrico', 'volador'),
    ('tierra', 'agua'), ('tierra', 'fuego'), ('tierra', 'electrico'), ('tierra', 'roca'), ('tierra', 'acero'),
    ('volador', 'planta'), ('volador', 'lucha'), ('volador', 'bicho'),
    ('hielo', 'planta'), ('hielo', 'tierra'), ('hielo', 'volador'), ('hielo', 'dragón'),
    ('bicho', 'planta'), ('bicho', 'psíquico'), ('bicho', 'oscuro'),
    ('roca', 'fuego'), ('roca', 'hielo'), ('roca', 'volador'), ('roca', 'bicho'),
    ('dragón', 'dragón'),
    ('lucha', 'hielo'), ('lucha', 'roca'), ('lucha', 'acero'), ('lucha', 'siniestro'), ('lucha', 'hada'),
    ('fantasma', 'fantasma'), ('fantasma', 'psíquico'),
    ('hada', 'lucha'), ('hada', 'dragón'), ('hada', 'siniestro')
]

for tipo_fuerte, tipo_debil in relaciones:
    cursor.execute('INSERT OR IGNORE INTO relaciones (tipo_fuerte, tipo_debil) VALUES (?, ?)', (tipo_fuerte, tipo_debil))

# Confirmar cambios
conn.commit()

# Función para recomendar un Pokémon basado en el tipo enemigo
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