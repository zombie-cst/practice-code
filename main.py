from database_ar.db_automobiles_rental import initialize_db
from ui_ar.menu import main_menu
from ui_ar.menu_employees import menu_employees
from ui_ar.menu_body_type import menu_body_type
from ui_ar.menu_automobiles import menu_automobiles
from ui_ar.menu_clients import menu_clients
from ui_ar.menu_booking import menu_booking
from ui_ar.menu_contract import menu_contract

def main():
    initialize_db()
    while True:
        choice = main_menu()
        if choice == '1':
            menu_employees()
        elif choice == '2':
            menu_body_type()
        elif choice == '3':
            menu_automobiles()
        elif choice == '4':
            menu_clients()
        elif choice == '5':
            menu_booking()
        elif choice == '6':
            menu_contract()
        elif choice == '0':
            print('\n🚪Выход из программы.')
            break
        else:
            print('❌Некоректный ввод.')
if __name__ == '__main__':
    main()