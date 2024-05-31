import pytest

from src.task import Task
from src.user import User
from src.task_iterator import TaskIterator


@pytest.fixture
def first_user():
    return User(
        username="Mefanya",
        email="Mefanya@gmail.com",
        first_name="Mikhail",
        last_name="Soldatov",
        task_list=[
            Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="31.05.2024"),
            Task("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз", created_at="31.05.2024")
        ]
    )


@pytest.fixture
def second_user():
    return User(
        username="Johny",
        email="Johny@gmail.com",
        first_name="John",
        last_name="Smit",
        task_list=[
            Task("Искупаться в реке", "Челлендж", created_at="31.05.2024"),
            Task("Искупаться в море", "Первый заплыв", created_at="31.05.2024"),
            Task("Нырнуть с акволангом", "Интересные ощущения", created_at="31.05.2024")
        ]
    )


@pytest.fixture
def task():
    return Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="1.08.2024")


@pytest.fixture
def task_with_runtime1():
    return Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="25.11.2025", run_time=3600)


@pytest.fixture
def task_with_runtime2():
    return Task("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз", created_at="25.07.2025", run_time=2400)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)
