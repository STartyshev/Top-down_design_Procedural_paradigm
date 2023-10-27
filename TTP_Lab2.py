from console_ui import *
from number_of_common_numbers import *
from distance_between_points import *
from arithmetic_conversion import *
from os import system
from error_output import *


def main():
    """
    Функция старта главного меню.
    """
    while True:
        task_selection_item = ui_menu()

        match task_selection_item:
            case 1:
                ui_number_of_common_numbers()

            case 2:
                ui_distance_between_points()

            case 3:
                ui_arithmetic_conversion()

            case 4:
                system('CLS')
                return

            case _:
                print_error_message()


if __name__ == '__main__':
    main()