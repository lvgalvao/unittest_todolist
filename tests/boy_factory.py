from factory import Factory, Faker
from fakes import TaskProvider
from serial import Task


Faker.add_provider(TaskProvider)


class TaskFactory(Factory):
    class Meta:
        model = Task

    task_name = Faker('task_name')
    state = Faker('state')