import datetime
from src.task import Task


def test_task_init(task):
    assert task.name == "Прыгнуть с паращютом"
    assert task.description == "Для крутых эмоций"
    assert task.status == "Ожидает старта"
    assert task.created_at == "1.08.2024"


def test_task_create():
    task = Task("Купить билеты", "Купить билеты на самолет")

    assert task.name == "Купить билеты"
    assert task.description == "Купить билеты на самолет"
    assert task.status == "Ожидает старта"
    assert task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')


def test_task_update(capsys, task):
    task.created_at = '24.04.2024'
    message = capsys.readouterr()
    assert message.out.strip() == "Нельзя изменить дату создания на дату из прошлого"

    task.created_at = datetime.datetime.now().date().strftime('%d.%m.%Y')
    assert task.created_at == datetime.datetime.now().date().strftime('%d.%m.%Y')
