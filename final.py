username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату в формате 'день-месяц-год' (укажите дату цифрами): ")
issue_date = input("Введите дату истечения в формате 'день-месяц-год' (укажите дату цифрами): ")
subtitle = [] #подзаголовки
for i in range(3): # кол-во подзаголовков 3
    titles = input(f"Введите подзаголовок заметки {i + 1}: ")
    subtitle.append(titles)

note = [ # вся информация
    "Имя пользователя: ", username,
    "Заголовок заметки: ", title,
    "Содержание заметки: ", content,
    "Статус: ", status,
    "Дата создания: ", created_date,
    "Дата истечения: ", issue_date,
    [
      "Подзаголовок 1:", subtitle[0], "Подзаголовок 2:", subtitle[1], "подзаголовок 3:", subtitle[2]
    ]
]
print(note)