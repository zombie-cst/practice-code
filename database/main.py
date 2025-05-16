from database.db_automobiles_rental import initialize_db
from ui.menu import main_menu
from ui.menu_bodyType import menu_bodyType
from ui.menu_automobiles import menu_automobiles
from ui.menu_clients import menu_clients
from ui.menu_booking import menu_booking
from ui.menu_contract import menu_contract
def main():
    initialize_db()
    while True:
        choice = main_menu()
        if choice == '1':
            menu_bodyType()
        elif choice == '2':
            menu_automobiles()
        elif choice == '3':
            menu_clients()
        elif choice == '4':
            menu_booking()
        elif choice == '5':
            menu_contract()
        elif choice == '0':
            print('🚪Выход из программы.')
            break
        else:
            print('❌Некоректный ввод.')
if __name__ == '__main__':
    main()