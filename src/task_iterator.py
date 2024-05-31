from src.task import Task
from src.user import User

class TaskIterator:
    def __init__(self, user_obj):
        self.user = user_obj
        self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.user.task_in_list):
            task = self.user.task_in_list[self.index]
            self.index += 1
            return task
        else:
            raise StopIteration


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Для салатика")
    task2 = Task("Купить помидоры", "Для салатика второго")
    task3 = Task("Купить редис", "Для желудка")
    task4 = Task("Купить морковь", "Для зрения")

    user = User("Mefanya", "mefanya@gmail.com", "Mikhail", "Soldatov", [task1, task2, task3, task4])

    iterator = TaskIterator(user)

    for task in iterator:
        print(task)

    print()

    for task in iterator:
        print(task)
