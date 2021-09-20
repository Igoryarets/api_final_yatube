## Описание:

В этом проекте реализован API с помощью Django REST Framework для Yatube. 
Перечислю все доступные эндпоинты и возможные запросы к ним:

1. api/v1/posts/                            (GET, POST: получение и создание публикаций)
2. api/v1/posts/{id}/                       (GET, PUT, PATCH, DELETE: получение, обновление, частичное обновление, удаление публикации )
3. api/v1/groups/                           (GET: получение списка сообществ)
4. api/v1/groups/{id}/                      (GET: получение конкретного сообщества)
5. api/v1/posts/{post_id}/comments/         (GET, POST: получение, создание комментариев)
6. api/v1/posts/{post_id}/comments/{id}/    (GET, PUT, PATCH, DELETE получение, обновление, частичное обновление, удаление комментария к публикации)
7. api/v1/follow/                           (GET, POST: получение, создание подписки)
8. api/v1/users/                            (регистрация нового пользователя)
9. api/v1/jwt/create/                       (создание JWT-токена для конкретного пользователя)
10. api/v1/jwt/refresh/                     (получение нового JWT токена по истечении времени жизни ранее сгенерированного токена)

Для создания, удаления, обновления постов, комментариев, операции по подписке на определенного пользователя и отписки, пользователь должен быть аутентифицирован.

Безопасные запросы c методом GET доступны по всем эндпоинтам кроме api/v1/follow/. 


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Igoryarets/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение (для Windows):

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Обновление менеджера пакетов pip

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
## Примеры запросов к API:

### Регистрация пользователя:

Post запрос на api/v1/users/ 

в теле запроса передаем:
```
{
    "username": "user_1",
    "password": "password_1"
}
```
ответ:
```
{
    "email": "",
    "username": "user_1",
    "id": 4
}
```
### Получение JWT токена:

Post запрос на api/v1/jwt/create/

в теле запроса передаем:
```
{
    "username": "user_1",
    "password": "password_1"
}
```
ответ:
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMjIyMjQzMywianRpIjoiODhkYjU3MmQzNmY2NDlmMmI0YzNlYjg3MzAxZTczNGEiLCJ1c2VyX2lkIjo0fQ.JMBrHFOUmXsf5hNI5MSJoX1GCGtV4hChVQLFVbE9L2k",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMyMjIyNDMzLCJqdGkiOiI1MDBjNjU3NjQwOWM0ZGZiODAzNmI3Mzk3YjRlZWM5YSIsInVzZXJfaWQiOjR9.FrdAum5zJmGGjxhHxjvZ0HzrtUTVy4PhBSp7sphtnuo"
}
```
токен передается в поле access


### Создание поста:

Post запрос на api/v1/posts/

в теле запроса передаем:
```
{
    "text": "text_post"
}
```
ответ:
```
{
    "id": 1,
    "author": "author_1",
    "text": "text_post",
    "pub_date": "2021-09-20T11:11:37.957689Z",
    "image": null,
    "group": null
} 
```
### Создание комментария:

Post запрос на api/v1/posts/{post_id}/comments/

в теле запроса передаем:
```
{
    "text": "text_post_comment",
    "post": "1"
}
```
ответ:
```
{
    "id": 1,
    "author": "author_1",
    "text": "text_post_comment",
    "created": "2021-09-20T11:33:11.884710Z",
    "post": 1
}
```
### Создание подписки:

Post запрос на api/v1/follow/

в теле запроса передаем:
```
{
    "following": "author_1"
}
```
ответ (author_2 подписался на author_1):
```
{
    "user": "author_2",
    "following": "author_1"
}
```