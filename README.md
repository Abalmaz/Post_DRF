# Post_DRF

## Функционал:
1. Просматриваьб посты и категории могут все пользователи
2. Создавать посты могут только аутентифицированные пользователи
3. Редактировать и удалять посты может только автор
4. Создавать/редактировать/удалять категории мошут только пользователи is_staff

## Запуск:
### Создание БД:
1. flask db init
2. flask db migrate
3. flask db upgrade
### Запуск приложения
flask run

| Methods | URI | Action |
|---------|-----|--------|
|GET| http://127.0.0.1:8000/api/post| Show post list (for all users)|
|POST| http://127.0.0.1:8000/api/post| Create new post, model:{"title": string, "category": string, "content": string}, just for authorized user, user by default is current user|
|GET| http://127.0.0.1:8000/api/post/{id}| Show post detail|
|PATCH| http://127.0.0.1:8000/api/post/{id}|Partial update post, just for author of post|
|DELETE| http://127.0.0.1:8000/api/post/{id}| Delete post, just for author of post|
|GET| http://127.0.0.1:8000/api/category| Show category list (for all users)|
|POST| http://127.0.0.1:8000/api/post| Create new category, model:{"description": string, "name": string, "is_active": true}, just for is_staff user|
|GET| http://127.0.0.1:8000/api/category/{id}| Show category detail|
|PATCH| http://127.0.0.1:8000/api/category/{id}|Partial update category, just for is_staff user|
|DELETE| http://127.0.0.1:8000/api/category/{id}| Delete category, just for is_staff user|
|GET| http://127.0.0.1:8000/api/user| Show all users|
|GET| http://127.0.0.1:8000/api/user/id| Show detail by user|
