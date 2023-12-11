import database as db
import functions as func


def main_menu():
    while True:
        answer = func.send_menu()  # Отправка меню и получение на него ответа
        match answer:
            case 1:
                 func.create_book()
            case 2:
                search_menu()
            case 3:
                game_id = input("Введите ID книги: ")
                if game_id.isdigit() == False:
                    print("Введите число")
                    continue
                update_menu(int(game_id))


def search_menu():
    name = ''
    author = ''
    year = ''
    genre = ''
    while True:
        books = db.search_game(name,author,year,genre) # Звбираем все книги по заданным параметрам из дб
        print(func.books_to_text(books)) #отправляем эти книги красивым текстом
        answer = func.send_search_menu(name,author,year,genre) # Отправка меню и получение на него ответа

        # проверка введенных значений и сброс их до стандарта в случае ошибки
        match answer:
            case 1:
                name = input("Введите имя: ")
                if not(func.is_input_valid(name=name)):
                    name = ''
            case 2:
                author = input("Введите автора: ")
                if not(func.is_input_valid(author=author)):
                    author = ''
            case 3:
                year = input("Введите год: ")
                if not(func.is_input_valid(year=year)):
                    year = ''
            case 4:
                genre = input("Введите жанр: ")
                if not(func.is_input_valid(genre=genre)):
                    genre = ''
            case 5:
                break

def update_menu(game_id: int):
    while True:
        answer = func.send_refactor_menu(game_id)  # Отправка меню и получение на него ответа
        match answer:
            case 1:
                new_name = input("Введите новое имя: ")
                if not(func.is_input_valid(name=new_name)):  # проверка введенных значений
                    continue
                db.update_book_name(game_id,new_name)
            case 2:
                new_author = input("Введите нового издателя: ")
                if not(func.is_input_valid(author=new_author)):  # проверка введенных значений
                    continue
                db.update_book_author(game_id, new_author)
            case 3:
                new_year = input("Введите новый год: ")
                if not(func.is_input_valid(year=new_year)):  # проверка введенных значений
                    continue
                db.update_book_year(game_id, int(new_year))
            case 4:
                new_genre = input("Введите новый жанр: ")
                if not(func.is_input_valid(genre=new_genre)):  # проверка введенных значений
                    continue
                db.update_book_genre(game_id, new_genre)
            case 5:
                db.delete_book(game_id)
                print("✅✅✅Книга удалена")
                break
            case 6:
                break


if __name__ == '__main__':
    main_menu()