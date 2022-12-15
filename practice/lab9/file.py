from pathlib import Path


class FileInfo:
    def __init__(self, file_path):
        self._path = file_path
        self._name = Path(file_path).name

        with open(file_path, 'r') as file:
            self._number_of_lines = len(file.readlines())

    @property
    def path(self):
        return self._path

    @property
    def name(self):
        return self._name

    @property
    def number_of_lines(self):
        return self._number_of_lines

    def new_file(self, path):
        self.__init__(path)
