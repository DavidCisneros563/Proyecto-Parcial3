import sqlite3

# Conectamos a la base de datos (se crea si no existe)
conn = sqlite3.connect('pokemon_battle.db')
cursor = conn.cursor()

# Crear las tablas
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

# Insertar Pokémon en la base de datos (3 ejemplos para cada uno)
cursor.execute('''
INSERT OR IGNORE INTO pokemons (nombre, tipo, tipo_ataque, nivel, velocidad) VALUES
('Charizard', 'fuego', 'físico', 'alto', 'alta'),
('Charmeleon', 'fuego', 'especial', 'medio', 'alta'),
('Charmander', 'fuego', 'físico', 'bajo', 'baja'),
('Venusaur', 'planta', 'especial', 'medio', 'media'),
('Venusaur', 'planta', 'físico', 'alto', 'baja'),
('Venusaur', 'planta', 'especial', 'bajo', 'media'),
('Pikachu', 'eléctrico', 'especial', 'alto', 'alta'),
('Pikachu', 'eléctrico', 'físico', 'medio', 'alta'),
('Pikachu', 'eléctrico', 'especial', 'bajo', 'media'),
('Blastoise', 'agua', 'físico', 'alto', 'media'),
('Blastoise', 'agua', 'especial', 'medio', 'alta'),
('Blastoise', 'agua', 'físico', 'bajo', 'baja'),
('Machop', 'lucha', 'físico', 'alto', 'baja'),
('Machop', 'lucha', 'físico', 'medio', 'media'),
('Machop', 'lucha', 'especial', 'bajo', 'alta'),
('Jolteon', 'eléctrico', 'especial', 'medio', 'alta'),
('Jolteon', 'eléctrico', 'físico', 'bajo', 'alta'),
('Jolteon', 'eléctrico', 'especial', 'alto', 'alta');
''')

# Insertar relaciones entre tipos
cursor.execute('''
INSERT OR IGNORE INTO relaciones (tipo_debil, tipo_fuerte) VALUES
('agua', 'eléctrico'),
('agua', 'planta'),
('fuego', 'agua'),
('fuego', 'roca'),
('eléctrico', 'tierra');
''')

# Confirmamos que los datos han sido insertados
conn.commit()

print("Base de datos creada y poblada correctamente.")

# Cerrar la conexión
conn.close()
