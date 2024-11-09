# TODO решите задачу
import json


def task(name) -> float:
    # Чтение данных из файла в формате JSON
    with open(name, 'r') as file:
        data = json.load(file)

    total = sum([i["score"] * i["weight"] for i in data])
    return round(total, 3)


print(task('input.json'))
