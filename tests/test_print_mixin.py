from src.task import Task
from src.periodic_task import PeriodicTask
from src.deadline_task import DeadlineTask


def test_print_mixin(capsys):
    Task("Прыгнуть с паращютом", "Для крутых эмоций", created_at="1.08.2024")
    massage = capsys.readouterr()
    assert massage.out.strip() == "Task(Прыгнуть с паращютом, Для крутых эмоций, Ожидает старта, 1.08.2024)"

    PeriodicTask("Прыгнуть с паращютом", "Для крутых эмоций", "26.11.2025", "30.12.2025", created_at="25.11.2025",
                 run_time=3600)
    massage = capsys.readouterr()
    assert massage.out.strip() == "PeriodicTask(Прыгнуть с паращютом, Для крутых эмоций, Ожидает старта, 25.11.2025)"

    DeadlineTask("Прыгнуть с паращютом", "Для крутых эмоций", "30.12.2025", created_at="25.11.2025", run_time=3600)
    massage = capsys.readouterr()
    assert massage.out.strip() == "DeadlineTask(Прыгнуть с паращютом, Для крутых эмоций, Ожидает старта, 25.11.2025)"
