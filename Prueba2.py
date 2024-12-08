import sqlite3

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
    nombre TEXT UNIQUE NOT NULL
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
    cursor.execute('INSERT OR IGNORE INTO pokemons (nombre) VALUES (?)', (pokemon,))

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