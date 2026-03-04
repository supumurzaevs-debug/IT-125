import tkinter as tk
from tkinter import ttk, messagebox
from dataclasses import dataclass
from typing import List

@dataclass
class Employee:
    name: str
    surname: str
    age: int
    position: str
    salary: float

class EmployeeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Каталог сотрудников")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Список сотрудников
        self.employees: List[Employee] = []
        
        # Создание интерфейса
        self.create_input_form()
        self.create_employee_list()
        
    def create_input_form(self):
        # Основной контейнер для формы
        form_frame = ttk.LabelFrame(self.root, text="Добавление сотрудника", padding=10)
        form_frame.pack(fill="x", padx=10, pady=5)
        
        # Имя
        ttk.Label(form_frame, text="Имя сотрудника:").grid(row=0, column=0, sticky="w", pady=2)
        self.name_entry = ttk.Entry(form_frame, width=30)
        self.name_entry.grid(row=0, column=1, pady=2, padx=5)
        
        # Фамилия
        ttk.Label(form_frame, text="Фамилия:").grid(row=1, column=0, sticky="w", pady=2)
        self.surname_entry = ttk.Entry(form_frame, width=30)
        self.surname_entry.grid(row=1, column=1, pady=2, padx=5)
        
        # Возраст
        ttk.Label(form_frame, text="Возраст:").grid(row=2, column=0, sticky="w", pady=2)
        self.age_entry = ttk.Entry(form_frame, width=30)
        self.age_entry.grid(row=2, column=1, pady=2, padx=5)
        
        # Должность
        ttk.Label(form_frame, text="Должность:").grid(row=3, column=0, sticky="w", pady=2)
        self.position_combo = ttk.Combobox(form_frame, values=["Разработчик", "Дизайнер", "Менеджер", "Тестировщик"], width=27)
        self.position_combo.grid(row=3, column=1, pady=2, padx=5)
        self.position_combo.current(0)
        
        # Зарплата
        ttk.Label(form_frame, text="Зарплата:").grid(row=4, column=0, sticky="w", pady=2)
        self.salary_entry = ttk.Entry(form_frame, width=30)
        self.salary_entry.grid(row=4, column=1, pady=2, padx=5)
        
        # Кнопка добавления
        self.add_button = ttk.Button(form_frame, text="Добавить сотрудника", command=self.add_employee)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Кнопка сортировки
        self.sort_button = ttk.Button(form_frame, text="Сортировать по зарплате", command=self.sort_by_salary)
        self.sort_button.grid(row=6, column=0, columnspan=2, pady=5)
        
    def create_employee_list(self):
        # Контейнер для списка сотрудников
        list_frame = ttk.LabelFrame(self.root, text="Список сотрудников", padding=10)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Заголовки
        headers = ["Имя", "Фамилия", "Возраст", "Должность", "Зарплата", ""]
        for i, header in enumerate(headers):
            ttk.Label(list_frame, text=header, font=("Arial", 10, "bold")).grid(row=0, column=i, padx=5, pady=2, sticky="w")
        
        # Canvas и Scrollbar для прокрутки
        self.canvas = tk.Canvas(list_frame, borderwidth=0, highlightthickness=0)
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.grid(row=1, column=0, columnspan=len(headers), sticky="nsew")
        scrollbar.grid(row=1, column=len(headers), sticky="ns")
        
        list_frame.grid_rowconfigure(1, weight=1)
        list_frame.grid_columnconfigure(0, weight=1)
        
        # Словарь для хранения виджетов сотрудников
        self.employee_widgets = []
        
    def add_employee(self):
        # Получение данных
        name = self.name_entry.get().strip()
        surname = self.surname_entry.get().strip()
        age = self.age_entry.get().strip()
        position = self.position_combo.get()
        salary = self.salary_entry.get().strip()
        
        # Проверка на заполненность полей
        if not all([name, surname, age, salary]):
            messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля")
            return
        
        # Проверка возраста
        try:
            age = int(age)
            if age <= 0 or age > 120:
                messagebox.showerror("Ошибка", "Возраст должен быть положительным числом до 120")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Возраст должен быть числом")
            return
        
        # Проверка зарплаты
        try:
            salary = float(salary)
            if salary < 0:
                messagebox.showerror("Ошибка", "Зарплата должна быть положительным числом")
                return
        except ValueError:
            messagebox.showerror("Ошибка", "Зарплата должна быть числом")
            return
        
        # Создание сотрудника
        employee = Employee(name, surname, age, position, salary)
        self.employees.append(employee)
        
        # Очистка полей
        self.name_entry.delete(0, tk.END)
        self.surname_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        
        # Обновление списка
        self.update_employee_list()
        
        messagebox.showinfo("Успех", "Сотрудник успешно добавлен")
    
    def update_employee_list(self):
        # Очистка старых виджетов
        for widget in self.employee_widgets:
            widget.destroy()
        self.employee_widgets.clear()
        
        # Добавление новых виджетов
        for i, emp in enumerate(self.employees):
            row_frame = ttk.Frame(self.scrollable_frame)
            row_frame.grid(row=i, column=0, sticky="ew", pady=1)
            
            # Данные сотрудника
            ttk.Label(row_frame, text=emp.name, width=10).grid(row=0, column=0, padx=2)
            ttk.Label(row_frame, text=emp.surname, width=10).grid(row=0, column=1, padx=2)
            ttk.Label(row_frame, text=str(emp.age), width=6).grid(row=0, column=2, padx=2)
            ttk.Label(row_frame, text=emp.position, width=12).grid(row=0, column=3, padx=2)
            
            # Подсветка высокой зарплаты
            salary_label = ttk.Label(row_frame, text=f"{emp.salary:.2f}")
            if emp.salary > 100000:
                salary_label.configure(foreground="red", font=("Arial", 10, "bold"))
            salary_label.grid(row=0, column=4, padx=2)
            
            # Кнопка удаления
            delete_btn = ttk.Button(row_frame, text="Удалить", 
                                   command=lambda e=emp: self.delete_employee(e))
            delete_btn.grid(row=0, column=5, padx=5)
            
            self.employee_widgets.append(row_frame)
    
    def delete_employee(self, employee):
        self.employees.remove(employee)
        self.update_employee_list()
        messagebox.showinfo("Успех", "Сотрудник удален")
    
    def sort_by_salary(self):
        # Сортировка по зарплате (от меньшего к большему)
        self.employees.sort(key=lambda x: x.salary)
        self.update_employee_list()

def main():
    root = tk.Tk()
    app = EmployeeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
