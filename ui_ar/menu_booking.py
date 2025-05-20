from models_ar.booking import Booking, get_all_booking
from models_ar.automobiles import get_all_automobiles, get_automobiles_by_id
from models_ar.clients import get_all_clients, get_clients_by_id
def menu_booking():
    while True:
        print("\n=== Бронь 🔑 ===")
        print("1. 👀Показать все брони")
        print("2. ☑️Добавить бронь")
        print("3. ❌Удалить бронь")
        print("4. 🛠Изменить бронь")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            booking = get_all_booking()
            if booking is not None:
                print('\n📜Список броней:')
                for n in booking:
                    print(f'{n.id}. Даты выдачи и возврата:{n.dateIssue} - {n.returnDate} | Адрес: {n.addres} '
                          f'\nАвтомобиль ID: {n.automobiles_id}'
                          f'\nКлиент ID: {n.clients_id}')
            else:
                print('Брони пока нет в списке!')
        elif choice == '2':
            print('\n☑️Добавление новую бронь.')
            dateIssue = input('Дата выпуска: ')
            returnDate = input('Дата возврата: ')
            addres = input('Адрес: ')
            print('\nДоступные автомобили:')
            automobiles = get_all_automobiles()
            for n in automobiles:
                print(f'{n.id} - {n.brand} {n.model} | Кузов ID: {n.bodyType_id} | Цена: {n.price}'
                      f'\nТопливо: {n.fuel} Цвет: {n.color} | Год выпуска: {n.yearRelease}')
            automobiles_id = int(input('Введите ID автомобиля: '))
            print('\nДоступные клиенты:')
            clients = get_all_clients()
            for n in clients:
                print(f'{n.id}. ФИО: {n.lastName} {n.firstName} {n.patronymic}'
                        f'\nНомер телефона: {n.phoneNumber} | Адрес: {n.addres}')
            clients_id = int(input('Введите ID клиента: '))
            booking = Booking(dateIssue=dateIssue, returnDate=returnDate, addres=addres, automobiles_id=automobiles_id, clients_id=clients_id)
            booking.save()
            print('☑️Бронь добавлен.')
        elif choice == '3':
            id = int(input('❌Введите ID брони, который хотите удалить: '))
            if id is not None:
                booking = Booking(id=int(id))
                booking.delete()
                print('❌Бронь удалён.')
            else:
                print('Бронь не найдена!')
        elif choice == '4':
            id = int(input('🛠Введите ID брони, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение.")
            current_booking = next((p for p in get_all_booking if p.id == id), None)
            if not current_booking:
                print("Бронь не найдена!")
                continue
            dateIssue = input('Дата выпуска: ')
            returnDate = input('Дата возврата: ')
            addres = input('Адрес: ')
            print('\nДоступные автомобили:')
            automobiles = get_all_automobiles()
            for n in automobiles:
                print(f'{n.id} - {n.brand} {n.model} | Кузов ID: {n.bodyType_id} | Цена: {n.price}'
                      f'\nТопливо: {n.fuel} | Цвет: {n.color} | Год выпуска: {n.yearRelease}')
            automobiles_id = int(input('Введите ID автомобиля: '))
            print('\nДоступные клиенты:')
            clients = get_all_clients()
            for n in clients:
                print(f'{n.id}. ФИО: {n.lastName} {n.firstName} {n.patronymic}'
                          f'\nНомер телефона: {n.phoneNumber} | Адрес: {n.addres}')
            clients_id = int(input('Введите ID клиента: '))
            booking = Booking(dateIssue=dateIssue if dateIssue else current_booking.dateIssue,
                                      returnDate=returnDate if returnDate else current_booking.returnDate,
                                      addres=addres if addres else current_booking.addres,
                                      automobiles_id=automobiles_id if automobiles_id else current_booking.automobiles_id,
                                      clients_id=clients_id if clients_id else current_booking.clients_id,)
            booking.save()
            print('🛠Бронь обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')