from datetime import date
import re

def creat_note():

    global notebook

    current_date = date.today() # возвращает сегоднящний день: {date} (datetime.date(2025, 1, 19))
    created_date = current_date.strftime("%d-%m-%Y") # Сегоднящний день в строковом типе данных в формате: {str} 'день-месяц-год'



    # Имя пользователя
    while True:
        # Просим ввести имя пользователя
        # Назначаем позволительные символы для имени
        username = input("Введите имя пользователя: ").strip().capitalize() # {str}
        pattern = "^[A-Za-zА-Яа-я0-9_-]+$"

        # Защита от пустого ввода
        if not username:
            print("Ввод не может быть пустым.\n"
                  "Пожалуйста, введите имя."
                  )
            continue
        # Защита от короткого ввода
        elif len(username) < 3:
            print("Имя пользователя слишком короткое.\n"
                  "Оно должно содержать хотя бы 3 символа."
                  )
            continue
        # Защита от длинного ввода
        elif len(username) > 30:
            print("Имя слишком длинное.\n "
                  "Оно не должно превышать 30 символов."
                  )
            continue
        # Проверяем имя на допустимые символы
        elif not re.match(pattern, username):
            print("Имя пользователя содержит недопустимые символы. \n"
                  "Оно должно содержать только буквы, "
                  "цифры, дефисы и подчеркивания."
                  )
            continue
        else:
            print(f"Имя пользователя {username}!")
            break



    # Заголовок
    while True:
        # Просим пользователя ввести заголовок для заметки.
        # Символы, которые могут применяться для заголовка
        title = input("Введите заголовок заметки: ").strip().title() # {str}
        pattern = "^[A-Za-zА-Яа-я0-9 _-]+$"

        # Защита от пустого ввода
        if not title:
            print("Заголовок не может быть пустым.]\n"
                  "Пожалуйста, введите заголовок."
                  )
            continue
        # Защита от короткого ввода
        elif len(title) < 3:
            print("Заголовок слишком короткий.\n"
                  "Он должен содержать хотя бы 3 символа."
                  )
            continue
        # Защита от длинного ввода
        elif len(title) > 100:
            print("Заголовок слишком длинный.\n"
                  "Он не должен превышать 100 символов."
                  )
            continue
        # Защита от использования некорретных символов
        elif not re.match(pattern, title):
            print("Заголовок содержит недопустимые символы.\n"
                  "Пожалуйста, используйте только буквы, цифры, пробелы, дефисы и подчеркивания."
                  )
            continue
        # При корректном заголовке выходим из цикла
        else:
            print(f"Заголовок заметки {title}!")
            break



    # Описание
    while True:
        # Просим пользвателя ввести описание
        content = input("Введите описание заметки: ").strip() # {str}

        # Защита от пустого ввода
        if not content:
            print("Описание не может быть пустым.\n"
                  "Пожалуйста, введите описание."
                  )
            continue
        # Защита от короткого ввода
        elif len(content) < 10:
            print("Описание слишком короткое.\n"
                  "Оно должно быть минимум 10 символов."
                  )
            continue
        # Защита от длинного ввода
        elif len(content) > 1000:
            print("Описание слишком длинное.\n"
                  "Оно не должно превышать 1000 символов."
                  )
            continue
        # При корректном описании выходим из цикла
        else:
            print(f"Вы ввели корректное описание!")
            break



    # Статус
    while True:
        # Просим пользователя ввести статус заметки
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").lower().strip() # {str}

        # Ввод должен содержать только те значения, которые
        # приведены в качестве примеров, иначе возвращаем пользователя к вводу.
        if not status:
            print("Статус не может быть пустым.\n"
                  "Пожалуйста, введите статус."
                  )
            continue
        elif status == "новая":
            print(f"Заявка со статусом {status}!")
            break
        elif status == "в процессе":
            print(f"Заявка со статусом {status}!")
            break
        elif status == "выполнено":
            print(f"Заявка со статусом {status}!")
            break
        else:
            print("Неверный статус. Введите статус по примеру предложенных.")



    # Получение даты дедлайна от пользователя с защитой от дурака
    while True:
        # Просим пользователя ввести дату дедлайна,
        deadline_date = input("Введите дату дедлайна (день-месяц-год): ").strip()

        if not deadline_date:
            print("Вы ничего не ввели. Попробуйте снова.")
            continue

        # Проверка на наличие недопустимых символов
        if re.search(r'[a-zA-Zа-яА-Я!"№%?*()+=~@#$^&<>{}]', deadline_date):
            print("Вы ввели не позволительные символы.\nВозможно буквы, попробуйте снова ввести дату по примеру.")
            continue

        # Разделение строки на компоненты даты
        issue_date = re.split(r'[ /.,\\:;\-_]+', deadline_date)

        # В случае, если введен только день, месяц и год текущие
        if len(issue_date) == 1:
            day, month, year = int(issue_date[0]), current_date.month, current_date.year
        # В случае, если введены только день и месяц, год текущий
        elif len(issue_date) == 2:
            day, month, year = int(issue_date[0]), int(issue_date[1]), current_date.year
        # Введены день, месяц и год
        elif len(issue_date) == 3:
            day, month, year = map(int, issue_date)
        else:
            print("Вы ввели слишком много данных. Попробуйте снова.")
            continue

        # Проверка формата даты
        issue_date = f"{day}-{month}-{year}"
        if re.match(r"^\d{1,2}-\d{1,2}-\d{4}$", issue_date):
            print("Дата соответствует формату")
        else:
            print("Некорректный формат даты")
            continue

        # Проверка корректности месяца
        if not (1 <= month <= 12):
            print(f"В году не может быть больше 12 месяцев.\n"
                  f"Вы ввели {month}.")
            continue

        # Проверка корректности дня, включая проверку високосного года,
        # если is_leap_year == True => 29 дней в феврале, == False => 28
        is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if month in {1, 3, 5, 7, 8, 10, 12}:
            max_days = 31
        elif month in {4, 6, 9, 11}:
            max_days = 30
        elif is_leap_year:
            max_days = 29
        else:
            max_days = 28

        # Проверка на количество дней в месяце
        if not (1 <= day <= max_days):
            print(f"Некорректная дата.\n"
                  f"В месяце {month} не может быть столько дней."
                  )
            continue

        if issue_date == f"{day}-{month}-{year}":
            break



    notebook = {"username": username,
            "title": title,
            "content": content,
            "status": status,
            "created_date": created_date,
            "issue_date": issue_date
            }
    return notebook
creat_note()
print(f"Заметка создана: {notebook}")