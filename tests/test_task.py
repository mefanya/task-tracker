
def test_task_init(task):
    assert task.name == "Прыгнуть с паращютом"
    assert task.description == "Для крутых эмоций"
    assert task.status == "Ожидает старта"
    assert task.created_at == "1.08.2024"
