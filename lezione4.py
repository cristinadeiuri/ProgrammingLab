class Persona():
    
    def __init__(self, nome, cognome):
        #setto nome e cognome
        self.nome = nome
        self.cognome = cognome

persona = Persona('Mario', 'Rossi')
print(persona)
print(persona.nome)
print(persona.cognome)

#altro modo, usando __str__ affinchè mi ritorni una stringa specifica
class Persona():
    
    def __init__(self, nome, cognome):
        #setto nome e cognome
        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return 'Persona "{} {}"'.format(self.nome, self.cognome)    

persona = Persona('Mario', 'Rossi')
print(persona)


