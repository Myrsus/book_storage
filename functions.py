import database as db


def create_book():
    name = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = input("Введите год: ")
    description = input("Введите описание: ")
    genre = input("Введите жанр книги: ")
    if not is_input_valid(name, author, year, genre,description):  # проверка на валидность
        return
    db.create_game(name, author,year,genre,description)
    print("✅✅✅Ваша книга успешно создана")

def send_menu():
    print("_____________________________________\n"
          "Основное меню:\n"
          "1) Добавить книгу\n"
          "2) Поиск книги\n"
          "3) Управление книгой\n"
          '_____________________________________')
    ans = ""
    while ans.isdigit() == False:
        ans = input("Выберите пункт меню: ")
    return int(ans)

def send_search_menu(name,publisher,year,genre):
    print("_____________________________________\n"
          "Меню поиска:\n"
          f"1) Имя: {name}\n"
          f"2) Автор: {publisher}\n"
          f"3) Год: {year}\n"
          f"4) Жанр: {genre}\n"
          f"5) Назад\n"
          '_____________________________________')
    ans = ""
    while ans.isdigit() == False:
        ans = input("Выберите пункт меню: ")
    return int(ans)

def send_refactor_menu(game_id):
    data = db.get_game(game_id)
    if data is None:
        print("Был введен неправильный ID")
        return 6
    print("_____________________________________\n"
          "Управление книгой:\n"
          f"1) Изменить Имя: {data.name}\n"
          f"2) Изменить Издатель: {data.author}\n"
          f"3) Изменить Год: {data.year}\n"
          f"4) Изменить Жанр: {data.genre}\n"
          f"5) Удалить\n"
          "6) Назад\n"
          '_____________________________________')
    ans = ""
    while ans.isdigit() == False:
        ans = input("Выберите пункт меню: ")
    return int(ans)

def is_input_valid(name=None, author=None, year=0, genre=None,descriprion=None):
    if str(year).isdigit() == False:
        print("❌❌❌Год должен быть числом")
        return False
    if name == '':
        print("❌❌❌Вы не ввели имя")
        return False
    if author == '':
        print("❌❌❌Вы не ввели издателя")
        return False
    if genre == '':
        print("❌❌❌Вы не ввели жанр")
        return False
    if descriprion == '':
        print("❌❌❌Вы не ввели описание")
        return False
    return True

def books_to_text(datas: list):
    text = '📖📖📖Книги по вашим фильтрам📖📖📖\n'
    for data in datas:
        text+=f"______________________\n" \
              f"ID: {data.id}\n" \
              f"Название: {data.name}\n" \
              f"Автор: {data.author}\n" \
              f"Год: {data.year}\n" \
              f"Жанр: {data.genre}\n" \
              f"Описание:\n" \
              f"{data.description}\n"
    text += '\n☝️☝️☝️Книги по вашем фильтрам☝️☝️☝️'
    return text