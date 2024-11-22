from utils.constants import PersonEnum
from utils.constants import SpecialityEnum
from utils.constants import DepartmentEnum

class Person:
    def __init__(self, species: str, first_name: str, last_name: str):
        if not PersonEnum.is_valid_type(species):
            raise ValueError(f"Недопустимый тип человека {species}")
        self.__person_id: int = 0
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__species: str = species

    @property
    def person_id(self) -> str:
        return self.__person_id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    @property
    def species(self) -> str:
        return self.__species
    

    @person_id.setter
    def person_id(self, id: int) -> None:
        self.__person_id = id
    
    @first_name.setter
    def name(self, first_name: str) -> None:
        self.__first_name = first_name

    @last_name.setter
    def name(self, last_name: str) -> None:
        self.__last_name = last_name

    @species.setter
    def species(self, species: PersonEnum) -> None:
        self.__species = species

    def to_dict(self) -> dict:
        return {
            "species": self.__species,
            "person_id": self.__person_id,
            "first_name": self.__first_name,
            "last_name": self.__last_name
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Person":
        person = Person(data["species"], data["first_name"], data["last_name"])
        person.person_id = data["person_id"]
        return person
    
    def __str__(self) -> str:
        return f"{self.species} - {self.first_name} {self.last_name}"
    


class Student(Person):
    def __init__(self, first_name: str, last_name: str, speciality: str, group: int):
        if not SpecialityEnum.is_valid_type(speciality):
            raise ValueError(f"Недопустимый тип направления {speciality}")
        if not 1 <= group <= 18:
            raise ValueError(f"Недопустимый номер группы {group}")
        super().__init__(PersonEnum.STUDENT.value, first_name, last_name)
        self.__speciality = speciality
        self.__group = group

    @property
    def speciality(self) -> str:
        return self.__speciality
    
    @property
    def group(self) -> int:
        return self.__group
    
    @speciality.setter
    def speciality(self, speciality: str) -> None:
        if not SpecialityEnum.is_valid_type(speciality):
            raise ValueError(f"Недопустимый тип направления {speciality}")
        self.__speciality = speciality

    @group.setter
    def group(self, group: int) -> None:
        if not 1 <= group <= 18:
            raise ValueError(f"Недопустимый номер группы {group}")
        self.__group = group

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["speciality"] = self.speciality
        data["group"] = self.group
        return data
    

    @staticmethod
    def from_dict(data: dict) -> "Student":
        student = Student(data["first_name"], data["last_name"], data["specialuty"], data["group"])
        student.person_id = data["person_id"]
        return student
    
    def __str__(self) -> str:
        return f"{super()}, {self.speciality} - ИДБ-23-{self.group}"
    

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, department: str):
        if not DepartmentEnum.is_valid_type(department):
            raise ValueError(f"Такой кафедры нет: {department}")
        
        super().__init__(PersonEnum.TEACHER, first_name, last_name)
        self.__department = department

    @property
    def department(self) -> str:
        return self.__department
    
    @department.setter
    def department(self, department: str) -> None:
        if not DepartmentEnum.is_valid_type(department):
            raise ValueError(f"Такой кафедры нет: {department}")
        self.__department = department

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["department"] = self.department
        return data
    
    @staticmethod
    def from_dict(data: dict) -> "Student":
        student = Student(data["first_name"], data["last_name"], data["department"])
        student.person_id = data["person_id"]
        return student
    
    def __str__(self) -> str:
        return f"{super()}, {self.department}"
