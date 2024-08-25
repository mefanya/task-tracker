import pytest

from src.task import Task
from src.user import User
from src.task_iterator import TaskIterator
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask


@pytest.fixture
def first_user():
    return User(
        username="Mefanya",
        email="Mefanya@gmail.com",
        first_name="Mikhail",
        last_name="Soldatov",
        task_list=[
            Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="31.05.2024", run_time=600),
            Task("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз", created_at="31.05.2024", run_time=300)
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
    return Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="1.08.2024", run_time=60)


@pytest.fixture
def task_with_runtime1():
    return Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="25.11.2025", run_time=3600)


@pytest.fixture
def task_with_runtime2():
    return Task("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз", created_at="25.07.2025", run_time=2400)


@pytest.fixture
def task_iterator(second_user):
    return TaskIterator(second_user)


@pytest.fixture
def task_periodic1():
    return PeriodicTask("Прыгнуть с паращютом", "Для крутых эмоций", "26.11.2025", "30.12.2025",  created_at="25.11.2025", run_time=3600)


@pytest.fixture
def task_periodic2():
    return PeriodicTask("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз", "26.08.2025", "30.12.2025",  created_at="25.11.2025", run_time=3600)


@pytest.fixture
def task_deadline1():
    return DeadlineTask("Прыгнуть с паращютом", "Для крутых эмоций", "30.12.2025",  created_at="25.11.2025", run_time=3600)


@pytest.fixture
def task_deadline2():
    return DeadlineTask("Прыгнуть с тарзанки", "Для крутых эмоций, но только один раз", "30.12.2025",  created_at="25.11.2025", run_time=3600)


@pytest.fixture
def user_without_tests():
    return User(
        username="Misha",
        email="Misha@gmail.com",
        first_name="Misha",
        last_name="Pupkin")
