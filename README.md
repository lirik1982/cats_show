# Тестовое задание на Python Developer:

#### Стек: Django, DRF, PostgreSQL, JWT, Swagger, Docker, Pytest  
#### Цель задания: Спроектировать REST API онлайн-выставки котят

<br><br>                                                 
### 🛠️ Для установки и запуска сервиса, нужно выполнить следующие действия:

- склонируйте текущий репозиторий в локальную папку и выполните команду:
 ```cmd
    git clone https://github.com/lirik1982/cats_show.git
```
- из командной строки выполните команду развертывания докер-контейнера:
```cmd
    docker-compose up -d
```
 - сервис готов к обработке запросов, и содержит стартовый набор фикстур - породы, участники, кошки и оценки 

#### <font color="pink">-В корне проекта имеется файл cats-show.postman_collection.json, содержащий экспорт команд Postman для работы с сервисом</font>

<br><br>                      	
### API имеет следующие эндпоинты:
1) Получение списка пород
```cmd
  localhost:8000/cats/breedlist/
```
2) Получение списка всех котят
```cmd
  localhost:8000/cats/
```
3) Получение списка котят определенной породы по фильтру.  
```cmd
   localhost:8000/cats/?breed=1
```
4) Получение подробной информации о котенке.
```cmd
   localhost:8000/cats/3/
```
5) Добавление информации о котенке
```cmd
   localhost:8000/cats/
```
6) Изменение информации о котенке
```cmd
   localhost:8000/cats/3/
```
7) Удаление информации о котенке
```cmd
   localhost:8000/cats/3/
```
8) Поставить оценку котенку 
```cmd
   localhost:8000/cats/2/rate/
```
9) #### Swagger-документация доступна по ссылке
```cmd
  http://localhost:8000/swagger/
```

### Команда для запуска pytest-автотестов из командной строки 
```cmd
  pytest
```


## Порядок работы
- выполните запрос о регистрации участника, например
```cmd
curl --location 'localhost:8000/auth/register/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "reade10@mail.ru",
    "password": "!Qwerty1",
    "username": "tester10"
}'
```

- выполните запрос о выдаче токена (авторизации), например
```cmd
curl --location 'localhost:8000/auth/login/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "!Qwerty1",
    "username": "tester10"
}'
```

- выполните запрос на получение доступных пород кошек, например
```cmd
curl --location 'localhost:8000/cats/breedlist/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTAsImV4cCI6MTcyNzk1NDU5MX0.u9znAslYlX183lq_OtTB9fuo3KrxKObTZQ0MrZx4I5I'
```

- выполните запрос на регистрацию кошки, например
```cmd
curl --location 'localhost:8000/cats/' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
    "name": "Мурка2",
    "breed": 1,
    "age": 15,
    "color": "серый",
    "description": "Отличный экстерьер"

}'
```

- выполните запрос на получение списка кошек, например
```cmd
curl --location 'localhost:8000/cats/?breed=1' \
--header 'breed: 2' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTIsImV4cCI6MTcyNzk3NDE5MH0.Ms5EkO8ZB35aLJHMbsgw2T01UGUBcISZdUolxi4x53Y' \
--data ''
```

- выполните запрос на обнавление данных о своей кошке, например
```cmd
curl --location --request PATCH 'localhost:8000/cats/3/' \
--header 'Content-Type: application/json' \
--header 'Authorization: ••••••' \
--data '{
    "name": "Маркиз"
}'
```
- есть возможность удалить данные о своей кошке, например
```cmd
curl --location --request DELETE 'localhost:8000/cats/3/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTAsImV4cCI6MTcyNzk1NDU5MX0.u9znAslYlX183lq_OtTB9fuo3KrxKObTZQ0MrZx4I5I' \
--data ''
```

- есть возможность поставить оценку другим кошкам, например
```cmd
curl --location 'localhost:8000/cats/2/rate/' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTEsImV4cCI6MTcyNzk1Njg3Nn0.fjN6h8ILUVFd1JLVNgGczTX4zi6C6JJprptzDbIS_NY' \
--data '{
    "rating": 5
}'
```
- посмотреть данные о кошке, например
```cmd
curl --location 'localhost:8000/cats/3/' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTIsImV4cCI6MTcyNzk3NjIxOX0.lyjift_1vyIn65TV_13eu9Js22a-lf5f4oLGW5P4ChM'
```


 

