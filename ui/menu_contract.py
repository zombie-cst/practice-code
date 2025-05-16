from models.contract import Contract, get_all_contract
from models.booking import get_all_booking, get_booking_by_id
def menu_contract():
    while True:
        print("\n=== Договоры ===")
        print("1. Показать все договоры")
        print("2. Добавить договор")
        print("3. Удалить договор")
        print("4. Изменить договор")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            contract = get_all_contract()
            print('\nСписок договоров:')
            for n in contract:
                print(f'\n{n.id}. {n.date} {n.rules}, {n.discounts}, '
                      f'{n.finalPrice}, {n.booking_id}')
        elif choice == '2':
            print('\nДобавление нового договора.')
            date = input('Дата: ')
            rules = input('Штрафы: ')
            discounts = int(input('Скидки: '))
            finalPrice = input('Итоговая стоимость: ')
            print('\nДоступные брони:')
            type = get_all_booking()
            for n in type:
                print(f"{n.id} - {n.name}")
            booking_id = int(input('Введите ID брони: '))
            contract = Contract(date=date, rules=rules, discounts=discounts,
                                finalPrice=finalPrice, booking_id=booking_id)
            contract.save()
            print('Договор добавлён.')
        elif choice == '3':
            id = int(input('Введите ID договора, который хотите удалить: '))
            contract = Contract(id=int(id))
            contract.delete()
            print('Договор удалён.')
        elif choice == '4':
            id = int(input('Введите ID договора, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение")
            current_contract = next((p for p in get_all_contract if p.id == id), None)
            if not current_contract:
                print("Дговор не найден!")
                continue
            date = input('Дата: ')
            rules = input('Штрафы: ')
            discounts = int(input('Скидки: '))
            finalPrice = input('Итоговая стоимость: ')
            print('\nДоступные брони:')
            type = get_all_booking()
            for n in type:
                print(f"{n.id} - {n.name}")
            booking_id = int(input('Введите ID брони: '))
            contract = Contract(date=date if date else current_contract.date,
                                      rules=rules if rules else current_contract.rules,
                                      discounts=discounts if discounts else current_contract.discounts,
                                      finalPrice=finalPrice if finalPrice else current_contract.finalPrice,
                                      booking_id=booking_id if booking_id else current_contract.booking_id)
            contract.save()
            print('Договор обновлён.')
        elif choice == '0':
            break
        else:
            print('Некоректный ввод.')