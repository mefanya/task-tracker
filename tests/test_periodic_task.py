import pytest


def test_periodic_task_init(task_periodic1):
    assert task_periodic1.name == "Прыгнуть с паращютом"
    assert task_periodic1.description == "Для крутых эмоций"
    assert task_periodic1.start_date == "26.11.2025"
    assert task_periodic1.end_date == "30.12.2025"
    assert task_periodic1.created_at == "25.11.2025"
    assert task_periodic1.status == "Ожидает старта"
    assert task_periodic1.frequency == "Ежедневная"
    assert task_periodic1.run_time == 3600


def test_periodic_task_add(task_periodic1, task_periodic2):
    assert task_periodic1 + task_periodic2 == 7200


def test_periodic_task_add_error(task_periodic1):
    with pytest.raises(TypeError):
        result = task_periodic1 + 1
