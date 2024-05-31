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

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 5
    assert second_user.all_tasks_count == 5


def test_user_task_list_property(first_user):
    assert (first_user.task_list ==
            ("Прыгнуть с паращютом, Статсус выполнения: Ожидает старта, Дата создания: 31.05.2024"
             "\nПрыгнуть с тарзанки, Статсус выполнения: Ожидает старта, Дата создания: 31.05.2024\n"))


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3
