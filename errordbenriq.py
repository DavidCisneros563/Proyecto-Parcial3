import sqlite3

# Conectamos a la base de datos (se crea si no existe)
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

# Insertar Pokémon de cada tipo
cursor.execute('''
INSERT OR IGNORE INTO pokemons (nombre, tipo) VALUES
('Charizard', 'fuego'),
('Venusaur', 'planta'),
('Pikachu', 'eléctrico'),
('Blastoise', 'agua'),
('Machop', 'lucha'),
('Jolteon', 'eléctrico'),
('Glaceon', 'hielo'),
('Alakazam', 'psíquico'),
('Onix', 'roca'),
('Gengar', 'fantasma'),
('Umbreon', 'siniestro'),
('Steelix', 'acero'),
('Sylveon', 'hada'),
('Pidgeot', 'volador'),
('Groudon', 'tierra'),
('Dragonite', 'dragón'),
('Scyther', 'bicho'),
('Weezing', 'veneno'),
('Snorlax', 'normal');
''')

# Insertar relaciones de tipos
cursor.execute('''
INSERT OR IGNORE INTO relaciones (tipo_debil, tipo_fuerte) VALUES
('agua', 'eléctrico'),
('agua', 'planta'),
('fuego', 'agua'),
('fuego', 'roca'),
('eléctrico', 'tierra'),
('hielo', 'fuego'),
('hielo', 'roca'),
('psíquico', 'siniestro'),
('roca', 'agua'),
('fantasma', 'normal'),
('siniestro', 'psíquico'),
('acero', 'fuego'),
('hada', 'dragón'),
('volador', 'eléctrico'),
('tierra', 'agua'),
('dragón', 'hielo'),
('bicho', 'volador'),
('veneno', 'psíquico'),
('normal', 'lucha');
''')

# Confirmar que los datos han sido insertados
conn.commit()

print("Base de datos creada y poblada correctamente.")

# Cerrar la conexión
conn.close()