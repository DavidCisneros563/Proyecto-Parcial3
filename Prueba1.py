# Diccionario de relaciones de tipos de Pokémon (quién es fuerte contra quién)
tipos_fuertes = {
    'fuego': ['planta', 'hielo', 'bicho', 'acero'],
    'agua': ['fuego', 'tierra', 'roca'],
    'planta': ['agua', 'tierra', 'roca'],
    'electrico': ['agua', 'volador'],
    'tierra': ['agua', 'fuego', 'electrico', 'roca', 'acero'],
    'volador': ['planta', 'lucha', 'bicho'],
    'hielo': ['planta', 'tierra', 'volador', 'dragón'],
    'bicho': ['planta', 'psíquico', 'oscuro'],
    'roca': ['fuego', 'hielo', 'volador', 'bicho'],
    'dragón': ['dragón'],
    'lucha': ['hielo', 'roca', 'acero', 'siniestro', 'hada'],
    'fantasma': ['fantasma', 'psíquico'],
    'hada': ['lucha', 'dragón', 'siniestro']
}

# Lista de Pokémon con sus tipos
pokemons = {
    'Charizard': ['fuego', 'volador'],
    'Blastoise': ['agua'],
    'Venusaur': ['planta', 'veneno'],
    'Pikachu': ['electrico'],
    'Golem': ['roca', 'tierra'],
    'Dragonite': ['dragón', 'volador'],
    'Alakazam': ['psíquico'],
    'Machamp': ['lucha'],
    'Gardevoir': ['psíquico', 'hada'],
    'Tyranitar': ['roca', 'siniestro']
}

def elegir_pokemon(tipo_enemigo):
    # Buscamos qué tipos son fuertes contra el tipo enemigo
    tipos_efectivos = tipos_fuertes.get(tipo_enemigo, [])
    
    if not tipos_efectivos:
        print(f"No se encontraron contra-efectos para el tipo {tipo_enemigo}.")
        return
    
    print(f"Tipos fuertes contra {tipo_enemigo}: {', '.join(tipos_efectivos)}")
    
    # Verificamos qué Pokémon de nuestra lista tiene un tipo fuerte contra el enemigo
    candidatos = []
    
    for pokemon, tipos in pokemons.items():
        for tipo in tipos:
            if tipo in tipos_efectivos:
                candidatos.append(pokemon)
                break
    
    if candidatos:
        print(f"Recomendados para la batalla contra un Pokémon de tipo {tipo_enemigo}: {', '.join(candidatos)}")
    else:
        print(f"No se encontraron Pokémon con ventaja contra {tipo_enemigo}.")

# Solicitar al usuario el tipo del Pokémon enemigo
tipo_enemigo = input("Ingresa el tipo del Pokémon enemigo (por ejemplo, fuego, agua, planta): ").lower()
elegir_pokemon(tipo_enemigo)
