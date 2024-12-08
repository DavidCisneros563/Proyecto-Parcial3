import sqlite3

# Conectamos a la base de datos (se crea si no existe)
conn = sqlite3.connect('pokemon_battle.db')
cursor = conn.cursor()

# Crear tablas
cursor.execute('''
CREATE TABLE IF NOT EXISTS pokemons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS relaciones (
    tipo_debil TEXT NOT NULL,
    tipo_fuerte TEXT NOT NULL,
    PRIMARY KEY (tipo_debil, tipo_fuerte)
);
''')

# Insertar Pokémon y relaciones en la base de datos
cursor.execute('''
INSERT OR IGNORE INTO pokemons (nombre, tipo) VALUES
('Charizard', 'fuego'),
('Venusaur', 'planta'),
('Pikachu', 'eléctrico'),
('Blastoise', 'agua'),
('Machop', 'lucha'),
('Jolteon', 'eléctrico');
''')

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