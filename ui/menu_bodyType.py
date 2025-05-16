from models.bodyType import BodyType, get_all_bodyType
def menu_bodyType():
    while True:
        print("\n=== Типы ===")
        print("1. Показать все типы")
        print("2. Добавить тип")
        print("3. Удалить тип")
        print("0. Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            bodyType = get_all_bodyType()
            print('\nСписок типов:')
            for n in bodyType:
                print(f'\n{n.id}. {n.name}')
        elif choice == '2':
            print('\nДобавление нового типа.')
            name = input('Название: ')
            bodyType = BodyType(name=name)
            bodyType.save()
            print('Тип добавлен.')
        elif choice == '3':
            id = int(input('Введите ID типа, который хотите удалить: '))
            bodyType = BodyType(id=int(id))
            bodyType.delete()
            print('Тип удалён.')
        elif choice == '0':
            break
        else:
            print('Некоректный ввод.')