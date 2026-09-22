# Task Manager API

Небольшой REST API для управления задачами на FastAPI.

Проект поддерживает создание, просмотр, закрытие и удаление задач. Данные хранятся в PostgreSQL через SQLAlchemy. Для проверки API используются автоматические тесты на Pytest.

## Возможности

- получение списка задач;
- создание новых задач;
- закрытие существующих задач;
- удаление задач;
- автоматическая валидация данных через Pydantic;
- интерактивная документация Swagger UI и ReDoc;
- интеграционные тесты API через Pytest;
- запуск приложения и базы данных через Docker Compose.

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

Dockerfile
docker-compose.yml
pytest.ini
requirements.txt
README.md
```

## API Endpoints

| Метод | Endpoint | Описание |
|---------|---------|---------|
| GET | `/tasks` | Получить все задачи |
| POST | `/tasks` | Создать задачу |
| PUT | `/tasks/{task_id}` | Закрыть задачу |
| DELETE | `/tasks/{task_id}` | Удалить задачу |

Все endpoints доступны через Swagger:
```text
http://localhost:8000/docs
```

## Запуск через Docker

Собрать и запустить контейнеры:

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

Создать базу данных PostgreSQL:

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

## Примеры запросов

### Получить список задач

```http
GET /tasks
```

Пример ответа:

```json
[
  {
    "id": 1,
    "title": "Изучить FastAPI",
    "is_closed": false
  }
]
```

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

## Тестирование

Запуск тестов:

```bash
pytest
```

Текущий набор тестов проверяет:

- получение списка задач;
- создание задачи;
- закрытие задачи;
- удаление задачи;
- закрытие несуществующей задачи;
- удаление несуществующей задачи;
- валидацию пустого запроса.

Пример результата:

```text
collected 7 items

tests/test_tasks.py .......

7 passed
```

## Полученные навыки

- разработка REST API на FastAPI;
- работа с PostgreSQL через SQLAlchemy ORM;
- контейнеризация приложения с Docker;
- настройка Docker Compose;
- тестирование API через Pytest;
- работа со Swagger/OpenAPI;
- организация проекта через routers, schemas и CRUD слой.


## Автор

Мустафа Муратов

Pet-проект для изучения Python Backend Development.