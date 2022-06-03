from os.path import exists as file_exists, join as path_join
from json import dumps as json_dumps, load as json_loads


# Класс для работы файлами json в виде массива
class Config:
    filename: str
    data: list = {}

    def __init__(self, working_directory: str, file: str):
        filename = path_join(working_directory, file)
        if not file_exists(filename):
            open(filename, "w+").write(json_dumps([]))

        self.filename = filename
        self.data = json_loads(open(filename, "r+"))

    def save(self):
        open(self.filename, "w+").write(json_dumps(self.data, indent=4))
