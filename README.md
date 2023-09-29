# Руководство по проекту "Сервис для работы с результатами исследований"

Этот проект представляет собой веб-приложение, разработанное для управления и просмотра результатов медицинских исследований, проводимых в лабораториях при исследовательском центре. Ниже приведены основные шаги для начала работы с этим приложением.

## Описание проекта

Проект "Сервис для работы с результатами исследований" предназначен для управления результатами медицинских исследований. В данном проекте используется Django в качестве основной платформы для разработки веб-приложения.

## Workflow(CI)

В этом проекте используется автоматизация с использованием GitHub Actions для запуска тестов (`pytest`) при каждом пуше в ветку `main`. 

Тесты проекта находятся в директории `tests`. Эти тесты позволяют проверить работоспособность приложения и обнаружить возможные ошибки и проблемы.


## Docker Контейнеры

В этом проекте используются Docker контейнеры для развертывания бекенда (Django), веб-сервера (Nginx) и базы данных PostgreSQL с целью обеспечения изолированного и масштабируемого окружения. 

### Docker Контейнер для бекенда

Для бекенда используется контейнер, основанный на образе Python 3.10-slim. Этот контейнер устанавливает необходимые зависимости из файла `requirements.txt` и запускает приложение Django с помощью Gunicorn на порту 8000.

### Docker Контейнер для Nginx
Для веб-сервера Nginx также используется Docker контейнер. Он копирует файл конфигурации nginx.conf, который используется для настройки Nginx, в /etc/nginx/templates/default.conf.template.

### Docker Контейнер для PostgreSQL
База данных PostgreSQL также развертывается в отдельном Docker контейнере. Он использует официальный образ PostgreSQL 14 и настраивает переменные окружения, такие как POSTGRES_USER, POSTGRES_PASSWORD, и POSTGRES_DB.

### Взаимосвязь контейнеров
Контейнеры для бекенда, Nginx и PostgreSQL связаны друг с другом через сеть Docker, чтобы обеспечить взаимодействие между бекендом, веб-сервером и базой данных. Вы можете использовать Docker Compose для управления этой сетью и настройки контейнеров.

## Установка и настройка
<i>Примечание: Все примеры указаны для Mac/Linux</i><br>

1. **Установите Docker и Docker Compose**

2. **Склонируйте репозиторий**: Склонируйте репозиторий с проектом на свой компьютер: 
    ```
    git clone git@github.com:1emd/Lab_Data_Hub.git
    ```
3. **Создайте файл `.env` и заполните его своими данными.**:
    ```     
    Пример:
    POSTGRES_USER=django_user
    POSTGRES_PASSWORD=mysecretpassword
    POSTGRES_DB=django
    DB_HOST=db
    DB_PORT=5432
    ```
4. **Запустите контейнеры**: В корневой папке проекта(Lab_Data_Hub) выполните следующую команду, чтобы запустить контейнеры с использованием Docker Compose:
    ```
    docker compose up 
    ```
Это создаст и запустит контейнеры для вашего проекта.

5. **Примените миграции**: Выполните миграции для создания таблиц в базе данных:
    ```
    - docker compose -f docker-compose.yml exec backend python manage.py makemigrations
    - docker compose -f docker-compose.yml exec backend python manage.py migrate      
    ```

6. **Соберите статические файлы бэкенда**:
    ```
    docker-compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /backend_static/static/
    ```

7. **Создайте суперюзера**:
    ```
    docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
    ```

## Swagger API

Для документации и тестирования API в проекте доступен Swagger UI. После успешного запуска вашего проекта, вы можете открыть Swagger UI в веб-браузере, перейдя по следующему URL:
    ```
    http://127.0.0.1:8000/api/swagger/
    ```

## Пример использования API

### Авторизация пользователя 

**Примечание:** Для полноценной работы с API необходимо создать пользователя (или воспользоваться суперюзером) и получить аутентификационный токен.

1. **Создание пользователя.** 

**Метод**: `POST`
**http://127.0.0.1:8000/api/users/**

**Тело запроса (JSON)**:
```json
{
    "email": "example@example.com",
    "username": "example_user",
    "password": "example_password"
}
```

2. **Введите email и пароль для получения токена.**:

**Метод**: `POST`
**http://127.0.0.1:8000/api/auth/token/login/**

**Тело запроса (JSON)**:
```json
{
    "email": "example@example.com",
    "password": "example_password"
}
```
**Пример ответа (JSON)**:
```json
{
    "auth_token": "35b4af1ca10a8ff3d239e40188ea9fdc617dcf19"
}
```
Данный токен необходим для совершения `POST`, `PUT`, `PATCH`, `DELETE` запросов на другие эндпоинты.

Пример использования в `Postman`:

- В `Postman` выберите вкладку `Headers`.
- В поле `Key` введите `Authorization`.
- В поле `Value` введите `Token <token>`, где `<token>` замените на фактический аутентификационный токен.

### Работа с основными эндпоинтами 

#### URLS проекта:

- **Доступные методы**: GET (получение списка), GET (поиск по ID), POST (создание), PUT (обновление), PATCH (частичное обновление), DELETE (удаление)

**Лаборатории (Labs)**:
   - **URL**: `http://127.0.0.1:8000/api/labs/`
   - **Описание**: Здесь вы можете добавлять и просматривать информацию о лабораториях, в которых проводятся исследования.

**Тесты (Tests)**:
   - **URL**: `http://127.0.0.1:8000/api/tests/`
   - **Описание**: Этот эндпоинт используется для создания записей о медицинских тестах, включая даты начала и завершения.

**Показатели (Indicators)**:
   - **URL**: `http://127.0.0.1:8000/api/indicators/`
   - **Описание**: Здесь можно добавлять информацию о показателях, которые измеряются в ходе медицинских исследований.

**Метрики (Metrics)**:
   - **URL**: `http://127.0.0.1:8000/api/metrics/`
   - **Описание**: Здесь вы можете добавлять и просматривать информацию о метриках, связанных с исследованиями.

**Показатель метрики (Indicator Metric)**:

   - **URL**: `http://127.0.0.1:8000/api/indicator-metrics/`
   - **Описание**: Здесь устанавливаются связи между показателями и метриками.

**Количественные значения (Scores)**:

   - **URL**: `http://127.0.0.1:8000/api/scores/`
   - **Описание**: Этот эндпоинт предназначен для ввода количественных данных, полученных в ходе медицинских исследований. 

**Справки (References)**:

   - **URL**: `http://127.0.0.1:8000/api/references/`
   - **Описание**: Здесь устанавливаются справочные значения, которые используются для сравнения с полученными данными.

**Результаты медицинских исследований (Test Results)**:

   - **URL**: `http://127.0.0.1:8000/api/test-results/`
   - **Описание**: После заполнения информации в вышеперечисленных эндпоинтах, в этом эндпоинте будет доступен результат медицинских исследований. Вы можете также выполнять фильтрацию по ID лаборатории.

Для получения результатов медицинских исследований (`/test-results/`) необходимо заполнить информацию во всех указанных эндпоинтах. Это позволит вам проводить комплексные медицинские анализы и получать точные результаты.

Вы также можете выполнять поиск по ID для **каждого эндпоинта**, используя URL вида: `/api/<endpoint_name>/<item_id>`, где `<endpoint_name>` - имя конкретного эндпоинта, а `<item_id>` - идентификатор объекта.
Пример: `/api/labs/lab_id`, где `lab_id` - это идентификатор конкретной лаборатории.

В `/api/test-results/` доступна возможность фильтрации по ID лабораторий (`lab_id`). Пример: `/api/test-results/?lab_id=<lab_id>`, где `<lab_id>` - идентификатор конкретной лаборатории.

