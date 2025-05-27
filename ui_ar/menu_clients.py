from models_ar.clients import Clients, get_all_clients

def menu_clients():
    while True:
        print("\n----- Клиенты 👥 -----")
        print("1. ☑️Добавения клиента")
        print("2. 👀Показать всех клиентов")
        print("3. 🗑Удаления клиента")
        print("4. 🛠Изменения клиента")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            print('\n☑️Добавление нового клиента.')
            first_name = input('Имя: ')
            last_name = input('Фамилия: ')
            patronymic = input('Отчество: ')
            addres = input('Адрес: ')
            phone_number = input('Номер телефона: ')
            clients = Clients(first_name=first_name, last_name=last_name,
                              patronymic=patronymic, addres=addres,
                              phone_number=phone_number)
            clients.save()
            print('☑️Клиент добавлен.')
        elif choice == '2':
            clients = get_all_clients()
            print('\n📜Список клиентов:')
            for n in clients:
                print(f'{n.id}. ФИО: {n.last_name} {n.first_name} {n.patronymic}'
                      f'\nНомер телефона: {n.phone_number}'
                      f'\nАдрес: {n.addres}')
        elif choice == '3':
            id = int(input('🗑Введите ID клиента, для удаления: '))
            if id is not None:
                decision = input('Вы действительно хотите удалить этого клиента? (д/н): ')
                if decision == 'д':
                    contract = Clients(id=int(id))
                    contract.delete()
                    print('🗑Клиент удалён.')
                else:
                    print('❌Клиент не удалён.')
            else:
                print('❌Клиент не найден!')
        elif choice == '4':
            id = int(input('\n🛠Введите ID клиента, для обновления: '))
            print("Оставьте поле пустым, чтобы не изменять значение")
            current_clients = next((p for p in get_all_clients() 
                                    if p.id == id), None)
            if not current_clients:
                print("❌Клиент не найден!")
                continue
            first_name = input('Имя: ')
            last_name = input('Фамилия: ')
            patronymic = input('Отчество: ')
            addres = input('Адрес: ')
            phone_number = input('Номер телефона: ')
            clients = Clients(first_name=first_name if first_name else current_clients.first_name,
                                      last_name=last_name if last_name else current_clients.last_name,
                                      patronymic=patronymic if patronymic else current_clients.patronymic,
                                      addres=addres if addres else current_clients.addres,
                                      phone_number=phone_number if phone_number else current_clients.phone_number)
            clients.save()
            print('🛠Клиент обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')