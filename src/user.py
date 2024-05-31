from src.task import Task


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

    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{task.name}, Статсус выполнения: {task.status}, Дата создания: {task.created_at}\n"

        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        self.__task_list.append(task)
        User.all_tasks_count += 1

    @property
    def task_in_list(self):
        return self.__task_list


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
