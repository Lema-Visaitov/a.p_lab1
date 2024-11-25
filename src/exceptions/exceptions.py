class InvalidPersonTypeException(Exception):
    def __init__(self, person_type):
        super().__init__(f"Неверный тип человека: {person_type}. Допустимые типы: Студент и Преподаватель")

class PersonNotFoundException(Exception):
    def __init__(self, person_type):
        super().__init__(f"Такого преподавателя или студента не существует")