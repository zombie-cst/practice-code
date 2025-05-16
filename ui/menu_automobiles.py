from models.automobiles import Automobiles, get_all_automobiles
from models.bodyType import get_all_bodyType, get_bodyType_by_id
def menu_automobiles():
    while True:
        print("\n=== Автомобили ===")
        print("1. Показать все автомобили")
        print("2. Добавить автомобиль")
        print("3. Удалить автомобиль")
        print("4. Изменить автомобиль")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            automobiles = get_all_automobiles()
            print('\nСписок автомобилей:')
            for n in automobiles:
                print(f'\n{n.id}. {n.brend} {n.model}, {n.yearRelease}, {n.fuel}, '
                      f'{n.speed}, {n.color}, {n.price}, {n.odyType_id}')
        elif choice == '2':
            print('\nДобавление нового автомобиля.')
            brend = input('Бренд: ')
            model = input('Модель: ')
            yearRelease = int(input('Год выпуска: '))
            fuel = input('Топливо: ')
            speed = input('Скорость: ')
            color = input('Цвет: ')
            price = float(input('Цена: '))
            print('\nДоступные типы:')
            type = get_all_bodyType()
            for n in type:
                print(f"{n.id} - {n.name}")
            bodyType_id = int(input('Введите ID типа: '))
            automobiles = Automobiles(brend=brend, model=model, yearRelease=yearRelease, fuel=fuel,
                                      speed=speed, color=color, price=price, bodyType_id=bodyType_id)
            automobiles.save()
            print('Автомобиль добавлен.')
        elif choice == '3':
            id = int(input('Введите ID автомобиля, который хотите удалить: '))
            automobiles = Automobiles(id=int(id))
            automobiles.delete()
            print('Автомобиль удалён.')
        elif choice == '4':
            id = int(input('Введите ID автомобиля, который хотите обновить: '))
            print("\nОставьте поле пустым, чтобы не изменять значение")
            current_automobiles = next((p for p in get_all_automobiles if p.id == id), None)
            if not current_automobiles:
                print("Автомобиль не найден!")
                continue
            brend = input('Новый бренд: ')
            model = input('Новая модель: ')
            yearRelease = int(input('Новый год выпуска: '))
            fuel = input('Новое топливо: ')
            speed = input('Нвая скорость: ')
            color = input('Нвый цвет: ')
            price = float(input('Новая цена: '))
            print('Доступные типы:')
            type = get_all_bodyType()
            for n in type:
                print(f"{n.id} - {n.name}")
            bodyType_id = int(input('Введите ID нового типа: '))
            automobiles = Automobiles(brend=brend if brend else current_automobiles.brend,
                                      model=model if model else current_automobiles.model,
                                      yearRelease=yearRelease if yearRelease else current_automobiles.yearRelease,
                                      fuel=fuel if fuel else current_automobiles.fuel,
                                      speed=speed if speed else current_automobiles.speed,
                                      color=color if color else current_automobiles.color,
                                      price=price if price else current_automobiles.price,
                                      bodyType_id=bodyType_id if bodyType_id else current_automobiles.bodyType_id)
            automobiles.save()
            print('Автомобиль обновлён.')
        elif choice == '0':
            break
        else:
            print('Некоректный ввод.')