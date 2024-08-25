from src.task import Task
from src.exceptions import ZeroRunTimeTask


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f"{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}"

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{str(task)}\n"

        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):
            try:
                if task.run_time == 0:
                    raise ZeroRunTimeTask("Нельзя создать задачу с нулевым временем выполнения")
            except ZeroRunTimeTask as exception:
                print(str(exception))
            else:
                self.__task_list.append(task)
                User.all_tasks_count += 1
                print("Задача добавлена успешно")
            finally:
                print("Обработка входных данных завершена")
        else:
            raise TypeError

    @property
    def task_in_list(self):
        return self.__task_list

    def average_task_completion_time(self):
        try:
            return sum([task.run_time for task in self.__task_list])/len(self.__task_list)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    task1 = Task("Купить огурцы", "Для салатика")
    task2 = Task("Купить помидоры", "Для салатика второго")
    task3 = Task("Купить редис", "Для желудка")
    task4 = Task("Купить морковь", "Для зрения")

    user = User("Mefanya", "mefanya@gmail.com", "Mikhail", "Soldatov", [task1, task2, task3, task4])

    print(user.username)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)

    print(user.users_count)
    print(user.all_tasks_count)

    task5 = Task("Купить молоко", "Купить молоко для кота")
    user.task_list = task5

    print(user.task_list)
    print(user.all_tasks_count)

    print(user)