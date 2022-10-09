from application.exeptions import BaseAppException


class RequestParser:
    def __init__(self, request: dict):
        self.__request = request
        self.__file_name: str = ''
        self.__query: dict = {}
        self.__parse_data()

    @property
    def file_name(self) -> str:
        return self.__file_name

    @property
    def query(self) -> dict:
        return self.__query

    def __parse_data(self) -> None:
        data = dict(self.__request)
        try:
            self.__file_name = data.pop('file_name')
        except KeyError:
            raise BaseAppException('Не указан путь к файлу в аргументах запроса file_name')
        if len(data) % 2 != 0:
            raise BaseAppException('Не верно заданы аргументы для обработки')
        self.__query = self.__validate_query(data)

    @staticmethod
    def __validate_query(query: dict) -> dict:
        _cmd = {}
        _values = {}
        query = dict(sorted(query.items(), key=lambda item: item[0]))
        for key, value in query.items():
            if key.startswith('cmd') and value in ('filter', 'map', 'unique', 'sort', 'limit', 'regex'):
                _cmd[key.lstrip('cmd')] = value
            elif key.startswith('value'):
                _values[key.lstrip('value')] = value
        if len(_cmd) != len(_values):
            raise BaseAppException('Не верно заданы аргументы для обработки')
        try:
            return {_cmd[key]: _values[key] for key, value in _cmd.items()}
        except KeyError:
            raise BaseAppException('Не верно заданы аргументы для обработки')
