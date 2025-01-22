from datetime import date
import re




def parse_date(input_date, current_date):
    """
    Функция для получения даты дедлайна.
    Разбиваем {str} дату на части и преобразуем их в {int}.
    Если введён только день, используем текущий месяц и год, возвращаем дату.
    Если введены только день и месяц, используем текущий год, возвращаем дату.
    Если введены все данные возвращаем дату.
    Если введены некорректные данные возвращаем None.
    """

    try:
        parts = list(map(int, re.split(r"[ /.,\\:;\-_]+", input_date)))
        if len(parts) == 1:
            return date(current_date.year, current_date.month, parts[0])
        elif len(parts) == 2:
            return date(current_date.year, parts[1], parts[0])
        elif len(parts) == 3:
            return date(parts[2], parts[1], parts[0])
    except ValueError:
        return None




def invalid_input(prompt, pattern, min_length, max_length, error_messages):
    """
    Функция для проверки пользовательского ввода по определенным параметрам.
    Пользователь вводит, удаляем лишние пробелы.
    Защита от пустого ввода.
    Защита от короткого ввода.
    Защита от длинного ввода.
    Защита от использования недопустимых символов.
    В случае корректного ввода, возвращаем его.
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print(error_messages['empty'])
            continue
        if len(user_input) < min_length:
            print(error_messages['short'])
            continue
        if len(user_input) > max_length:
            print(error_messages['long'])
            continue
        if not re.match(pattern, user_input):
            print(error_messages['invalid'])
            continue
        return user_input




def create_note():
    """
    Функция для создания заметки.
    Получаем текущую дату.
    Форматируем её.
    Запрашиваем имя пользователя.
    Запрашиваем заголовок.
    Запрашиваем контент.
    Запрашиваем статус.
    Запрашиваем дату дедлайна.
    Проверяем корректность даты и её не находимость в прошлом.
    Форматируем дату.
    Собираем данные заметки в словарь.
    Выводим данные заметки и возвращаем их.
    """
    current_date = date.today()
    created_date = current_date.strftime("%d-%m-%Y")


    username = invalid_input(
        "Введите имя пользователя: ",
        r"^[A-Za-zА-Яа-я0-9_-]+$",
        3,
        30,
        {
            "empty": "Имя не может быть пустым.",
            "short": "Имя слишком короткое.",
            "long": "Имя слишком длинное.",
            "invalid": "Имя содержит недопустимые символы."
        }
    )


    title = invalid_input(
        "Введите заголовок заметки: ",
        r"^[A-Za-zА-Яа-я0-9 _-]+$",
        3,
        100,
        {
            "empty": "Заголовок не может быть пустым.",
            "short": "Заголовок слишком короткий.",
            "long": "Заголовок слишком длинный.",
            "invalid": "Заголовок содержит недопустимые символы."
        }
    )


    while True:
        content = input("Введите описание заметки: ").strip()
        if len(content) < 10:
            print("Описание слишком короткое.")
            continue
        elif len(content) > 1000:
            print("Описание слишком длинное.")
            continue
        break


    while True:
        status = input("Введите статус (новая, в процессе, выполнено): ").strip().lower()
        if status in {"новая", "в процессе", "выполнено"}:
            break
        print("Некорректный статус.")


    while True:
        deadline_date = input("Введите дату дедлайна (дд-мм-гггг, дд-мм или дд): ").strip()
        parsed_date = parse_date(deadline_date, current_date)
        if parsed_date and parsed_date >= current_date:
            issue_date = parsed_date.strftime("%d-%m-%Y")
            break
        print("Некорректная дата дедлайна.")


    notebook = {
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date
    }

    print(f"Заметка создана: {notebook}")
    return notebook

# Вызываем функцию для создания заметки
create_note()
