import pytest


def test_deadline_task_init(task_deadline1):
    assert task_deadline1.name == "Прыгнуть с паращютом"
    assert task_deadline1.description == "Для крутых эмоций"
    assert task_deadline1.deadline == "30.12.2025"
    assert task_deadline1.created_at == "25.11.2025"
    assert task_deadline1.status == "Ожидает старта"
    assert task_deadline1.run_time == 3600


def test_deadline_test_add(task_deadline1, task_deadline2):
    assert task_deadline1 + task_deadline2 == 7200


def test_deadline_test_add_error(task_deadline1):
    with pytest.raises(TypeError):
        result = task_deadline1 + 1
