from models_ar.automobiles import Automobiles, get_all_automobiles
from models_ar.bodyType import get_all_body_type, get_body_type_by_id
def menu_automobiles():
    while True:
        print("\n----- Автомобили 🚗 -----")
        print("1. 👀Показать все автомобили.")
        print("2. ☑️Добавить автомобиль.")
        print("3. ❌Удалить автомобиль.")
        print("4. 🛠Изменить автомобиль.")
        print("0. 🚪Назад в главное меню.")
        choice = input("Выберите действие: ")
        if choice == '1':
            automobiles = get_all_automobiles()
            if automobiles is not None:
                print('\n📜Список автомобилей:')
                for n in automobiles:
                    print(f'{n.id}. {n.brand} {n.model} | Кузов ID: {n.bodyType_id} | Цена: {n.price} '
                          f'\nТопливо: {n.fuel} | Цвет: {n.color} | Год выпуска: {n.yearRelease}')
            else:
                print('Автомобилей пока нет в списке!')
        elif choice == '2':
            print('\n☑️Добавление нового автомобиля.')
            brand = input('Бренд: ')
            model = input('Модель: ')
            print('\nДоступные типы:')
            type = get_all_body_type()
            for n in type:
                print(f"{n.id} - {n.name}")
            bodyType_id = int(input('Введите ID типа: '))
            price = float(input('Цена(в день): '))
            fuel = input('Топливо: ')
            color = input('Цвет: ')
            yearRelease = int(input('Год выпуска: '))
            automobiles = Automobiles(brand=brand, model=model, yearRelease=yearRelease, fuel=fuel, color=color, price=price, bodyType_id=bodyType_id)
            automobiles.save()
            print('☑️Автомобиль добавлен.')
        elif choice == '3':
            id = int(input('❌Введите ID автомобиля, который хотите удалить: '))
            if id is not None:
                automobiles = Automobiles(id=int(id))
                automobiles.delete()
                print('❌Автомобиль удалён.')
            else:
                price('Автомобиль не найден!')
        elif choice == '4':
            id = int(input('🛠Введите ID автомобиля, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение")
            current_automobiles = next((p for p in get_all_automobiles if p.id == id), None)
            if not current_automobiles:
                print("Автомобиль не найден!")
                continue
            brand = input('Бренд: ')
            model = input('Модель: ')
            print('\nДоступные типы:')
            type = get_all_body_type()
            for n in type:
                print(f"{n.id} - {n.name}")
            bodyType_id = int(input('Введите ID типа: '))
            price = float(input('Цена: '))
            fuel = input('Топливо: ')
            color = input('Цвет: ')
            yearRelease = int(input('Год выпуска: '))
            automobiles = Automobiles(brand=brand if brand else current_automobiles.brand,
                                      model=model if model else current_automobiles.model,
                                      yearRelease=yearRelease if yearRelease else current_automobiles.yearRelease,
                                      fuel=fuel if fuel else current_automobiles.fuel,
                                      color=color if color else current_automobiles.color,
                                      price=price if price else current_automobiles.price,
                                      bodyType_id=bodyType_id if bodyType_id else current_automobiles.bodyType_id)
            automobiles.save()
            print('🛠Автомобиль обновлён.')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')