
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

    def set_inwork(self, executor: str):
        self.current_status = 1
        self.executor = executor
        if self.ritm.current_status == 0:
            self.ritm.current_status = 1

    def get_current_status(self) -> str:
        return self.route_map[self.current_status]


class Ritm():
    route_map = {0: 'Создан', 1: "В работе", 2: "Выполнено", 3: "Закрыт", 4: 'Отменено'}
    transitions = {0: [1, 4], 1: [2, 3, 4], 2: [1, 3]}
    number_counter = 0

    def __init__(self, description: str):
        self.number = self.__class__.number_counter
        self.__class__.number_counter += 1
        self.current_status = 0
        self.current_task = Task(self)
        self.tasks = [self.current_task, ]

    def get_current_status(self) -> str:
        return self.route_map[self.current_status]


ritm1 = Ritm('Не могу войти в систему MGP')
ritm2 = Ritm('Не могу войти в систему MEP')

def print_all():
    print('-'*100)
    print('Текущий статус ritm1: ', ritm1.get_current_status())
    print('Текущий номер задачи ritm1: ', ritm1.current_task.number)
    print('Текущий статус задачи ritm1: ', ritm1.current_task.get_current_status())
    print('Текущий обработчик задачи ritm1: ', ritm1.current_task.executor)


print('Текущий ritm1: ', ritm1.number)
print('Текущий ritm2: ', ritm2.number)
print_all()
ritm1.current_task.set_inwork('Козлов АА')
print_all()