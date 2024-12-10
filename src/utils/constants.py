from model.person import Teacher, Student

JSON_DB_PATH = '../db/json/db.json'
XML_DB_PATH = '../db/xml/db.xml'

PERSON_MAP = {
    "Teacher" : {
        "Кафедра УИТС" : lambda first_name, last_name: Teacher(first_name, last_name, "Кафедра УИТС"),
        "Кафедра ИТВС" : lambda first_name, last_name: Teacher(first_name, last_name, "Кафедра ИТВС")
    },
    "Student" : {
        "прикладная информатика" : lambda first_name, last_name, group: Student(first_name, last_name, "Прикладная информатика", group),
        "программная инженерия" : lambda first_name, last_name, group: Student(first_name, last_name, "Программная инжерия", group),
        "информатика и вычислительная техника" : lambda first_name, last_name, group: Student(first_name, last_name, "Информатика и вычислительная техника", group)
    }
}

PERSON_FROM_DICT = {
    "Teacher" : lambda teacher_data: Teacher.from_dict(teacher_data),
    "Student" : lambda student_data: Student.from_dict(student_data)
}
