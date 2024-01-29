
class Task():
    route_map = {0: 'Назначен', 1: "В работе", 2: "Выполнено"}
    transitions = {0: [1], 1: [2]}
    number_counter = 1000

    def __init__(self, ritm):
        self.number = self.__class__.number_counter
        self.__class__.number_counter += 1
        self.ritm = ritm
        self.current_status = 0
        self.executor = ''

    def set_status(self, target_status):
        if target_status in self.transitions[self.current_status]:
            self.current_status = target_status
        else:
            print('!!!Данного перехода статусов нет в маршрутной карте!!!')

    def set_inwork(self, executor: str):
        self.set_status(1)
        self.executor = executor
        if self.ritm.current_status == 0:
            self.ritm.current_status = 1

    def complete_with_new(self):
        self.set_status(2)
        self.ritm.create_task()

    def complete(self):
        self.set_status(2)
        self.ritm.done()

    def get_current_status(self) -> str:
        return self.route_map[self.current_status]
        self.current_task = Task(self)


class Ritm():
    route_map = {0: 'Создан', 1: "В работе", 2: "Выполнено", 3: "Закрыт", 4: 'Отменено'}
    transitions = {0: [1, 4], 1: [2, 3, 4], 2: [1, 3]}
    number_counter = 0

    def __init__(self, description: str):
        self.number = self.__class__.number_counter
        self.__class__.number_counter += 1
        self.current_status = 0
        self.tasks = []
        self.create_task()

    def set_status(self, target_status):
        if target_status in self.transitions[self.current_status]:
            self.current_status = target_status
        else:
            print('!!!Данного перехода статусов нет в маршрутной карте!!!')

    def done(self):
        self.set_status(2)

    def create_task(self):
        self.current_task = Task(self)
        self.tasks.append(self.current_task)

    def get_tasks(self):
        result_str = ''
        for task in self.tasks:
            result_str += f'{task.number} - {task.current_status} - {task.executor}\n'
        return result_str

    def get_current_status(self) -> str:
        return self.route_map[self.current_status]

    def test_class_method(self='вызов из класса'):
        print(self)


ritm1 = Ritm('Не могу войти в систему MGP')
ritm2 = Ritm('Не могу войти в систему MEP')

def print_all():
    print('-'*100)
    print('Текущий статус ritm1: ', ritm1.get_current_status())
    print(ritm1.get_tasks())


print('Текущий ritm1: ', ritm1.number)
print('Текущий ritm2: ', ritm2.number)
print_all()
ritm1.current_task.set_inwork('Козлов АА')
print_all()
ritm1.current_task.complete_with_new()
print_all()
ritm1.current_task.set_inwork('Кошелева ЕВ')
print_all()
ritm1.current_task.complete()
print_all()
print('-'*100)
print('-'*100)
Ritm.test_class_method()
ritm1.test_class_method()