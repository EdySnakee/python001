
persona = {
    'nombre': 'snake',
    'edad': 333,
    'gustos': ['rojo','negro'],
    'dato': 'curioso'
}

print(persona)

# ACTUALIZANDO UNA LLAVE
persona['nombre'] = 'whisper'

# MODIFICAMOS LA EDAD Y RESTAMOS
persona['edad'] -= 300

#AGREGAMOS A LA LLAVE
persona['gustos'].append('morado')

print('actualizada->>',persona)

#ELIMINAMOS UN DATO
# del persona['nombre']
# persona.pop('edad')
print('eliminado->>',persona)

#OBTENEMOS LOS ITEMS DEL DICCIONARIO
print('Items->', persona.items())

#OBTENEMOS keys DEL DICCIONARIO
print('Keys->', persona.keys())

#OBTENEMOS LOS values DEL DICCIONARIO
print('Values->', persona.values())