class Task:
    def __init__(self, description, due_date):
        self.description = description  # Описание задачи
        self.due_date = due_date  # Срок выполнения
        self.completed = False  # Статус задачи (по умолчанию не выполнена)

    def mark_completed(self):
        """Отмечает задачу как выполненную."""
        self.completed = True

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, description, due_date):
        """Добавляет новую задачу."""
        task = Task(description, due_date)
        self.tasks.append(task)

    def complete_task(self, description):
        """Отмечает задачу как выполненную по её описанию."""
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                break

    def show_current_tasks(self):
        """Выводит список текущих (не выполненных) задач."""
        print("Текущие задачи:")
        for task in self.tasks:
            if not task.completed:
                print(task)


# Пример использования
task_manager = TaskManager()
task_manager.add_task("Купить продукты", "2023-10-15")
task_manager.add_task("Сделать домашнее задание", "2023-10-10")
task_manager.add_task("Позвонить другу", "2023-10-12")

task_manager.complete_task("Сделать домашнее задание")

task_manager.show_current_tasks()