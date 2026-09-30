APP_TITLE = "Todo Planner"

task = []

run = False
def show_tasks():
    print("Список справ:")
    for i, item in enumerate(task, 1):
        print(f"{i}. {item}")

def clear_tasks():
    task.clear()
    print("Список справ очищено")

while True:
    print("1 - Додати до списку")
    print("2 - Видалити зі списку")
    print("3 - Переглянути список")
    print("0 - Вийти")

    number = int(input("Введіть число: "))
    if number == 1:
        print("Додати до списку")
        task_input = input("Введіть справу для списку: ")
        task.append(task_input)
    elif number == 2:
        print("Видалити зі списку")
        task_number = int(input("Введіть номер справи: "))
        task.pop(task_number - 1)
    elif number == 3:
        show_tasks()
    elif number == 0:
        print("Вийти")
        break
    else:
        break