from models_ar.contract import Contract, get_all_contract
from models_ar.booking import get_all_booking, get_booking_by_id
def menu_contract():
    while True:
        print("\n=== Договоры 📑 ===")
        print("1. 👀Показать все договоры")
        print("2. ☑️Добавить договор")
        print("3. ❌Удалить договор")
        print("4. 🛠Изменить договор")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            contract = get_all_contract()
            if contract is not None:
                print('\n📜Список договоров:')
                for n in contract:
                    print(f'{n.id}. Штрафы: {n.rules}, Скидкa: {n.discounts}'
                          f'\nБронь ID: {n.booking_id}')
            else:
                print('Договоров пока нет в списке!')
        elif choice == '2':
            print('\n☑️Добавление нового договора.')
            rules = input('Штрафы: ')
            if rules == '':
                rules = 'Отсутствуют'
            discounts = int(input('Скидки(%): '))
            print('\nДоступные брони:')
            booking = get_all_booking()
            for n in booking:
                print(f'{n.id}. Даты выдачи и возврата:{n.dateIssue} - {n.returnDate} | Адрес: {n.addres} '
                          f'\nАвтомобиль ID: {n.automobiles_id}'
                          f'\nКлиент ID: {n.clients_id}')
            booking_id = int(input('Введите ID брони: '))
            contract = Contract(rules=rules, discounts=discounts, booking_id=booking_id)
            contract.save()
            print('☑️Договор добавлен.')
        elif choice == '3':
            id = int(input('❌Введите ID договора, который хотите удалить: '))
            if id is not None:
                contract = Contract(id=int(id))
                contract.delete()
                print('❌Договор удалён.')
            else:
                print('Дговор не найден!')
        elif choice == '4':
            id = int(input('🛠Введите ID договора, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение")
            current_contract = next((p for p in get_all_contract if p.id == id), None)
            if not current_contract:
                print("Дговор не найден!")
                continue
            rules = input('Штрафы: ')
            discounts = int(input('Скидки(%): '))
            print('\nДоступные брони:')
            type = get_all_booking()
            for n in type:
                print(f'{n.id}. Даты выдачи и возврата:{n.dateIssue} - {n.returnDate} | Адрес: {n.addres} '
                          f'\nАвтомобиль ID: {n.automobiles_id}'
                          f'\nКлиент ID: {n.clients_id}')
            booking_id = int(input('Введите ID брони: '))
            contract = Contract(rules=rules if rules else current_contract.rules,
                                discounts=discounts if discounts else current_contract.discounts,
                                booking_id=booking_id if booking_id else current_contract.booking_id)
            contract.save()
            print('🛠Договор обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')