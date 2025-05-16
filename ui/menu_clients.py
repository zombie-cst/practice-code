from models.clients import Clients, get_all_clients
def menu_clients():
    while True:
        print("\n=== Клиенты ===")
        print("1. Показать все клиентов")
        print("2. Добавить клиента")
        print("3. Удалить клиента")
        print("4. Изменить клиента")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            clients = get_all_clients()
            print('\nСписок клиентов:')
            for n in clients:
                print(f'\n{n.id}. {n.firstName} {n.lastName}, {n.patronymic}, '
                      f'{n.addres}, {n.phoneNumber}')
        elif choice == '2':
            print('\nДобавление нового клиента.')
            firstName = input('Имя: ')
            lastName = input('Фамилия: ')
            patronymic = int(input('Отчество: '))
            addres = input('Адрес: ')
            phoneNumber = input('Номер телефона: ')
            clients = Clients(firstName=firstName, lastName=lastName, patronymic=patronymic,
                              addres=addres, phoneNumber=phoneNumber)
            clients.save()
            print('Клиент добавлен.')
        elif choice == '3':
            id = int(input('Введите ID клиента, который хотите удалить: '))
            clients = Clients(id=int(id))
            clients.delete()
            print('Клиент удалён.')
        elif choice == '4':
            id = int(input('Введите ID клиента, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение")
            current_clients = next((p for p in get_all_clients if p.id == id), None)
            if not current_clients:
                print("Клиент не найден!")
                continue
            firstName = input('Имя: ')
            lastName = input('Фамилия: ')
            patronymic = int(input('Отчество: '))
            addres = input('Адрес: ')
            phoneNumber = input('Номер телефона: ')
            clients = Clients(firstName=firstName if firstName else current_clients.firstName,
                                      lastName=lastName if lastName else current_clients.lastName,
                                      patronymic=patronymic if patronymic else current_clients.patronymic,
                                      addres=addres if addres else current_clients.addres,
                                      phoneNumber=phoneNumber if phoneNumber else current_clients.phoneNumber)
            clients.save()
            print('Клиент обновлён.')
        elif choice == '0':
            break
        else:
            print('Некоректный ввод.')