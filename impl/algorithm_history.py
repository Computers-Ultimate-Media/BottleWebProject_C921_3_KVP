from os import getcwd
from datetime import datetime
from impl.config import Config


# This class describes the log file object
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

    # method that translates a class into a dictionary
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
