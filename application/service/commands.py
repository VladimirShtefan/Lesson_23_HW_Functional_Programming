from collections.abc import Generator

from flask import abort


class RunCommands:
    def __init__(self, data_file: Generator, **kwargs):
        self.__data_file = data_file
        self.__filter = kwargs.get('filter', None)
        self.__map = kwargs.get('map', None)
        self.__unique = kwargs.get('unique', None)
        self.__sort = kwargs.get('sort', None)
        self.__limit = kwargs.get('limit', None)
        self.__get_filter_data()
        self.__get_map_data()
        self.__get_unique_data()
        self.__get_sort_data()
        self.__get_limit_data()

    def __get_filter_data(self) -> None:
        if self.__filter:
            if not isinstance(self.__filter, str):
                abort(400, 'В команде filter должен быть передан текст для фильтрации')
            self.__data_file = filter(lambda line: self.__filter in line, self.__data_file)

    def __get_map_data(self) -> None:
        if self.__map:
            try:
                self.__map = int(self.__map)
            except ValueError:
                abort(400, 'В команде map должен быть передан номер столбца')
            self.__data_file = map(lambda data: data.split()[self.__map], self.__data_file)

    def __get_unique_data(self) -> None:
        if self.__unique is not None:
            if self.__unique == '':
                self.__data_file = set(self.__data_file)
                return
            abort(400, 'В команде unique должна быть передана пустая строка ""')

    def __get_sort_data(self) -> None:
        if self.__sort:
            if not isinstance(self.__sort, str) or self.__sort.lower() not in ('asc', 'desc'):
                abort(400, 'В команде sort должен быть передан текст asc или desc')
            if self.__sort.lower() == 'asc':
                self.__data_file = sorted(self.__data_file, reverse=False)
            else:
                self.__data_file = sorted(self.__data_file, reverse=True)

    def __get_limit_data(self) -> None:
        if self.__limit:
            try:
                self.__limit = int(self.__limit)
            except ValueError:
                abort(400, 'В команде limit должно быть передано необходимое количество записей (числом)')
            self.__data_file = list(self.__data_file)[:self.__limit]

    def run(self) -> Generator | set | list:
        return self.__data_file
