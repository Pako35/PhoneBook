# Определение словаря для хранения данных телефонного справочника
phone_directory = {}

# Функция для добавления нового контакта
def add_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phone_directory[(last_name, first_name)] = (patronymic, phone_number)
    print("Контакт успешно добавлен!")

# Функция для отображения всех контактов
def display_contacts():
    for name, (patronymic, phone_number) in phone_directory.items():
        print(f"{name[0]} {name[1]} ({patronymic}): {phone_number}")

# Функция для поиска контакта
def search_contact():
    search_term = input("Введите условие поиска (фамилия, имя или номер телефона): ")
    for name, (patronymic, phone_number) in phone_directory.items():
        if search_term.lower() in (name[0].lower(), name[1].lower(), phone_number):
            print(f"{name[0]} {name[1]} ({patronymic}): {phone_number}")

# Функция для изменения контакта
def modify_contact():
    last_name = input("Введите фамилию контакта для изменения: ")
    first_name = input("Введите имя контакта для изменения: ")
    if (last_name, first_name) in phone_directory:
        patronymic, phone_number = phone_directory[(last_name, first_name)]
        print(f"Текущие данные: {last_name} {first_name} ({patronymic}): {phone_number}")
        patronymic = input("Введите новое отчество (оставьте пустым, чтобы сохранить текущее): ")
        phone_number = input("Введите новый номер телефона (оставьте пустым, чтобы сохранить текущий): ")
        phone_directory[(last_name, first_name)] = (patronymic, phone_number)
        print("Контакт успешно изменен!")
    else:
        print("Контакт не найден.")

# Функция для удаления контакта
def delete_contact():
    last_name = input("Введите фамилию контакта для удаления: ")
    first_name = input("Введите имя контакта для удаления: ")
    if (last_name, first_name) in phone_directory:
        del phone_directory[(last_name, first_name)]
        print("Контакт успешно удален!")
    else:
        print("Контакт не найден.")

# Главный цикл меню
while True:
    print("\nМеню телефонного справочника:")
    print("1. Добавить контакт")
    print("2. Отобразить контакты")
    print("3. Поиск контакта")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Выйти")
    choice = input("Введите ваш выбор: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        modify_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        break
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
