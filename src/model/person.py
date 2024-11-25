class Person:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name: str = first_name
        self.__last_name: str = last_name
        self.__id = 0

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def first_name(self) -> str:
        return self.__first_name
    
    @property
    def last_name(self) -> str:
        return self.__last_name
    
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @first_name.setter
    def name(self, first_name: str) -> None:
        self.__first_name = first_name

    @last_name.setter
    def name(self, last_name: str) -> None:
        self.__last_name = last_name

    def __dict__(self) -> dict:
        return {
            "id" : self.__id,
            "type": self.__class__.__name__,
            "first_name": self.__first_name,
            "last_name": self.__last_name
        }
    
    @staticmethod
    def from_dict(data: dict) -> "Person":
        person = Person(data["first_name"], data["last_name"])
        return person
    
    def __str__(self) -> str:
        return f"{self.species} - {self.first_name} {self.last_name}"
    


class Student(Person):
    def __init__(self, first_name: str, last_name: str, speciality: str, group: int):
        super().__init__(first_name, last_name)
        self.__speciality: str = speciality
        self.__group: int = group

    @property
    def speciality(self) -> str:
        return self.__speciality
    
    @property
    def group(self) -> int:
        return self.__group
    
    @speciality.setter
    def speciality(self, speciality: str) -> None:
        self.__speciality = speciality

    @group.setter
    def group(self, group: int) -> None:
        if not 1 <= group <= 18:
            raise ValueError(f"Недопустимый номер группы {group}")
        self.__group = group

    def __dict__(self) -> dict:
        data = super().__dict__()
        data["specific"] = self.speciality
        data["group"] = self.group
        return data
    

    @staticmethod
    def from_dict(data: dict) -> "Student":
        student = Student(data["first_name"], data["last_name"], data["specific"], data["group"])
        return student
    
    def __str__(self) -> str:
        return f"{super()}, {self.speciality} - ИДБ-23-{self.group}"
    

class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, department: str):
        super().__init__(first_name, last_name)
        self.__department: str = department

    @property
    def department(self) -> str:
        return self.__department
    
    @department.setter
    def department(self, department: str) -> None:
        self.__department = department

    def __dict__(self) -> dict:
        data = super().__dict__()
        data["specific"] = self.department
        return data
    
    def __str__(self) -> str:
        return f"{super()}, {self.department}"
    
    @staticmethod
    def from_dict(data: dict) -> "Teacher":
        teacher = Teacher(data["first_name"], data["last_name"], data["specific"])
        return teacher
    
