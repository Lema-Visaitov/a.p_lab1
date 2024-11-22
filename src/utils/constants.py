from enum import Enum

JSON_DB_PATH = '../db/json/db.json'
XML_DB_PATH = '../db/xml/db.xml'

class PersonEnum(Enum):
    TEACHER = "Преподаватель"
    STUDENT = "Студент"

    @staticmethod
    def is_valid_type(value: str) -> bool:
        return value in [person_type.value for person_type in PersonEnum]
    
class SpecialityEnum(Enum):
    APPLIED_INFORMATICS = "Прикладная информатика"
    SOFTWARE_ENGINEERING = "Программная инжерия"
    CS_AND_CT = "Информатика и вычислительная техника"
    
    def is_valid_type(value: str) -> bool:
        return value in [speciality_type.value for speciality_type in SpecialityEnum]
    
class DepartmentEnum(Enum):
    UITS = "Кафедра УИТС"
    IT_AND_CT = "Кафедра информационных технологий и вычислительных систем"

    @staticmethod
    def is_valid_type(value: str) -> bool:
        return value in [department.value for department in DepartmentEnum]