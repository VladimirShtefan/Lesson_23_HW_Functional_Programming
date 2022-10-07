from os.path import exists
from pathlib import Path
from typing import Generator


class DataFile:
    def __init__(self, file_dir: Path) -> None:
        self.__file_dir: Path = file_dir

    def read(self) -> Generator:
        with open(self.__file_dir, 'r', encoding='utf-8') as file:
            for line in file:
                yield line

    def check_file(self) -> bool:
        return exists(self.__file_dir)
