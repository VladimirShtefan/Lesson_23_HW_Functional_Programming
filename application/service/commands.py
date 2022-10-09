import re
from collections.abc import Generator
from typing import Union

from application.exeptions import BaseAppException


class RunCommands:
    def __init__(self, data_file: Generator) -> None:
        self.__data_file: Union[Generator, set, list] = data_file
        self.__mapping = {
            'filter': self.__filter,
            'map': self.__map,
            'unique': self.__unique,
            'sort': self.__sort,
            'limit': self.__limit,
            'regex': self.__regex
        }

    @staticmethod
    def __get_item_after_split(data: str, item: int) -> str:
        try:
            return data.split()[item]
        except IndexError:
            raise BaseAppException('В функции map выбран не существующий столбец')

    def __filter(self, data_for_filter: str) -> None:
        if not isinstance(data_for_filter, str):
            raise BaseAppException('В команде filter должен быть передан текст для фильтрации')
        self.__data_file = list(filter(lambda line: data_for_filter in line, self.__data_file))

    def __map(self, data_for_map: str) -> None:
        try:
            column: int = int(data_for_map)
        except ValueError:
            raise BaseAppException('В команде map должен быть передан номер столбца')
        self.__data_file = list(map(lambda data: self.__get_item_after_split(data, column), self.__data_file))

    def __unique(self, data_for_unique: str) -> None:
        if data_for_unique == '':
            self.__data_file = set(self.__data_file)
            return
        raise BaseAppException('В команде unique должна быть передана пустая строка ""')

    def __sort(self, data_for_sort: str) -> None:
        if not isinstance(data_for_sort, str) or data_for_sort.lower() not in ('asc', 'desc'):
            raise BaseAppException('В команде sort должен быть передан текст asc или desc')
        if data_for_sort.lower() == 'asc':
            self.__data_file = sorted(self.__data_file, reverse=False)
        else:
            self.__data_file = sorted(self.__data_file, reverse=True)

    def __limit(self, data_for_limit: str) -> None:
        try:
            number_of_entries: int = int(data_for_limit)
        except ValueError:
            raise BaseAppException('В команде limit должно быть передано необходимое количество записей (числом)')
        self.__data_file = list(self.__data_file)[:number_of_entries]

    def __regex(self, regular_string: str) -> None:
        self.__data_file = list(filter(lambda data: re.search(regular_string, data), self.__data_file))

    def run_mapping(self, command: str, data: str) -> Generator | set | list | None:
        return self.__mapping[command](data)

    def get_result(self) -> Generator | set | list:
        return self.__data_file
