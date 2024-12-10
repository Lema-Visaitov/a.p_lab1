from exceptions.exceptions import InvalidPersonTypeException, PersonNotFoundException
from model.person import Person
from storage.serializer.jsonSerializer import JsonSerializer
from storage.serializer.xmlSerializer import XmlSerializer
from storage.storage import Storage
from services.personService import PersonService


def main():
    try:
        person: Person = Person.from_dict({
            "id": 1,
            "first_name": "asfsf",
            "last_name": "daf"
        })
        print("С каким форматом работать (1. json, 2. xml):")
        choice = input("Введите номер действия: ")
        if choice == "1":
            serializer = JsonSerializer()
        
        elif choice == "2":
            serializer = XmlSerializer()
        
        else:
            print("Неверный выбор, выход из программы.")
            return
        storage = Storage(serializer, "db")
        service = PersonService(storage)
        
        service.read()

        while True:
            print("\nВыберите действие:")
            print("1. Добавить человека")
            print("2. Обновить человека")
            print("3. Удалить человека")
            print("4. Показать всех людей")
            print("5. Выход")

            choice = input("Введите номер действия: ")

            try:
                if choice == "1":
                    person_data: dict = {}
                    person_type = input("Введите тип человека: ")
                    first_name = input("Введите имя человека: ")
                    last_name = input("Введите фамилию человека: ")
                    person_specific = input("Введите specific для человека: ")

                    person_data["type"] = person_type
                    person_data["first_name"] = first_name
                    person_data["last_name"] = last_name
                    person_data["specific"] = person_specific

                    if person_type == "Student":
                        person_group = input("Введите группу студента: ")
                        person_data["group"] = person_group

                    service.create(person_data)
                
                elif choice == "2":
                    id = int(input("Введите id человека, которого хотите изменить: "))
                    last_name = input("Введите фамилию человека, которую хотите изменить: ")
                    specific = int(input("Введите новый specific: "))
                    data = {
                        "last_name": last_name,
                        "specific": specific
                    }
                    service.update_movie(id, data)
                
                elif choice == "3":
                    id = input("Введите id человека: ")
                    service.delete(id)
                
                elif choice == "4":
                    service.read()
                
                elif choice == "5":
                    print("Выход из программы.")
                    break
                
                else:
                    print("Неверный выбор, попробуйте снова.")
            
            except PersonNotFoundException:
                print("Ошибка: такой человек не найден.")
            except InvalidPersonTypeException:
                print("Ошибка: такого типа человека нет.")
            except Exception as e:
                print(f"Произошла непредвиденная ошибка: {e}")
    
    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")
    except Exception as e:
        print(f"Произошла ошибка при запуске программы: {e}")


if __name__ == "__main__":
    main()