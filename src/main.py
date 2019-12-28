import csv

class Parser:

    _file_path = ''

    def __init__(self, file_path):
        self._file_path = file_path

    def display_line(self, index):
        with open(self._file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            count = 0
            for row in reader:
                if count == index:
                    print(row)
                else:
                    pass
                count += 1

    # Le nombre d'accident dans chaque rue
    def get_number_accident_of_street(self, street_name):
        with open(self._file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            result = 0
            for row in reader:
                if row[7] == street_name:
                    result += 1
            return result

    # La fonction qui additionne le nombre d'accidents dans les rues
    def get_number_accidents_by_street(self):
        with open(self._file_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            result = dict()
            for row in reader:
                if row[7] not in result.keys():
                    result[row[7]] = 1
                else :
                    result[row[7]] += 1
        return result

    # La fonction qui donne le nombre d'accident par jour de la semaine
    # ex: {'LU': 30, 'MA': 80, ...}


    # La fonction qui donne le nombre d'accident impliquant au moins un velo


    # La fonction qui donne le nombre d'accident impliquant au moins un velo ET un vehicule motorise
    # Il faut au moins 1 motorise (moto, camion leger, camion lourd, VHR, etc..) et au moins 1 velo


parser = Parser('assets/accidents_2012_2018.csv')
list = parser.get_number_accidents_by_street()
print(list)