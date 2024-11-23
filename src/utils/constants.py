from model.person import Person, Teacher, Student

JSON_DB_PATH = '../db/json/db.json'
XML_DB_PATH = '../db/xml/db.xml'

PERSON_MAP = {
    "Преподаватель" : {
        "Кафедра УИТС" : lambda first_name, last_name: Teacher(first_name, last_name, "Кафедра УИТС"),
        "Кафедра ИТВС" : lambda first_name, last_name: Teacher(first_name, last_name, "Кафедра ИТВС")
    },
    "Студент" : {
        "Прикладная информатика" : lambda first_name, last_name, group: Student(first_name, last_name, "Прикладная информатика", group),
        "Программная инжерия" : lambda first_name, last_name, group: Student(first_name, last_name, "Программная инжерия", group),
        "Информатика и вычислительная техника" : lambda first_name, last_name, group: Student(first_name, last_name, "Информатика и вычислительная техника", group)
    }
}

PERSON_FROM_DICT = {
    "Преподаватель" : lambda teacher_data: Teacher.from_dict(teacher_data),
    "Студент" : lambda student_data: Student.from_dict(student_data)
}
