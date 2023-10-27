def ui_menu(text_menu):
    """
    Функция реализующая пользовательский интерфейс в консоли для произвольного меню.
    :param text_menu: Текст меню, который будет выводиться в консоли.
    :return: Возвращает выбранный пункт меню (целочисленное значение).
    """
    system('CLS')
    print(text_menu)

    while True:
        try:
            return int(input('Выберите пункт меню: '))
        except ValueError:
            print_error_message('Введенное значение должно быть цифрой! '
                                'Попробуйте еще раз.')
            print(text_menu)


def main_menu_for_tasks(task_name):
    """
    Функция реализующая пользовательский интерфейс в консоли для главного меню.
    :param task_name: Название задания для которого будет вызываться меню.
    :return: Возвращает номер выбранного пользователем пункта меню (результат работы функции ui_menu).
    """
    return ui_menu(
        f"{task_name}\n"
        f"Главное меню.\n"
        f"1. Условие задачи.\n"
        f"2. Ввод исходных данных.\n"
        f"3. Выполнение алгоритма.\n"
        f"4. Вывод результатов работы алгоритма.\n"
        f"5. Выход в главное меню."
    )
