import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize('book', ['9', 'я', 'Книга_название_которой_состоит_из_40_св.'])
    def test_add_new_book_add_min_and_max_len_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert book in collector.get_books_genre()

    def test_set_book_genre_add_book_and_set_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Фантастика')
        assert collector.get_book_genre('Хоббит') == 'Фантастика'

    def test_get_book_genre_set_unknown_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.set_book_genre('Хоббит', 'Мьюзикл')
        assert collector.get_book_genre('Хоббит') != 'Мьюзикл'

    def test_get_books_with_specific_genre_two_books_1_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Детективы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Детективы')
        assert (collector.get_books_with_specific_genre('Детективы') ==
                ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])

    def test_get_books_genre_add_book_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        assert collector.get_books_genre() == {'Хоббит': ''}

    @pytest.mark.parametrize(
        'book,genre',
        [
            ['Хоббит', 'Фантастика'],
            ['Один дома', 'Комедии'],
            ['История Игрушек','Мультфильмы']
        ]
    )
    def test_get_books_for_children_add_three_book_and_child_genres(self, book, genre):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_for_children() == [book]

    def test_add_book_in_favourites_add_one_favourite_book(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        assert collector.get_list_of_favorites_books() == ['Хоббит']

    def test_delete_book_from_favourites_books_delete_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Хоббит')
        collector.add_book_in_favorites('Хоббит')
        collector.delete_book_from_favorites('Хоббит')
        assert 'Хоббит' not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('book', ['Властелин колец', 'Дети Шпионов', 'Ночной дозор'])
    def test_get_list_of_favourites_books_added_book_not_fav(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        assert collector.get_list_of_favorites_books() == []
