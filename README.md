Задание:
-------

Приложение, которое по REST принимает запрос вида:

POST api/v1/wallets/<WALLET_UUID>/operation

{
        "operationType": "DEPOSIT",
        "amount": 1000
}

{
        "operationType": "WITHDRAW",
        "amount": 1000
}

после выполнять логику по изменению счета в базе данных

также есть возможность получить баланс кошелька

GET api/v1/wallets/{WALLET_UUID}

стек:
Django,
Postgresql

* Предусмотрите соблюдение формата ответа для заведомо неверных запросов, когда
кошелька не существует, не валидный json, или недостаточно средств.
* Приложение должно запускаться в докер контейнере, база данных тоже, вся система
должна подниматься с помощью docker-compose
* Предусмотрите возможность настраивать различные параметры приложения и базы
данных без пересборки контейнеров.
* Эндпоинты должны быть покрыты тестами.

Запуск Docker
------

```
git clone https://github.com/7nmw/Wallet_Rest_api.git
docker-compose up -d
```

Если вам нужен доступ к админке Django, создайте суперпользователя:
```
docker-compose exec web python manage.py createsuperuser
```

Запуск тестов в контейнере:
```
docker-compose exec web python manage.py test
```
Использованы переменные окружения в файле .env

Главная страница: http://localhost:8000/


Сервис
------

* `admin/` - Админка
* `api/v1/wallets/<uuid:wallet_uuid>/operation` - Операции DEPOSIT or WITHDRAW
* `api/v1/wallets/<uuid:wallet_uuid>` - Можно получить баланс кошелька
