# Task Manager API

Небольшой REST API для управления задачами на FastAPI. Проект поддерживает создание, просмотр, закрытие и удаление задач. Данные хранятся в PostgreSQL через SQLAlchemy.

## Возможности

- получить список задач;
- создать задачу;
- закрыть задачу;
- удалить задачу;
- автоматически открыть интерактивную документацию Swagger и ReDoc.

## Стек

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- PostgreSQL
- Pytest

## Структура проекта

```text
app/
├── main.py              # точка входа FastAPI
├── database.py          # подключение к PostgreSQL
├── models.py            # SQLAlchemy-модели
├── schemas.py           # Pydantic-схемы
├── crud.py              # операции с задачами
└── routers/
		└── tasks.py         # endpoints задач
tests/
└── test_tasks.py        # тесты API
```

## Установка

Клонируйте репозиторий и перейдите в его директорию:

```bash
git clone https://github.com/<your-username>/fastapi-task-manager-api.git
cd fastapi-task-manager-api
```

Создайте виртуальное окружение и установите зависимости:

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

```bash
pip install -r requirements.txt
```

## Настройка PostgreSQL

Создайте базу данных `fastapi_tasks` в PostgreSQL. Текущая конфигурация приложения ожидает следующие параметры:

```text
Хост: localhost
Порт: 5432
Пользователь: postgres
Пароль: postgres
База данных: fastapi_tasks
```

Например, командой `createdb`:

```bash
createdb -U postgres fastapi_tasks
```

Таблица `tasks` создаётся автоматически при запуске приложения. Если параметры подключения отличаются, измените `DATABASE_URL` в `app/database.py`.

## Запуск

Запустите сервер разработки:

```bash
uvicorn app.main:app --reload
```

После запуска API будет доступен по адресу `http://127.0.0.1:8000`.

Интерактивная документация:

- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API

### Получить все задачи

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

Новая задача создаётся с `is_closed: false`.

### Закрыть задачу

```http
PUT /tasks/{task_id}
```

После успешного запроса поле `is_closed` становится `true`. Если задача не найдена, API возвращает `404 Not Found`.

### Удалить задачу

```http
DELETE /tasks/{task_id}
```

Успешный ответ:

```json
{
	"message": "Task deleted"
}
```

Если задача не найдена, API возвращает `404 Not Found`.

## Тестирование

Запустите тесты из корневой директории проекта:

```bash
pytest
```

Тесты используют то же подключение к PostgreSQL, что и приложение, поэтому перед запуском убедитесь, что база данных доступна.
