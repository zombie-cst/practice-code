from models_ar.booking import Booking, get_all_booking
from models_ar.automobiles import get_all_automobiles
from models_ar.clients import get_all_clients
from models_ar.employees import get_all_employees

def menu_booking():
    while True:
        print("\n----- Бронь 🔑 -----")
        print("1. ☑️Добавить бронь")
        print("2. 👀Показать все брони")
        print("3. 🗑Удалить бронь")
        print("4. 🛠Изменить бронь")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            print('\n☑️Добавление новую бронь.')
            date_issue = input('Дата выпуска: ')
            return_date = input('Дата возврата: ')
            addres = input('Адрес: ')
            print('Доступные автомобили:')
            automobiles = get_all_automobiles()
            for n in automobiles:
                print(f'{n.id} - {n.brand} {n.model} '
                f'| Кузов ID: {n.body_type_id} | Цена за день: {n.price}'
                f'\nТопливо: {n.fuel} Цвет: {n.color} '
                f'| Год выпуска: {n.year_release}')
            automobiles_id = int(input('Введите ID автомобиля: '))
            print('Доступные клиенты:')
            clients = get_all_clients()
            for n in clients:
                print(f'{n.id}. ФИО: {n.last_name} {n.first_name} {n.patronymic}'
                        f'\nНомер телефона: {n.phone_number} '
                        f'| Адрес: {n.addres}')
            clients_id = int(input('Введите ID клиента: '))
            print('Доступные сотрудники:')
            employees = get_all_employees()
            for n in employees:
                print(f'{n.id}. ФИО: {n.last_name} {n.first_name} {n.patronymic}'
                        f'\nНомер телефона: {n.phone_number} ')
            employees_id = int(input('Введите ID сотрудника: '))
            booking = Booking(date_issue=date_issue, return_date=return_date,
                              addres=addres, automobiles_id=automobiles_id,
                              clients_id=clients_id, employees_id=employees_id)
            booking.save()
            print('☑️Бронь добавлен.')
        elif choice == '2':
            booking = get_all_booking()
            print('\n📜Список броней:')
            for n in booking:
                print(f'{n.id}. '
                      f'Даты выдачи и возврата: {n.date_issue}-{n.return_date}'
                      f'\nАдрес: {n.addres} '
                      f'\nАвтомобиль ID: {n.automobiles_id}'
                      f'\nКлиент ID: {n.clients_id}'
                      f'\nСотрудник: {n.employees_id}')
        elif choice == '3':
            id = int(input('🗑Введите ID брони, для удаления: '))
            if id is not None:
                decision = input('Вы действительно хотите удалить эту бронь? (д/н): ')
                if decision == 'д':
                    contract = Booking(id=int(id))
                    contract.delete()
                    print('🗑Бронь удалена.')
                else:
                    print('❌Бронь не удалена.')
            else:
                print('❌Бронь не найдена!')
        elif choice == '4':
            id = int(input('\n🛠Введите ID брони, для обновления: '))
            print("Оставьте поле пустым, чтобы не изменять значение.")
            current_booking = next((p for p in get_all_booking() 
                                    if p.id == id), None)
            if not current_booking:
                print("❌Бронь не найдена!")
                continue
            date_issue = input('Дата выпуска: ')
            return_date = input('Дата возврата: ')
            addres = input('Адрес: ')
            print('Доступные автомобили:')
            automobiles = get_all_automobiles()
            for n in automobiles:
                print(f'{n.id} - {n.brand} {n.model} '
                f'| Кузов ID: {n.body_type_id} | Цена за день: {n.price}'
                f'\nТопливо: {n.fuel} Цвет: {n.color} '
                f'| Год выпуска: {n.year_release}')
            automobiles_id = input('Введите ID автомобиля: ')
            print('Доступные клиенты:')
            clients = get_all_clients()
            for n in clients:
                print(f'{n.id}. ФИО: {n.last_name} {n.first_name} {n.patronymic}'
                        f'\nНомер телефона: {n.phone_number} '
                        f'| Адрес: {n.addres}')
            clients_id = input('Введите ID клиента: ')
            print('Доступные сотрудники:')
            employees = get_all_employees()
            for n in employees:
                print(f'{n.id}. ФИО: {n.last_name} {n.first_name} {n.patronymic}'
                        f'\nНомер телефона: {n.phone_number} ')
            employees_id = int(input('Введите ID сотрудника: '))
            booking = Booking(date_issue=date_issue if date_issue else current_booking.date_issue,
                              return_date=return_date if return_date else current_booking.return_date,
                              addres=addres if addres else current_booking.addres,
                              automobiles_id=int(automobiles_id) if automobiles_id else current_booking.automobiles_id,
                              clients_id=int(clients_id) if clients_id else current_booking.clients_id,
                              employees_id=int(employees_id) if employees_id else current_booking.employees_id)
            booking.save()
            print('🛠Бронь обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')