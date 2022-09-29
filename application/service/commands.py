from collections.abc import Generator

from application.exeptions import BaseAppException


class RunCommands:
    def __init__(self, data_file: Generator):
        self.__data_file = data_file

    def filter(self, data_for_filter: str) -> None:
        if not isinstance(data_for_filter, str):
            raise BaseAppException('В команде filter должен быть передан текст для фильтрации')
        self.__data_file = filter(lambda line: data_for_filter in line, self.__data_file)

    def map(self, data_for_map: str) -> None:
        try:
            data_for_map = int(data_for_map)
        except ValueError:
            raise BaseAppException('В команде map должен быть передан номер столбца')
        self.__data_file = map(lambda data: data.split()[data_for_map], self.__data_file)

    def unique(self, data_for_unique: str) -> None:
        if data_for_unique == '':
            self.__data_file = set(self.__data_file)
            return
        raise BaseAppException('В команде unique должна быть передана пустая строка ""')

    def sort(self, data_for_sort: str) -> None:
        if not isinstance(data_for_sort, str) or data_for_sort.lower() not in ('asc', 'desc'):
            raise BaseAppException('В команде sort должен быть передан текст asc или desc')
        if data_for_sort.lower() == 'asc':
            self.__data_file = sorted(self.__data_file, reverse=False)
        else:
            self.__data_file = sorted(self.__data_file, reverse=True)

    def limit(self, data_for_limit: str) -> None:
        try:
            data_for_limit = int(data_for_limit)
        except ValueError:
            raise BaseAppException('В команде limit должно быть передано необходимое количество записей (числом)')
        self.__data_file = list(self.__data_file)[:data_for_limit]

    def run(self) -> Generator | set | list:
        return self.__data_file
