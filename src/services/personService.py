from model.person import Person
from utils.constants import PERSON_FROM_DICT
from exceptions.exceptions import InvalidPersonTypeException, PersonNotFoundException
from storage.storage import Storage

class PersonService:
    def __init__(self, storage: Storage):
        self.__storage = storage
        self.__persons: list = []
        
    def create(self, person_data: dict) -> None:
        person_type = person_data['type']
        if person_type not in PERSON_FROM_DICT.keys():
            raise InvalidPersonTypeException
        
        person = PERSON_FROM_DICT[person_type](person_data)
        person.id = self.__storage.set_current_id()
        print(f"in service {person.id}")
        self.__persons = self.__storage.load_from_file()
        self.__persons.append(person)
        self.__storage.save_to_file(self.__persons)
        print(f"{person_type} успешно создан")

    def update(self, person_id: int, person_data: dict) -> None:
        self.__persons = self.__storage.load_from_file()
        
        person_type = person_data['type']
        for i in range (0, len(self.__persons)):
            if self.__persons[i].id == person_id:
                for key, value in person_data.items():
                    self.__persons[i][key] = value

                self.__storage.save_to_file(self.__persons)
                print(f"{person_type} успешно обновлён")
                return
            
        raise PersonNotFoundException
    
    def delete(self, person_id: int) -> None:
        self.__persons = self.__storage.load_from_file()

        for person in self.__persons:
            if person.id == person_id:
                self.__persons.remove(person)
                return
            
        raise PersonNotFoundException
    
    def read(self) -> None:
        
        self.__persons = self.__storage.load_from_file()
        
        if not self.__persons:
            print("База пуста")
            return
        else:
            
            for person in self.__persons:
                print(person.__str__())

