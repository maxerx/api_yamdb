#### YaMDb | REST API Service 

# Описание:
Проект YaMDb собирает отзывы пользователей на фильмы, музыку, книги (произведения)

Пользователя могут публиковать отзывы на произведения, оценивать их от 1 до 10 и обсуждать отзывы в комментариях

Средний рейтинг каждого произведения рассчитывается автоматически

Список категорий и жанров определен администратором, будет расширен в будущем.

# Ключевые особенности:
- Регистрация пользователей происходит путем отправки проверочного кода на e-mail
- Кастомные пользовательские роли: пользователь, модератор, админ
- Кастомная фильтрация по жанру и категориям
- Кастомная аутентификация по JWT токену

# Технологии и библиотеки:
- [Python](https://www.python.org/);
- [Django](https://www.djangoproject.com);
- [SQLite3](https://www.sqlite.org/index.html);
- [Simple-JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/);
- [Django REST Framework](https://www.django-rest-framework.org).

# Как запустить проект:

Клонируйте репозиторий:
```
git clone github.com/maxerx/api_yamdb
```

Измените свою текущую рабочую дерикторию:
```
cd /api_yamdb/
```

Создайте и активируйте виртуальное окружение (версия Python 3.7.9)

```
python -3.7 -m venv venv
```

```
source venv/scripts/activate
```

Обновите pip:
```
python3 -m pip install --upgrade pip
```

Установите зависимости из requirements.txt:

```
pip install -r requirements.txt
```

Создайте миграции:

```
python manage.py migrate
```
Запустите сервер:

```
python manage.py runserver
```
Полная документация прокта (redoc) доступна по адресу http://127.0.0.1:8000/redoc/


## Как зарегистрировать пользователя
1. Сделайте POST запрос, укаказав в теле "username" и "email" на эндпоинт "api/v1/auth/signup/"
2. YaMDb отправит проверочный код на указанный email 
3. Сделайте POST запрос указав "email" и "confirmation_code" в теле запроса на эндпоинт  "api/v1/auth/token/"/,в ответе вы получите JWT-токен


## API YaMDb ресурсы:
- AUTH: Аутентификация.
- USERS: Регистрация пользователей/редактирование информации
- TITLES: Произведения и информация о них
- CATEGORIES: Категории произведений (фильмы, музыка, книги)
- GENRES: Жанры. Одно произведение может иметь несколько жанров
- REVIEWS: Отзывы на произведения. Каждый отзыв относится к определенному произведению.
- COMMENTS: Комментарии к отзывам на произведения.


##### Авторы (команда проекта "Group_project_45"):
- [Мокрушин Илья](https://github.com/maxerx) (Тим-лид, разработчик 1)

- [Паневская Анастасия](https://github.com/AnastasiaPanevskaya) (разработчик 2)

- [Фёдоров Сергей Евгеньевич](https://github.com/Nemets87) (разработчик 3)
