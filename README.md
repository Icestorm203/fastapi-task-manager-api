# Task Manager API

REST API для управления задачами на FastAPI.

Проект позволяет создавать, просматривать, закрывать и удалять задачи. Данные хранятся в PostgreSQL через SQLAlchemy ORM. Для проверки работоспособности API используются автоматические тесты на Pytest. Проект контейнеризирован с помощью Docker и имеет настроенный CI через GitHub Actions.

---

## Возможности

- получение списка задач;
- создание новых задач;
- закрытие существующих задач;
- удаление задач;
- валидация входных данных через Pydantic;
- автоматическая генерация Swagger/OpenAPI документации;
- интеграционные тесты через Pytest;
- запуск приложения и базы данных через Docker Compose;
- автоматический запуск тестов через GitHub Actions (CI).

---

## Стек

- Python 3.12
- FastAPI
- Uvicorn
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Docker
- Docker Compose
- GitHub Actions

---

## Структура проекта

```text
app/
├── __init__.py
├── main.py              # точка входа FastAPI
├── database.py          # подключение к PostgreSQL
├── models.py            # SQLAlchemy-модели
├── schemas.py           # Pydantic-схемы
├── crud.py              # операции с БД
└── routers/
    ├── __init__.py
    └── tasks.py         # маршруты API

tests/
└── test_tasks.py        # тесты API

.github/
└── workflows/
    └── tests.yml        # GitHub Actions CI

Dockerfile
docker-compose.yml
pytest.ini
requirements.txt
README.md
```

---

## API Endpoints

| Метод | Endpoint | Описание |
|---------|---------|---------|
| GET | `/tasks` | Получить список задач |
| POST | `/tasks` | Создать задачу |
| PUT | `/tasks/{task_id}` | Закрыть задачу |
| DELETE | `/tasks/{task_id}` | Удалить задачу |

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

Посмотреть работающие контейнеры:

```bash
docker ps
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

Запустить приложение:

```bash
uvicorn app.main:app --reload
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
    "is_closed": false
  }
]
```

---

### Создать задачу

```http
POST /tasks
Content-Type: application/json
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
  "is_closed": false
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
  "is_closed": true
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

- получение списка задач;
- создание задачи;
- закрытие задачи;
- удаление задачи;
- обработку отсутствующей задачи (404);
- валидацию входных данных (422).

Пример результата:

```text
collected 7 items

tests/test_tasks.py .......

7 passed
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
- создание таблиц БД;
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
- валидация данных через Pydantic;
- контейнеризация приложения с Docker;
- настройка Docker Compose;
- написание интеграционных тестов на Pytest;
- документирование API через Swagger/OpenAPI;
- организация проекта через routers, schemas и CRUD слой;
- настройка непрерывной интеграции через GitHub Actions.

---

## Автор

Мустафа Муратов

Pet-проект для изучения Python Backend Development.