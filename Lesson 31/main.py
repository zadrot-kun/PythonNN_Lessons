
data_dict = {
    2022: {
        'Информатика': {
            'Иванов': [2, 3, 3],
            'Петров': [4]
        },
        'Физкультура': {
            'Иванов': [5],
            'Петров': [2, 4],
        }
    },
    2023: {
        'Информатика': {
            'Иванов': [2, 3],
            'Петров': [5],
        },
        'Физкультура': {
            'Иванов': [4],
            'Петров': [3, 5],
        }
    }
}

print(data_dict[2022]['Физкультура']['Петров'][1])
print('-'*100)
class Student():

    def __init__(self, name, *args):
        self.name = name
        self.scores = args

    def get_last_score(self):
        return self.scores[-1]

class Subject():

    def __init__(self, name):
        self.name = name
        self.students = {}


class Year():

    def __init__(self, name):
        self.name = name
        self.subjects = {}

petrov = Student('Петров', 2, 4)
fizra = Subject('Физкультура')
fizra.students[petrov.name] = petrov
year_2022 = Year(2022)
year_2022.subjects[fizra.name] = fizra

print(year_2022.subjects['Физкультура'].students['Петров'].get_last_score())