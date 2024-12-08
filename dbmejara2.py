import sqlite3

# Conectamos a la base de datos (se crea si no existe)
conn = sqlite3.connect('pokemon_battle.db')
cursor = conn.cursor()

# Crear las tablas con la columna correcta
cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL,
    tipo_ataque TEXT NOT NULL,
    nivel TEXT NOT NULL,
    velocidad TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS relaciones (
    tipo_debil TEXT NOT NULL,
    tipo_fuerte TEXT NOT NULL,
    PRIMARY KEY (tipo_debil, tipo_fuerte)
);
''')

# Insertar datos de prueba en las tablas
cursor.executemany('''
INSERT OR IGNORE INTO pokemons (nombre, tipo, tipo_ataque, nivel, velocidad) VALUES (?, ?, ?, ?, ?)
''', [
    ('Charizard', 'fuego', 'físico', 'alto', 'alta'),
    ('Charmeleon', 'fuego', 'especial', 'medio', 'alta'),
    ('Charmander', 'fuego', 'físico', 'bajo', 'baja'),
    ('Venusaur', 'planta', 'especial', 'medio', 'media'),
    ('Pikachu', 'eléctrico', 'especial', 'alto', 'alta'),
    ('Blastoise', 'agua', 'físico', 'alto', 'media')
])

cursor.executemany('''
INSERT OR IGNORE INTO relaciones (tipo_debil, tipo_fuerte) VALUES (?, ?)
''', [
    ('agua', 'eléctrico'),
    ('fuego', 'agua'),
    ('eléctrico', 'tierra')
])

conn.commit()
conn.close()

print("Base de datos recreada correctamente.")
