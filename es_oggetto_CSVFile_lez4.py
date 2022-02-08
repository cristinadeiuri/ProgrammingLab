#creare un oggetto CSVFile che rappresenti un file CSV e che: 1)venga inizializzato sul nome del file csv; 2)abbia un attributo "name" che ne contenga il nome; 3)abbia un metodo "get_data()" che torni i dati dal file CSV come lista di liste. Committare il file in cui è stato scritto.


#creo un oggetto
class CSVFile():

    def __init__(self, name):
        #setto il nome
        self.name = name

    #opzionale:
    def __str__(self):
        return 'Il nome del file è {}'.format(self.name)

    def get_data(self):
        file = open(self.name, 'r')
        data = []
        for line in file:
            elements = line.split()
            data.append(elements)
        file.close()
        return data
                       
#dò il nome al file e lo stampo
file = CSVFile(name = 'shampoo_sales.csv')
print(file)
print('Il nome del file è: "{}".'.format(file.name))
print('Dati contenuti nel mio file: "{}”.'.format(file.get_data()))






