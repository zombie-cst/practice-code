from models_ar.employees import Employees, get_all_employees

def menu_employees():
    while True:
        print("\n----- Сотрудник 👨‍💼 -----")
        print("1. ☑️Добавения сотрудника")
        print("2. 👀Показать всех сотрудников")
        print("3. 🗑Удаления сотрудника")
        print("4. 🛠Изменения сотрудника")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            print('\n☑️Добавление нового сотрудника.')
            first_name = input('Имя: ')
            last_name = input('Фамилия: ')
            patronymic = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            employees = Employees(first_name=first_name, last_name=last_name,
                                  patronymic=patronymic, phone_number=phone_number)
            employees.save()
            print('☑️Сотрудник добавлен.')
        elif choice == '2':
            employees = get_all_employees()
            print('\n📜Список сотрудников:')
            for n in employees:
                print(f'{n.id}. ФИО: {n.last_name} {n.first_name} {n.patronymic}'
                      f'\nНомер телефона: {n.phone_number}')
        elif choice == '3':
            id = int(input('🗑Введите ID сотрудника, для удаления: '))
            if id is not None:
                decision = input('Вы действительно хотите удалить этого сотрудника? (д/н): ')
                if decision == 'д':
                    contract = Employees(id=int(id))
                    contract.delete()
                    print('🗑Сотрудник удалён.')
                else:
                    print('❌Сотрудник не удалён.')
            else:
                print('❌Сотрудник не найден!')
        elif choice == '4':
            id = int(input('\n🛠Введите ID сотрудника, для обновления: '))
            print("Оставьте поле пустым, чтобы не изменять значение")
            current_employees = next((p for p in get_all_employees() 
                                    if p.id == id), None)
            if not current_employees:
                print("❌Сотрудник не найден!")
                continue
            first_name = input('Имя: ')
            last_name = input('Фамилия: ')
            patronymic = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            employees = Employees(first_name=first_name if first_name else current_employees.first_name,
                                  last_name=last_name if last_name else current_employees.last_name,
                                  patronymic=patronymic if patronymic else current_employees.patronymic,
                                  phone_number=phone_number if phone_number else current_employees.phone_number)
            employees.save()
            print('🛠Сотрудник обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')