from models_ar.automobiles import Automobiles, get_all_automobiles
from models_ar.body_type import get_all_body_type

def menu_automobiles():
    while True:
        print("\n----- Автомобили 🚗 -----")
        print("1. ☑️Добавить автомобиль.")
        print("2. 👀Показать все автомобили.")
        print("3. 🗑Удалить автомобиль.")
        print("4. 🛠Изменить автомобиль.")
        print("0. 🚪Назад в главное меню.")
        choice = input("Выберите действие: ")
        if choice == '1':
            print('\n☑️Добавление нового автомобиля.')
            brand = input('Бренд: ')
            model = input('Модель: ')
            print('Доступные типы:')
            type = get_all_body_type()
            for n in type:
                print(f"{n.id} - {n.name}")
            body_type_id = int(input('Введите ID типа: '))
            price = float(input('Цена(в день): '))
            fuel = input('Топливо: ')
            color = input('Цвет: ')
            year_release = int(input('Год выпуска: '))
            automobiles = Automobiles(brand=brand, model=model,
                                      year_release=year_release,
                                      fuel=fuel,
                                      color=color, price=price,
                                      body_type_id=body_type_id)
            automobiles.save()
            print('☑️Автомобиль добавлен.')
        elif choice == '2':
            automobiles = get_all_automobiles()
            print('\n📜Список автомобилей:')
            for n in automobiles:
                print(f'{n.id}. {n.brand} {n.model} '
                      f'| Кузов ID: {n.body_type_id} | Цена за день: {n.price} '
                      f'\nТопливо: {n.fuel} | Цвет: {n.color} '
                      f'| Год выпуска: {n.year_release}')
        elif choice == '3':
            id = int(input('🗑Введите ID автомобиля, для удаления: '))
            if id is not None:
                decision = input('Вы действительно хотите удалить этот автомбиль? (д/н): ')
                if decision == 'д':
                    contract = Automobiles(id=int(id))
                    contract.delete()
                    print('🗑Автомобиль удалён.')
                else:
                    print('❌Автомобиль не удалён.')
            else:
                price('❌Автомобиль не найден!')
        elif choice == '4':
            id = int(input('\n🛠Введите ID автомобиля, для обновления: '))
            print("Оставьте поле пустым, чтобы не изменять значение")
            current_automobiles = next((p for p in get_all_automobiles() 
                                        if p.id == id), None)
            if not current_automobiles:
                print("❌Автомобиль не найден!")
                continue
            brand = input('Бренд: ')
            model = input('Модель: ')
            print('Доступные типы:')
            type = get_all_body_type()
            for n in type:
                print(f"{n.id} - {n.name}")
            body_type_id = input('Введите ID типа: ')
            price = input('Цена: ')
            fuel = input('Топливо: ')
            color = input('Цвет: ')
            year_release = input('Год выпуска: ')
            automobiles = Automobiles(brand=brand if brand else current_automobiles.brand,
                                      model=model if model else current_automobiles.model,
                                      year_release=int(year_release) if year_release else current_automobiles.year_release,
                                      fuel=fuel if fuel else current_automobiles.fuel,
                                      color=color if color else current_automobiles.color,
                                      price=float(price) if price else current_automobiles.price,
                                      body_type_id=int(body_type_id) if body_type_id else current_automobiles.body_type_id)
            automobiles.save()
            print('🛠Автомобиль обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')