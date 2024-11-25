import os

from storage.serializer.serializer import Serializer
from utils.constants import PERSON_MAP
from utils.constants import PERSON_FROM_DICT

class Storage:
    def __init__(self, serializer: Serializer, file_path: str) -> None:
        self.__serializer: Serializer = serializer
        self.__db_path: str = file_path
        self.__current_id: int = 0

    @property
    def current_id(self) -> int:
        return self.__current_id
    
    def get_current_id(self) -> int:
        return self.__current_id

    def set_current_id(self) -> int:
        id = self.__current_id
        self.__current_id += 1
        return id

    def save_to_file(self, data: dict) -> None:
        try:
            if not os.path.exists(self.db_path):
                self._create_file(self.db_path)
            with open(self.db_path, 'w', encoding='utf-8') as file:
                file.write(self.__serializer.to_format(data))
                print(f"Данные сохранены в файл: {self.db_path}")
        except Exception as error:
            print(f"Ошибка при сохранении данных: {error}")

    def load_from_file(self) -> list:
        try:
            if not os.path.exists(self.db_path):
                self._create_file()
            with open(self.db_path, 'r', encoding='utf-8') as file:
                data = self.__serializer.from_format(file.read())
        except Exception as error:
            print(f"Ошибка при загрузке данных: {error}")
            return {"persons": []}
        
        persons = []
        for person in data:
            person_type = person["type"]
            if person_type not in PERSON_MAP:
                raise TypeError("No such type: {person_type}")
            if person['specific'] not in PERSON_MAP[person['type']]:
                person_specific: str = person_type
                raise TypeError("No such type: {person_specific}")
            
            persons.append(PERSON_FROM_DICT[person_type](person))

        print(f"Данные успешно загружены из файла: {self.__db_path}")
        return persons
            

    def _create_file(self) -> None:
        print(f"Создание нового файла: {self.db_path}")
        initial_data: dict = {"persons": []}
        with open(self.db_path, 'w', encoding='utf-8') as file:
            file.write(self.__serializer.to_format(initial_data))