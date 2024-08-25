from src.task import Task


class PeriodicTask(Task):
    def __init__(self, name, description, start_date, end_date, status="Ожидает старта", created_at=None, run_time=0, frequency="Ежедневная"):
        super().__init__(name, description, status, created_at, run_time)
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency

    def __add__(self, other):
        if type(other) is PeriodicTask:
            return self.run_time + other.run_time
        raise TypeError
