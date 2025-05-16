from database_ar.db_automobiles_rental import get_connection
from ui_ar.menu import main_menu
from ui_ar.menu_bodyType import menu_bodyType
from ui_ar.menu_automobiles import menu_automobiles
from ui_ar.menu_clients import menu_clients
from ui_ar.menu_booking import menu_booking
from ui_ar.menu_contract import menu_contract
def main():
    get_connection()
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