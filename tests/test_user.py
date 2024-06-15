import pytest


def test_user_init(first_user, second_user):
    assert first_user.username == "Mefanya"
    assert first_user.email == "Mefanya@gmail.com"
    assert len(first_user.task_in_list) == 2
    assert first_user.first_name == "Mikhail"
    assert first_user.last_name == "Soldatov"

    assert second_user.username == "Johny"
    assert second_user.email == "Johny@gmail.com"
    assert len(second_user.task_in_list) == 3
    assert second_user.first_name == "John"
    assert second_user.last_name == "Smit"

    assert first_user.users_count == 3
    assert second_user.users_count == 3

    assert first_user.all_tasks_count == 7
    assert second_user.all_tasks_count == 7


def test_user_task_list_property(first_user):
    assert (first_user.task_list ==
            ("Прыгнуть с паращютом, Статус выполнения: Ожидает старта, Дата создания: 31.05.2024"
             "\nПрыгнуть с тарзанки, Статус выполнения: Ожидает старта, Дата создания: 31.05.2024\n"))


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3


def test_task_str(task):
    assert str(task) == "Прыгнуть с паращютом, Статус выполнения: Ожидает старта, Дата создания: 1.08.2024"


def test_task_add(task_with_runtime1, task_with_runtime2):
    assert task_with_runtime2 + task_with_runtime1 == 6000


def test_task_iterator(task_iterator):
    iter(task_iterator)
    assert task_iterator.index == 0
    assert next(task_iterator).name == "Искупаться в реке"
    assert next(task_iterator).name == "Искупаться в море"
    assert next(task_iterator).name == "Нырнуть с акволангом"

    with pytest.raises(StopIteration):
        next(task_iterator)


def test_user_task_list_user_error(first_user, task):
    with pytest.raises(TypeError):
        first_user.task_list = 1
