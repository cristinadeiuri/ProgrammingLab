#creare un oggetto CSVFile che rappresenti un file CSV e che: 1)venga inizializzato sul nome del file csv; 2)abbia un attributo "name" che ne contenga il nome; 3)abbia un metodo "get_data()" che torni i dati dal file CSV come lista di liste. Committare il file in cui è stato scritto.


#creo un oggetto
class CSVFile():

    def __init__(self, name):
        #setto il nome
        self.name = name

    def get_data(self):
        file = open('shampoo_sales.csv', 'r')
        strings = []
        for line in file:
            elements = line.split()
            strings.append(elements)
        print(strings)
            
                        
           
#dò il nome al file e lo stampo
file = CSVFile('shampoo_sales')
print(file)
print(file.name)
file.get_data()






