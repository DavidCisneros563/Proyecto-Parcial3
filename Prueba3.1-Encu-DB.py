import sqlite3

# Conectar a la base de datos (se crea si no existe)
conn = sqlite3.connect('pokemon_battle.db')
cursor = conn.cursor()

# Crear tablas si no existen
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

# Insertar 20 Pokémon en la base de datos
cursor.execute('''
INSERT OR IGNORE INTO pokemons (nombre, tipo) VALUES
('Charizard', 'fuego'),
('Venusaur', 'planta'),
('Pikachu', 'eléctrico'),
('Blastoise', 'agua'),
('Machop', 'lucha'),
('Jolteon', 'eléctrico'),
('Golem', 'roca'),
('Alakazam', 'psíquico'),
('Lucario', 'lucha/acero'),
('Snorlax', 'normal'),
('Dragonite', 'dragón'),
('Gyarados', 'agua/volador'),
('Espeon', 'psíquico'),
('Tyranitar', 'roca/siniestro'),
('Garchomp', 'dragón/tierra'),
('Lapras', 'agua/hielo'),
('Arcanine', 'fuego'),
('Jolteon', 'eléctrico'),
('Clefairy', 'hada'),
('Mewtwo', 'psíquico');
''')

# Insertar relaciones de tipos (qué tipo vence a cuál)
cursor.execute('''
INSERT OR IGNORE INTO relaciones (tipo_debil, tipo_fuerte) VALUES
('agua', 'fuego'),
('agua', 'roca'),
('fuego', 'planta'),
('fuego', 'hielo'),
('eléctrico', 'agua'),
('eléctrico', 'volador'),
('planta', 'agua'),
('planta', 'tierra'),
('lucha', 'normal'),
('lucha', 'hielo'),
('lucha', 'roca'),
('lucha', 'siniestro'),
('psíquico', 'lucha'),
('psíquico', 'veneno'),
('dragón', 'dragón'),
('hielo', 'volador'),
('hielo', 'dragón'),
('hielo', 'planta'),
('hielo', 'tierra');
''')

# Confirmar que los datos fueron insertados correctamente
conn.commit()

# Confirmación
print("Base de datos creada y poblada con 20 Pokémon correctamente.")

# Cerrar la conexión
conn.close()