#estendere l'oggetto CSVFile chiamandolo NumericalCSVFile e facendo in modo che converta automaticamente a numero tutte le colonne tranne la prima (della data).
#successivamente aggiungere due campi al file
#gestire gli errori che verranno generati in modo che le linee vengano saltate senza bloccare il programma ma che venga stampato a schermo l'errore

#definisco la classe padre
class CSVFile():

    def __init__(self, name):
        self.name = name
        
        self.can_read = True
        try:
            file = open(self.name, 'r')
            file.readline()
        except Exception as e:
            self.can_read = False
            print('Non posso leggere il file! Errore: "{}".'.format(e))        
            

    def get_data(self):

        if not self.can_read:
            return None

        else:
            data = []
            file = open(self.name, 'r')
            for line in file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                data.append(elements)
            
            file.close()
            return data

    def add(self):
        file = open(self.name, 'r+')
        file.write('01-01-2015')
        file.write('01-01-2015, ciao')
        file.close()


file = CSVFile('shampoo_sales.csv')
print(file)
print('Il nome del file è: "{}".'.format(file.name))
print('Il contenuto del file è {}'.format(file.get_data()))
print('Ho aggiunto: "{}" al file "{}".'.format(file.add(), file.name))


#estendo la classe
class NumericalCSVFile(CSVFile):

    def get_data(self):
        #chiamo la get_data della classe padre
        string_data = super().get_data()

        #creo una lista per salvare i valori numerici
        numerical_data = []

        for string_row in string_data:
            numerical_row = []
            for i, element in enumerate(string_row):
                if i == 0:
                    numerical_row.append(element)

                else:
                    try:
                        numerical_row.append(float(element))

                    except Exception as e:
                        print('Errore di conversione del valore "{}" a numerico: "{}".'.format(element,e))
                        
                    
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)

        return numerical_data
     

numerical_file = NumericalCSVFile('shampoo_sales.csv')
print(numerical_file)
print('I valori numerici del file sono: {}'.format(numerical_file.get_data()))



