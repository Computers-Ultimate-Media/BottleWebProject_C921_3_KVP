# Данный класс описывает объект файла логов
class AlgorithmHistory:
    name: str
    date: str
    input: any
    output: any

    def __init__(self, name: str, date: str, input: any, output: any):
        self.name = name
        self.date = date
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
