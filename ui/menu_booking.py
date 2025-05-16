from models.booking import Booking, get_all_booking
from models.automobiles import get_all_automobiles, get_automobiles_by_id
from models.clients import get_all_clients, get_clients_by_id
def menu_booking():
    while True:
        print("\n=== Бронь ===")
        print("1. Показать все брони")
        print("2. Добавить бронь")
        print("3. Удалить бронь")
        print("4. Изменить бронь")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            booking = get_all_booking()
            print('\nСписок броней:')
            for n in booking:
                print(f'\n{n.id}. {n.dateIssue} {n.returnDate}, {n.addres}, '
                      f'{n.automobiles_id}, {n.clients_id}')
        elif choice == '2':
            print('\nДобавление новую бронь.')
            dateIssue = input('Дата выпуска: ')
            returnDate = input('Дата возврата: ')
            addres = int(input('Адрес: '))
            print('\nДоступные автомобили:')
            automobiles = get_all_automobiles()
            for n in automobiles:
                print(f"{n.id} - {n.name}")
            automobiles_id = int(input('Введите ID автомобиля: '))
            print('\nДоступные клиенты:')
            clients = get_all_clients()
            for n in clients:
                print(f"{n.id} - {n.name}")
            clients_id = int(input('Введите ID клиента: '))
            booking = Booking(dateIssue=dateIssue, returnDate=returnDate, addres=addres,
                              automobiles_id=automobiles_id, clients_id=clients_id)
            booking.save()
            print('Бронь добавлен.')
        elif choice == '3':
            id = int(input('Введите ID брони, который хотите удалить: '))
            booking = Booking(id=int(id))
            booking.delete()
            print('бронь удалён.')
        elif choice == '4':
            id = int(input('Введите ID брони, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение.")
            current_booking = next((p for p in get_all_booking if p.id == id), None)
            if not current_booking:
                print("Бронь не найдена!")
                continue
            dateIssue = input('Дата выпуска: ')
            returnDate = input('Дата возврата: ')
            addres = int(input('Адрес: '))
            print('\nДоступные автомобили:')
            automobiles = get_all_automobiles()
            for n in automobiles:
                print(f"{n.id} - {n.name}")
            automobiles_id = int(input('Введите ID автомобиля: '))
            print('\nДоступные клиенты:')
            clients = get_all_clients()
            for n in clients:
                print(f"{n.id} - {n.name}")
            clients_id = int(input('Введите ID клиента: '))
            booking = Booking(dateIssue=dateIssue if dateIssue else current_booking.dateIssue,
                                      returnDate=returnDate if returnDate else current_booking.returnDate,
                                      addres=addres if addres else current_booking.addres,
                                      automobiles_id=automobiles_id if automobiles_id else current_booking.automobiles_id,
                                      clients_id=clients_id if clients_id else current_booking.clients_id,)
            booking.save()
            print('Бронь обновлён.')
        elif choice == '0':
            break
        else:
            print('Некоректный ввод.')