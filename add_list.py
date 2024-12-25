username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки: ")
created_date = input("Введите дату в формате 'день-месяц-год' (укажите дату цифрами): ")
issue_date = input("Введите дату истечения в формате 'день-месяц-год' (укажите дату цифрами): ")
subtitle = [] #подзаголовки
for i in range(3): # кол-во подзаголовков 3
    titles = input("Введите подзаголовок заметки {i + 1}: ")
    subtitle.append(titles)

print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
print("Подзаголовки заметки:",subtitle,)