from models_ar.body_type import BodyType, get_all_body_type

def menu_body_type():
    while True:
        print("\n----- Типы 🚙 -----")
        print("1. ☑️Добавить тип")
        print("2. 👀Показать все типы")
        print("3. 🗑Удалить тип")
        print("0. 🚪Назад в главное меню")
        choice = input("Выберите действие: ")
        if choice == '1':
            print('\n☑️Добавление нового типа.')
            name = input('Название: ')
            body_type = BodyType(name=name)
            body_type.save()
            print('☑️Тип добавлен.')
        elif choice == '2':
            body_type = get_all_body_type()
            print('\n📜Список типов:')
            for n in body_type:
                print(f'{n.id}. {n.name}')
        elif choice == '3':
            id = int(input('🗑Введите ID типа, для удаления: '))
            if id is not None:
                decision = input('Вы действительно хотите удалить этот тип? (д/н): ')
                if decision == 'д':
                    contract = BodyType(id=int(id))
                    contract.delete()
                    print('🗑Тип удалён.')
                else:
                    print('❌Тип не удалён.')
            else:
                print('❌Тип не найден!')
        elif choice == '0':
            break
        else:
            print('❌Некоректный ввод.')