import pytest
from server import app



# helper auth header
def auth_header():
    return {"Authorization": "Bearer TEST_TOKEN"}


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/api/accounts/1/tasks",
        json={"title": "Test", "description": "Testing"},
        headers=auth_header()
    )

    assert response.status_code == 201
    body = response.get_json()

    assert body["title"] == "Test"
    assert body["description"] == "Testing"


def test_update_task():
    client = app.test_client()

    # create
    res = client.post(
        "/api/accounts/1/tasks",
        json={"title": "old", "description": "old-desc"},
        headers=auth_header()
    )
    task = res.get_json()

    # update
    patch_res = client.patch(
        f"/api/accounts/1/tasks/{task['id']}",
        json={"title": "new", "description": "new-desc"},
        headers=auth_header()
    )

    assert patch_res.status_code == 200
    updated = patch_res.get_json()

    assert updated["title"] == "new"
    assert updated["description"] == "new-desc"


def test_get_task():
    client = app.test_client()

    res = client.post(
        "/api/accounts/1/tasks",
        json={"title": "findme", "description": "desc"},
        headers=auth_header()
    )
    task = res.get_json()

    get_res = client.get(
        f"/api/accounts/1/tasks/{task['id']}",
        headers=auth_header()
    )

    assert get_res.status_code == 200
    found = get_res.get_json()
    assert found["title"] == "findme"


def test_delete_task():
    client = app.test_client()

    res = client.post(
        "/api/accounts/1/tasks",
        json={"title": "delete", "description": "temp"},
        headers=auth_header()
    )
    task = res.get_json()

    delete_res = client.delete(
        f"/api/accounts/1/tasks/{task['id']}",
        headers=auth_header()
    )

    assert delete_res.status_code == 204

