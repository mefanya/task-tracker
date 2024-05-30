import pytest

from src.task import Task
from src.user import User


@pytest.fixture
def first_user():
    return User(
        username="Mefanya",
        email="Mefanya@gmail.com",
        first_name="Mikhail",
        last_name="Soldatov",
        task_list=[
            Task("Прыгнуть с паращютом", "Для крутых эмоций"),
            Task("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз")
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
            Task("Искупаться в реке", "Челлендж"),
            Task("Искупаться в море", "Первый заплыв"),
            Task("Нырнуть с акволангом", "Интересные ощущения")
        ]
    )


@pytest.fixture
def task():
    return Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="1.08.2024")
