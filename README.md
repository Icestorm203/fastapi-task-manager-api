# Task Manager API

REST API для управления задачами на FastAPI.

Проект позволяет регистрировать пользователей, выполнять аутентификацию через JWT, создавать и управлять личными задачами. Данные хранятся в PostgreSQL через SQLAlchemy ORM. Для управления схемой базы данных используются миграции Alembic. Для проверки работоспособности API используются автоматические тесты на Pytest. Проект контейнеризирован с помощью Docker и имеет настроенный CI через GitHub Actions.

---

## Возможности

- регистрация пользователей;
- аутентификация через JWT;
- авторизация защищённых маршрутов;
- получение списка собственных задач;
- создание новых задач;
- закрытие существующих задач;
- удаление задач;
- изоляция задач между пользователями;
- валидация входных данных через Pydantic;
- миграции базы данных через Alembic;
- автоматическая генерация Swagger/OpenAPI документации;
- интеграционные тесты через Pytest;
- запуск приложения и базы данных через Docker Compose;
- healthcheck PostgreSQL для корректного запуска контейнеров;
- автоматический запуск тестов через GitHub Actions (CI).

---

## Стек

- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- Psycopg2
- Alembic
- Pydantic
- python-jose (JWT)
- Passlib
- Pytest
- Docker
- Docker Compose
- GitHub Actions

---

## Архитектура

Проект организован по слоям:

- `routers` — HTTP endpoints;
- `schemas` — модели запросов и ответов;
- `crud` — работа с базой данных;
- `models` — SQLAlchemy модели;
- `auth` — JWT-аутентификация и авторизация;
- `database` — подключение к PostgreSQL.

---

## Структура проекта

```text
app/
├── __init__.py
├── auth.py              # JWT, хеширование паролей
├── crud.py              # операции с БД
├── database.py          # подключение к PostgreSQL
├── main.py              # точка входа FastAPI
├── models.py            # SQLAlchemy-модели
├── schemas.py           # Pydantic-схемы
└── routers/
    ├── auth.py          # регистрация и логин
    └── tasks.py         # маршруты задач

alembic/
├── env.py
├── script.py.mako
└── versions/
    └── bfd731055e9c_initial.py

tests/
└── test_tasks.py

.github/
└── workflows/
    └── tests.yml

Dockerfile
docker-compose.yml
alembic.ini
pytest.ini
requirements.txt
README.md
```

---

## API Endpoints

| Метод | Endpoint | Описание |
|---------|---------|---------|
| POST | `/register` | Регистрация пользователя |
| POST | `/login` | Получение JWT-токена |
| GET | `/tasks` | Получить свои задачи |
| POST | `/tasks` | Создать задачу |
| PUT | `/tasks/{task_id}` | Закрыть задачу |
| DELETE | `/tasks/{task_id}` | Удалить задачу |

---

## Authentication

Для работы с маршрутом `/tasks` необходимо пройти аутентификацию.

### Регистрация

```http
POST /register
```

Тело запроса:

```json
{
  "username": "mustafa",
  "password": "123456"
}
```

---

### Получение JWT-токена

```http
POST /login
```

Тело запроса:

```json
{
  "username": "mustafa",
  "password": "123456"
}
```

Ответ:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

### Swagger Authorize

После получения JWT:

1. Открыть Swagger UI.
2. Нажать кнопку `Authorize`.
3. Вставить полученный `access_token`.
4. Выполнить авторизацию.

После этого маршруты `/tasks` будут доступны.

---

## Безопасность

- пароли пользователей хранятся в виде хешей;
- аутентификация выполняется через JWT-токены;
- защищённые маршруты требуют авторизации;
- пользователь имеет доступ только к собственным задачам.

---

## Swagger документация

После запуска проекта документация доступна по адресам:

```text
Swagger UI:
http://localhost:8000/docs

ReDoc:
http://localhost:8000/redoc
```

---

## Запуск через Docker

Собрать и запустить приложение:

```bash
docker compose up --build
```

После запуска будут доступны:

```text
API:
http://localhost:8000

Swagger UI:
http://localhost:8000/docs

ReDoc:
http://localhost:8000/redoc
```

Остановить контейнеры:

```bash
docker compose down
```

Остановить контейнеры с удалением volumes:

```bash
docker compose down -v
```

Посмотреть работающие контейнеры:

```bash
docker ps
```

Посмотреть логи:

```bash
docker compose logs -f
```

---

## Локальный запуск

Клонировать репозиторий:

```bash
git clone https://github.com/<your-username>/fastapi-task-manager-api.git

cd fastapi-task-manager-api
```

Создать виртуальное окружение:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать PostgreSQL базу данных:

```text
Database: fastapi_tasks
User: postgres
Password: postgres
Host: localhost
Port: 5432
```

Применить миграции:

```bash
alembic upgrade head
```

Запустить приложение:

```bash
uvicorn app.main:app --reload
```

---

## Работа с миграциями

Создать новую миграцию:

```bash
alembic revision --autogenerate -m "migration_name"
```

Применить миграции:

```bash
alembic upgrade head
```

Посмотреть текущую версию:

```bash
alembic current
```

История миграций:

```bash
alembic history
```

Откатить последнюю миграцию:

```bash
alembic downgrade -1
```

---

## Примеры запросов

### Получить список задач

```http
GET /tasks
```

Ответ:

```json
[
  {
    "id": 1,
    "title": "Изучить FastAPI",
    "is_closed": false,
    "user_id": 1
  }
]
```

---

### Создать задачу

```http
POST /tasks
```

Тело запроса:

```json
{
  "title": "Изучить FastAPI"
}
```

Ответ:

```json
{
  "id": 1,
  "title": "Изучить FastAPI",
  "is_closed": false,
  "user_id": 1
}
```

---

### Закрыть задачу

```http
PUT /tasks/1
```

Ответ:

```json
{
  "id": 1,
  "title": "Изучить FastAPI",
  "is_closed": true,
  "user_id": 1
}
```

---

### Удалить задачу

```http
DELETE /tasks/1
```

Ответ:

```json
{
  "message": "Task deleted"
}
```

---

## Тестирование

Запуск тестов:

```bash
pytest
```

Текущий набор тестов покрывает:

- получение JWT-токена для доступа к API;
- получение списка задач;
- создание задачи;
- закрытие задачи;
- удаление задачи;
- обработку отсутствующей задачи (404);
- проверку авторизации;
- валидацию входных данных (422).

Пример результата:

```text
collected 8 items

tests/test_tasks.py ........

8 passed
```

---

## CI/CD

Для проекта настроен GitHub Actions.

После каждого:

```bash
git push
```

автоматически выполняются:

- установка зависимостей;
- запуск PostgreSQL;
- применение миграций Alembic;
- запуск тестов Pytest.

При успешном прохождении тестов workflow получает статус:

```text
✅ Success
```

---

## Полученные навыки

В рамках проекта были изучены и применены:

- разработка REST API на FastAPI;
- работа с PostgreSQL;
- использование SQLAlchemy ORM;
- управление версиями схемы БД через Alembic;
- JWT-аутентификация и авторизация пользователей;
- хеширование паролей через Passlib;
- разграничение доступа пользователей к данным;
- валидация данных через Pydantic;
- контейнеризация приложения с Docker;
- настройка Docker Compose;
- настройка Healthcheck в Docker Compose;
- написание интеграционных тестов на Pytest;
- документирование API через Swagger/OpenAPI;
- организация проекта через routers, schemas и CRUD слой;
- настройка непрерывной интеграции через GitHub Actions.

---

## Автор

Мустафа Муратов

Pet-проект для изучения Python Backend Development.