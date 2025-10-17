import json  # модуль для работы с JSON-файлами

# выводим начало программы
print("start code...")

# открываем и считываем данные из файла dump.json
with open("dump.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# пользователь вводит номер квалификации
code = input("Введите номер квалификации: ")

# создаём флаг, чтобы знать — нашли ли что-то
found = False

# проходим по всем объектам в файле
for item in data:
    # ищем только те, где model == "data.skill"
    if item.get("model") == "data.skill":
        # получаем словарь с полями квалификации
        fields = item.get("fields", {})

        # если код совпадает с введённым
        if fields.get("code") == code:
            found = True
            print("=============== Найдено ===============")

            # выводим информацию в нужном формате
            print(f"{fields.get('code')} >> Квалификация \"{fields.get('name')}\"")

            # ищем связанный объект специальности, если есть
            specialty_code = fields.get("specialty_code")
            if specialty_code:
                print(f"{specialty_code} >> Специальность \"{fields.get('specialty_name')}\", {fields.get('education_level')}")
            break  # прекращаем цикл, если нашли

# если ничего не найдено
if not found:
    print("=============== Не найдено ===============")

# выводим конец программы
print("end code...")