import os

from storage.serializer.serializer import Serializer
from utils.constants import PERSON_MAP
from utils.constants import PERSON_FROM_DICT

class Storage:
    def __init__(self, serializer: Serializer, file_path: str) -> None:
        self.__serializer: Serializer = serializer
        self.__db_path: str = f'{file_path}/db.{serializer.get_type()}'
        self.__current_id: int = 0
        if not os.path.exists(self.__db_path):
            return
        with open(self.__db_path, 'r', encoding='utf-8') as file:
            serialized_data = file.read()
        data = self.__serializer.from_format(serialized_data)
        self.__current_id = int(data[len(data) - 1]["id"])


    # @property
    # def current_id(self) -> int:
    #     return self.__current_id
    
    # def get_current_id(self) -> int:
    #     return self.__current_id

    def set_current_id(self) -> int:
        id = self.__current_id
        self.__current_id += 1
        return id

    def save_to_file(self, data: list) -> None:
        try:
            if not os.path.exists(self.__db_path):
                self._create_file()
            with open(self.__db_path, 'w', encoding='utf-8') as file:
                file.write(self.__serializer.to_format(data))
                print(f"Данные сохранены в файл: {self.__db_path}")
        except Exception as error:
            print(f"Ошибка при сохранении данных: {error}")

    def load_from_file(self) -> list:
        try:
            if not os.path.exists(self.__db_path):
                self._create_file()
            with open(self.__db_path, 'r', encoding='utf-8') as file:
                serialized_data = file.read()
        except Exception as error:
            print(f"Ошибка при загрузке данных: {error}")
            return {[]}
        
        data = self.__serializer.from_format(serialized_data)
        persons = []
        for person in data:
            person_type = person["type"]
            if person_type not in PERSON_MAP.keys():
                raise TypeError(f"No such person type: {person_type}")
            if person['specific'] not in PERSON_MAP[person['type']].keys():
                raise TypeError(f"No such specific type: {person['specific']}")
            
            persons.append(PERSON_FROM_DICT[person_type](person))

        print(f"Данные успешно загружены из файла: {self.__db_path}")
        return persons
            

    def _create_file(self) -> None:
        print(f"Создание нового файла: {self.__db_path}")
        initial_data: dict = {"persons": []}
        with open(self.__db_path, 'w', encoding='utf-8') as file:
            file.write(self.__serializer.to_format(initial_data))