#importo il modulo per i numeri randomici
import random

class Persona():

    def __init__(self, nome, cognome):

        self.nome = nome
        self.cognome = cognome

    def __str__(self):
        return 'Persona "{} {}"'.format(self.nome, self.cognome)

    def di_ciao(self):
        #genero un numero random tra 0, 1 e 2
        numero_random = random.randint(0,2)

        #scelgo un saluto random
        if numero_random == 0:
            print('Ciao, sono {} {}.'.format(self.nome, self.cognome))
        elif numero_random == 1:
            print('Ciao, mi chiamo {}.'.format(self.nome))
        elif numero_random == 2:
            print('Eilà! {} è qui!'.format(self.nome))

persona = Persona('Mario', 'Rossi')
print(persona)
persona.di_ciao()

#estendo gli oggetti

class Studente(Persona):

    def __str__(self):
        return 'Studente "{} {}"'.format(self.nome, self.cognome)

class Professore(Persona):

    def __str__(self):
        return 'Prof. "{} {}"'.format(self.nome, self.cognome)

    def di_ciao(self):
        print('Buongiorno, sono il professor {} {}.'.format(self.nome, self.cognome))       

    def di_ciao_originale(self):
        super().di_ciao()#con il super cancello le sovrascrizioni inserite per questa sottoclasse

persona = Professore('Stefano', 'Laurenti')
print(persona)
persona.di_ciao()                 

prof = Professore('Pippo', 'Baudo')
print(prof)
prof.di_ciao()
prof.di_ciao_originale()