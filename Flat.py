import flet as ft import json from datetime import datetime

class TodoApp:

def __init__(self, page: ft.Page):
    self.page = page
    self.page.title = "TODO Планировщик"
    self.page.window_width = 500
    self.page.window_height = 700

    self.tasks = []

    self.build_ui()

# ---------------- UI ----------------
def build_ui(self):

    self.task_input = ft.TextField(label="Задача", width=300)

    self.priority = ft.Dropdown(
        label="Приоритет",
        width=200,
        options=[
            ft.dropdown.Option("Высокий"),
            ft.dropdown.Option("Средний"),
            ft.dropdown.Option("Низкий"),
        ],
    )

    self.deadline = ft.TextField(label="Дедлайн (YYYY-MM-DD HH:MM)", width=300)

    self.search = ft.TextField(label="Поиск", width=300, on_change=self.search_tasks)

    add_btn = ft.ElevatedButton("Добавить", on_click=self.add_task)
    save_btn = ft.ElevatedButton("Сохранить", on_click=self.save_tasks)

    self.stats = ft.Text("Всего: 0 | Выполнено: 0")

    self.task_list = ft.Column()

    self.page.add(
        ft.Text("Планировщик задач", size=20, weight="bold"),
        self.task_input,
        self.priority,
        self.deadline,
        add_btn,
        save_btn,
        self.search,
        self.stats,
        self.task_list
    )

# ---------------- Добавление ----------------
def add_task(self, e):

    if not self.task_input.value or not self.priority.value:
        return

    task = {
        "title": self.task_input.value,
        "priority": self.priority.value,
        "done": False,
        "deadline": self.deadline.value
    }

    self.tasks.append(task)

    self.task_input.value = ""
    self.priority.value = None
    self.deadline.value = ""

    self.update_tasks()
    self.page.update()

# ---------------- Список ----------------
def update_tasks(self, filtered=None):

    self.task_list.controls.clear()

    tasks = filtered if filtered is not None else self.tasks

    done_count = 0

    for index, task in enumerate(tasks):

        if task["done"]:
            done_count += 1

        color = "black"

        if task["priority"] == "Высокий":
            color = "red"
        elif task["priority"] == "Средний":
            color = "orange"
        elif task["priority"] == "Низкий":
            color = "green"

        # проверка дедлайна
        if task["deadline"]:
            try:
                dl = datetime.strptime(task["deadline"], "%Y-%m-%d %H:%M")
                if datetime.now() > dl and not task["done"]:
                    self.page.dialog = ft.AlertDialog(title=ft.Text("Дедлайн прошел!"))
                    self.page.dialog.open = True
            except:
                pass

        task_row = ft.Row(
            [
                ft.Checkbox(
                    value=task["done"],
                    on_change=lambda e, i=index: self.toggle_done(i)
                ),
                ft.Text(
                    f"[{task['priority']}] {task['title']} ({task['deadline']})",
                    color=color
                ),
                ft.IconButton(
                    icon=ft.Icons.DELETE,
                    on_click=lambda e, i=index: self.delete_task(i)
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        self.task_list.controls.append(task_row)

    self.stats.value = f"Всего: {len(self.tasks)} | Выполнено: {sum(t['done'] for t in self.tasks)}"

# ---------------- Галочка ----------------
def toggle_done(self, index):
    self.tasks[index]["done"] = not self.tasks[index]["done"]
    self.update_tasks()
    self.page.update()

# ---------------- Удаление ----------------
def delete_task(self, index):
    self.tasks.pop(index)
    self.update_tasks()
    self.page.update()

# ---------------- Поиск ----------------
def search_tasks(self, e):
    query = self.search.value.lower()
    filtered = [t for t in self.tasks if query in t["title"].lower()]
    self.update_tasks(filtered)
    self.page.update()

# ---------------- Сохранение ----------------
def save_tasks(self, e):
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    self.page.snack_bar = ft.SnackBar(ft.Text("Сохранено"))
    self.page.snack_bar.open = True
    self.page.update()

def main(page: ft.Page): TodoApp(page)

if name == "main": ft.app(target=main)
