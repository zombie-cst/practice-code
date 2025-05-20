from models_ar.bodyType import BodyType, get_all_body_type
def menu_bodyType():
    while True:
        print("\n=== Типы 🚙 ===")
        print("1. 👀Показать все типы")
        print("2. ☑️Добавить тип")
        print("3. ❌Удалить тип")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            bodyType = get_all_body_type()
            if bodyType is not None:
                print('\n📜Список типов:')
                for n in bodyType:
                    print(f'{n.id}. {n.name}')
            else:
                print('Типов кузова пока нет в списке!')
        elif choice == '2':
            print('\n☑️Добавление нового типа.')
            name = input('Название: ')
            bodyType = BodyType(name=name)
            bodyType.save()
            print('☑️Тип добавлен.')
        elif choice == '3':
            id = int(input('❌Введите ID типа, который хотите удалить: '))
            if id is not None:
                bodyType = BodyType(id=int(id))
                bodyType.delete()
                print('❌Тип удалён.')
            else:
                print('Тип не найден!')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')