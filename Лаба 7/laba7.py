class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.id = kwargs['id']

    def get_info(self):
        print('ID: ' + str(self.id) + ", Имя: " + self.name)


class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.department = kwargs['department']

    def get_info(self):
        super().get_info()
        print("Департамент: " + self.department)

    def manage_project(self, project_name):
        print(self.name + ' менеджерирует проект ' + project_name + '.')


class Technician(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.specialization = kwargs['specialization']

    def get_info(self):
        super().get_info()
        print('Специализация: ' + self.specialization)

    def perform_maintenance(self):
        print(self.name + ' специализируется на ' + self.specialization + '.')


class TechManager(Manager, Technician):
    def __init__(self, **kwargs):
        Manager.__init__(self, **kwargs)
        Technician.__init__(self, **kwargs)
        self.team = []

    def add_employee(self, employee):
        self.team.append(employee)
        print(employee.name + ' был добавлен в команду.')

    def get_team_info(self):
        for employee in self.team:
            employee.get_info()


emp1 = Employee(name='СТАСЯН', id=1488)
manager = Manager(name='ВОВЧИК', id=1337, department='ШКИБИДИУНИТАЗИКИ')
technician = Technician(name='ЗУБЕНКО МИХАЙЛО ПЕТРОВЧИК', id=322, specialization='БРАВЛСТАРСОБНОВА')
tech_manager = TechManager(name='СПАСАТЕЛЬ МАЛИБУ', id=228, department='КОГО СПАСУ', specialization='ТОГО КХМКХМ')

emp1.get_info()
manager.get_info()
technician.get_info()
tech_manager.get_info()

manager.manage_project('СВО')
technician.perform_maintenance()

tech_manager.add_employee(emp1)
tech_manager.add_employee(manager)
tech_manager.add_employee(technician)

print('СПИСОК ТИМЫ:')
tech_manager.get_team_info()