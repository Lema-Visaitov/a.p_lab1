import json
from storage.serializer.jsonSerializer import JsonSerializer
from model.person import Teacher
from utils.constants import PERSON_FROM_DICT

def main():
    serializer = JsonSerializer()
    teacher1 = Teacher("asd", "sd", "uits")
    teacher2 = Teacher("fhdasb", "ajllf", "csct")
    data = serializer.to_format([teacher1])
    teacher3 = PERSON_FROM_DICT["Преподаватель"](teacher1.__dict__())
    print(serializer.to_format([teacher3]))

if __name__ == "__main__":
    main()