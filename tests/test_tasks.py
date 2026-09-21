from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_tasks():

    response = client.get("/tasks")

    assert response.status_code == 200

    data = response.json()

    if data:
        assert "id" in data[0]
        assert "title" in data[0]
        assert "is_closed" in data[0]


def test_create_task():

    response = client.post(
        "/tasks",
        json={
            "title": "Test task"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test task"
    assert data["is_closed"] is False


def test_close_task():

    create_response = client.post(
        "/tasks",
        json={
            "title": "Task for close test"
        }
    )

    task_id = create_response.json()["id"]

    response = client.put(f"/tasks/{task_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == task_id
    assert data["is_closed"] is True


def test_delete_task():

    create_response = client.post(
        "/tasks",
        json={
            "title": "Task for delete test"
        }
    )

    task_id = create_response.json()["id"]

    response = client.delete(
        f"/tasks/{task_id}"
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Task deleted"


def test_close_nonexistent_task():

    response = client.put("/tasks/999999")

    assert response.status_code == 404


def test_delete_nonexistent_task():

    response = client.delete("/tasks/999999")

    assert response.status_code == 404


def test_create_task_empty_title():

    response = client.post(
        "/tasks",
        json={}
    )

    assert response.status_code == 422