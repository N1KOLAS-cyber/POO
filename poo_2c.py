class Personaje:
    # Constructor de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):  # Corregido a __init__
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza:", self.fuerza)
        print("-Inteligencia:", self.inteligencia)
        print("-Defensa:", self.defensa)
        print("-Vida:", self.vida)
    
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
    
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "Ha muerto")
        return self.vida <= 0
    
    def dmg(self, enemigo):
        # Si la defensa del enemigo es mayor o igual que la fuerza del atacante, el daño es 0
        return max(0, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        daño = self.dmg(enemigo)
        # Asegurarse de que la vida no baje de cero
        enemigo.vida = max(0, enemigo.vida - daño)
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
        
class Guerrero(Personaje):
    
    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
        
    # Sobreescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-Espada:", self.espada)

    # Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa 
    
    # Escoger navaja
    def escoger_navaja(self):
        opcion = int(input("Escoge sabiamente:\n(1) Navaja suiza, daño 10.\n(2) Navaja pioja, daño 4.\n>>>>>> "))
        if opcion == 1:
            self.espada = 10  
        elif opcion == 2:
            self.espada = 6
        else:
            print("Valor inválido, intente nuevamente.")
            # Vuelve a ejecutar el método escoger navaja
            self.escoger_navaja()

#################################################################
class Mago(Personaje):
    
    # Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = libro
        
    # Sobreescribir impresión de atributos
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("-libro:", self.libro)

    # Sobreescribir el cálculo del daño
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa 
    
    # Escoger libro
    def escoger_libro(self):
        opcion = int(input("Escoge el libro de la sabiduria:\n(1) El principito, daño 10.\n(2) crepúculo, daño 6.\n>>>>>> "))
        if opcion == 1:
            self.libro = 10  
        elif opcion == 2:
            self.libro = 6
        else:
            print("Valor inválido, intente nuevamente.")
            # Vuelve a ejecutar el método escoger navaja
            self.escoger_libro()

# Crear objeto Guerrero
#arturoSuarez = Guerrero("Arturo Suárez", 12, 3000, 2, 100, 0.5)
#arturoSuarez.escoger_navaja()
#arturoSuarez.imprimir_atributos(
# creando todos los objetos 
persona = Personaje("Angel Suarez", 20, 15, 10, 100)
arturosuarez = Guerrero("Arturo suarez ", 20, 15, 10,100,5)
gandalf = Mago ("Gandalf", 20, 15,10,100,5)
#atributos antes de la tragedia 
persona.imprimir_atributos()
arturosuarez.imprimir_atributos()
gandalf.imprimir_atributos()
#Ataques sin piedad 
persona.atacar(arturosuarez)
arturosuarez.atacar(gandalf)
gandalf.atacar(gandalf)
gandalf.atacar(persona)
#atributos despues de la tragedia
persona.imprimir_atributo()
arturosuarez.imprimir_atributos()
gandalf.imprimir_atributos()
