from os import getcwd
from datetime import datetime
from impl.config import Config


# Данный класс описывает объект файла логов
class AlgorithmHistory:
    name: str
    date: str
    input: any
    output: any

    def __init__(self, name: str, input: any, output: any):
        self.name = name
        self.date = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.input = input
        self.output = output

    # метод, который переводит класс в словарь
    def to_dict(self):
        return {
            'name': self.name,
            'date': self.date,
            'input': self.input,
            'output': self.output,
        }

    def save(self):
        config = Config(getcwd(), 'history.json')
        config.data.append(self.to_dict())
        config.save()
