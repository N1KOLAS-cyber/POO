class personaje:
    #Atributos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    #¿Qué es self (En Python)? Es una referencia al mismo objeto
    #¿Qué es el metodo init (En python)? Constructor que inicializa atributos de un objeto
    #¿Porque se usa doble __ (En python)? Dunder. Porque es metodo magico 
    #¿Cuando  se ejecuta el metodo init? Autom. al crear una nueva 
    
    #Una nueva instancia
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza", self.fuerza)
        print("-Inteligencia", self.inteligencia)
        print("-Defensa", self.defensa)
        print("-Vida", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
    
    def esta_vivo(self):
        return self.vida > 0
        print (self.nombre, "ha muerto")
        
    def dañar(self,enemigo):
        return self.fuerza - self.defensa
    
    def atacar (self,enemigo):
        daño = self.dañar (enemigo)
        enemigo.vida = enemigo.vida - daño 
        print( self.nombre, "ha realizado",daño,"puntos de de daño a",enemigo.nombre)
        print("vida de", enemigo.nombre, "es", enemigo.vida)

#Variable del constructor vacío
mi_personaje = personaje("EsteBandido", 100, 50, 45, 100 )
mi_enemigo = personaje("angel",70,100,40,100)
mi_personaje.atacar(mi_enemigo)
mi_personaje.imprimir_atributos()
mi_personaje.subir_nivel(15,5,10)

# print("Valores actaulizados")
# mi_personaje.imprimir_atributos()
