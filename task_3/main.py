# ВАРИАНТ 1
print("start code …")  # начало кода

import json  # импортируем модуль для работы с JSON
import os  # импортируем модуль для работы с файловой системой

filename = "fishes.json"  # имя файла для хранения записей

# если файла нет, создаем его с 5 подготовленными записями
if not os.path.exists(filename):  # проверяем наличие файла
    initial_data = [  # создаем список с 5 словарями о рыбах
        {"id": 1, "name": "Карп", "latin_name": "Cyprinus carpio", "is_salt_water_fish": False, "sub_type_count": 3},  # запись 1
        {"id": 2, "name": "Щука", "latin_name": "Esox lucius", "is_salt_water_fish": False, "sub_type_count": 2},      # запись 2
        {"id": 3, "name": "Треска", "latin_name": "Gadus morhua", "is_salt_water_fish": True, "sub_type_count": 4},  # запись 3
        {"id": 4, "name": "Сёмга", "latin_name": "Salmo salar", "is_salt_water_fish": True, "sub_type_count": 3},     # запись 4
        {"id": 5, "name": "Окунь", "latin_name": "Perca fluviatilis", "is_salt_water_fish": False, "sub_type_count": 2} # запись 5
    ]  # конец списка
    with open(filename, "w", encoding="utf-8") as f:  # открываем файл для записи
        json.dump(initial_data, f, ensure_ascii=False, indent=4)  # сохраняем записи в файл

operations_count = 0  # счетчик выполненных операций

while True:  # главный цикл меню
    try:
        with open(filename, "r", encoding="utf-8") as f:  # читаем данные из файла
            records = json.load(f)  # загружаем JSON в переменную
    except:
        records = []  # если не удалось, используем пустой список

    # выводим меню
    print("=== Меню ===")  # заголовок меню
    print("1. Вывести все записи")  # пункт 1
    print("2. Вывести запись по полю (id)")  # пункт 2
    print("3. Добавить запись")  # пункт 3
    print("4. Удалить запись по полю (id)")  # пункт 4
    print("5. Выйти из программы")  # пункт 5
    choice = input("Выберите номер пункта: ").strip()  # ввод пользователя

    if choice == "1":  # вывод всех записей
        if not records:  # если список пуст
            print("Записей нет.")  # предупреждение
        else:
            for idx, fish in enumerate(records, start=1):  # перебор записей с номером
                print("---------------------- Запись", idx, "-----------------------")  # разделитель
                print("id:", fish.get("id"))  # вывод id
                print("name:", fish.get("name"))  # вывод name
                print("latin_name:", fish.get("latin_name"))  # вывод latin_name
                print("is_salt_water_fish:", fish.get("is_salt_water_fish"))  # булевое поле
                print("sub_type_count:", fish.get("sub_type_count"))  # количество подвидов
        operations_count += 1  # увеличиваем счетчик операций

    elif choice == "2":  # вывод записи по полю id
        id_input = input("Введите id записи (число): ").strip()  # ввод id
        try:
            id_val = int(id_input)  # преобразуем в число
        except:
            print("Неверный формат id.")  # если ошибка
            continue  # возвращаемся в меню

        found = False  # флаг поиска
        for idx, fish in enumerate(records):  # перебор записей
            if fish.get("id") == id_val:  # если найдено
                print("=============== Найдено ===============")  # заголовок
                print("id:", fish.get("id"))  # вывод id
                print("name:", fish.get("name"))  # вывод name
                print("latin_name:", fish.get("latin_name"))  # вывод latin_name
                print("is_salt_water_fish:", fish.get("is_salt_water_fish"))  # булевое поле
                print("sub_type_count:", fish.get("sub_type_count"))  # подвиды
                print("Позиция в словаре:", idx + 1)  # позиция в списке
                found = True  # отметка найдено
                operations_count += 1  # увеличиваем счетчик операций
                break  # выходим после первого совпадения
        if not found:  # если запись не найдена
            print("=============== Не найдено ===============")  # предупреждение

    elif choice == "3":  # добавление записи
        id_input = input("id (число): ").strip()  # ввод id
        try:
            new_id = int(id_input)  # преобразуем в число
        except:
            print("Неверный формат id. Добавление отменено.")  # предупреждение
            continue  # возвращаемся в меню

        duplicate = False  # проверка дубликата
        for fish in records:  # перебор существующих записей
            if fish.get("id") == new_id:  # если id уже есть
                duplicate = True
                break
        if duplicate:  # если дубликат
            print("Запись с таким id уже существует. Добавление отменено.")  # предупреждение
            continue

        new_name = input("name: ").strip()  # ввод name
        new_latin = input("latin_name: ").strip()  # ввод latin_name

        is_salt_input = input("is_salt_water_fish (y/n): ").strip().lower()  # ввод булевого значения
        if is_salt_input in ("y", "yes", "д", "да"):  # проверка
            new_is_salt = True
        else:
            new_is_salt = False

        sub_input = input("sub_type_count (число): ").strip()  # ввод подвидов
        try:
            new_sub = int(sub_input)  # преобразуем
        except:
            print("Неверный формат sub_type_count. Использовано 0.")  # предупреждение
            new_sub = 0

        new_record = {  # создаем новый словарь
            "id": new_id,
            "name": new_name,
            "latin_name": new_latin,
            "is_salt_water_fish": new_is_salt,
            "sub_type_count": new_sub
        }  # конец словаря

        records.append(new_record)  # добавляем в список

        try:
            with open(filename, "w", encoding="utf-8") as f:  # сохраняем в файл
                json.dump(records, f, ensure_ascii=False, indent=4)
            operations_count += 1  # увеличиваем счетчик операций
            print("Запись добавлена.")  # уведомление
        except:
            print("Ошибка при сохранении файла.")  # предупреждение

    elif choice == "4":  # удаление записи по полю id
        id_input = input("Введите id записи для удаления: ").strip()  # ввод id
        try:
            del_id = int(id_input)  # преобразуем
        except:
            print("Неверный формат id.")  # предупреждение
            continue

        found = False  # флаг удаления
        for idx, fish in enumerate(records):  # перебор
            if fish.get("id") == del_id:  # если нашли
                del records[idx]  # удаляем
                try:
                    with open(filename, "w", encoding="utf-8") as f:  # сохраняем
                        json.dump(records, f, ensure_ascii=False, indent=4)
                    operations_count += 1  # увеличиваем счетчик
                    print("Запись удалена.")  # уведомление
                except:
                    print("Ошибка при сохранении файла.")  # предупреждение
                found = True
                break
        if not found:  # если не нашли
            print("=============== Не найдено ===============")  # предупреждение

    elif choice == "5":  # выход из программы
        print("Количество выполненных операций с записями:", operations_count)  # выводим счетчик
        break  # выходим из цикла

    else:  # неверный ввод
        print("Неверный выбор, введите номер от 1 до 5.")  # предупреждение

print("end code …")  # конец кода