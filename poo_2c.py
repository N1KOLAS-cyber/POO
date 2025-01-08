class personaje:
    #Atributos de la clase 
    Nombre = 'default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    #indicar que no se hara nada por el momento 
    pass

mi_personaje = personaje() 
#modificando valores de los atributos
mi_personaje.Nombreombre = "EstebanDido"
mi_personaje.fuerza = 300
mi_personaje.inteligencia = 300
mi_personaje.defensa = 30
mi_personaje.vida =  2

print("El nombre de mi personaje es: ", mi_personaje.defensa )
print("El nombre de mi personaje es: ", mi_personaje.fuerza )
print("El nombre de mi personaje es: ", mi_personaje.inteligencia )
print("El nombre de mi personaje es: ", mi_personaje.vida )
