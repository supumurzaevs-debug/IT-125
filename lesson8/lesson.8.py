from abc import ABC, abstractmethod
import math

# 1 задание: Account
class Account:
    def __init__(self, account_number, balance, pin):
        self.__account_number = account_number
        self.__balance = float(balance)
        self.__pin = str(pin)
    def deposit(self, amount, pin):
        if str(pin) != self.__pin:
            return "PIN неверный"
        if amount <= 0:
            return "Сумма должна быть положительной"
        self.__balance += amount
        return f"Пополнение успешно. Баланс: {self.__balance}"
    def withdraw(self, amount, pin):
        if str(pin) != self.__pin:
            return "PIN неверный"
        if amount <= 0:
            return "Сумма должна быть положительной"
        if amount > self.__balance:
            return "Недостаточно средств"
        self.__balance -= amount
        return f"Снятие успешно. Баланс: {self.__balance}"
    def get_balance(self, pin):
        if str(pin) != self.__pin:
            return "PIN неверный"
        return self.__balance

# 2 задание: Product
class Product:
    def __init__(self, price):
        self.__price = float(price)
        self.__discount_percent = 0.0
    def set_discount(self, percent):
        if percent < 0:
            return "Скидка не может быть отрицательной"
        self.__discount_percent = percent
        if self.final_price() < 0:
            self.__discount_percent = 0
            return "Скидка привела бы к отрицательной цене и была отменена"
        return f"Скидка установлена: {self.__discount_percent}%"
    def final_price(self):
        return max(0.0, self.__price * (1 - self.__discount_percent / 100))

# 3 задание: Course
class Course:
    def __init__(self, name, max_seats):
        self.__name = name
        self.__students = []
        self.__max_seats = int(max_seats)
    def add_student(self, name):
        if len(self.__students) >= self.__max_seats:
            return "Мест нет"
        if name in self.__students:
            return "Студент уже записан"
        self.__students.append(name)
        return "Студент добавлен"
    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)
            return "Студент удалён"
        return "Студент не найден"
    def get_students(self):
        return tuple(self.__students)

# 4 задание: SmartWatch
class SmartWatch:
    def __init__(self, battery=65):
        self.__battery = float(battery)
    def use(self, minutes):
        reduction = minutes / 10.0
        self.__battery = max(0.0, self.__battery - reduction)
        return self.__battery
    def charge(self, percent):
        if percent < 0:
            return self.__battery
        self.__battery = min(100.0, self.__battery + percent)
        return self.__battery
    def get_battery(self):
        return self.__battery

# 5 задание: Transport, Bus, Train, Airplane
class Transport:
    def __init__(self, speed, capacity):
        self.speed = float(speed)
        self.capacity = int(capacity)
    def travel_time(self, distance):
        if self.speed <= 0:
            return float('inf')
        return distance / self.speed

class Bus(Transport):
    pass

class Train(Transport):
    pass

class Airplane(Transport):
    def travel_time(self, distance):
        base = super().travel_time(distance)
        return base * 0.8

# 6 задание: Order и подклассы
class Order:
    def __init__(self, items):
        self.items = list(items)
    def subtotal(self):
        return sum(self.items)

class DineInOrder(Order):
    def calculate_total(self):
        sub = self.subtotal()
        tip = sub * 0.12  # чуть большие чаевые
        return sub + tip

class TakeAwayOrder(Order):
    def calculate_total(self):
        return self.subtotal()

class DeliveryOrder(Order):
    def calculate_total(self):
        sub = self.subtotal()
        delivery_fee = 5.0  # фиксированная плата за доставку
        return sub + delivery_fee

# 7 задание: Character, Warrior, Mage, Archer
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack

class Warrior(Character):
    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона мечом"

class Mage(Character):
    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона магией"

class Archer(Character):
    def attack(self):
        return f"{self.name} наносит {self.attack_power} урона стрелой"

# 8 задание: MediaFile, AudioFile, VideoFile, Podcast
class MediaFile:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
    def play(self):
        return f"Воспроизведение: {self.name}"

class AudioFile(MediaFile):
    def play(self):
        return f"{self.name} проигрывается как аудио, длина {self.duration}"

class VideoFile(MediaFile):
    def play(self):
        return f"{self.name} воспроизводится с изображением, длина {self.duration}"

class Podcast(MediaFile):
    def play(self):
        return f"Эпизод подкаста {self.name}, длина {self.duration}"

# 9 задание: PaymentSystem и реализации
class PaymentSystem(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        fee = round(amount * 0.025, 2)  # 2.5% комиссия
        return f"Карта: списано {amount}, комиссия {fee}"

class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        return f"Крипто: транзакция на {amount} отправлена в сеть"

class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        fee = 0
        if amount < 50:
            fee = 2
        return f"Банк: перевёл {amount}, комиссия {fee}"

# 10 задание: Animal и наследники
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        return "Лев жрёт мясо"
    def sleep(self):
        return "Лев дремлет на солнышке"

class Elephant(Animal):
    def eat(self):
        return "Слон хрумкает траву"
    def sleep(self):
        return "Слон отдыхает стоя"

class Snake(Animal):
    def eat(self):
        return "Змея глотает добычу"
    def sleep(self):
        return "Змея свернулась клубком"

# 11 задание: Document и реализации
class Document(ABC):
    @abstractmethod
    def open(self):
        pass
    @abstractmethod
    def edit(self, content):
        pass
    @abstractmethod
    def save(self):
        pass

class WordDocument(Document):
    def __init__(self):
        self.content = ""
    def open(self):
        return "Word открыт"
    def edit(self, content):
        self.content += content
        return "Word обновлён"
    def save(self):
        return "Word сохранён"

class PdfDocument(Document):
    def __init__(self):
        self.content = ""
    def open(self):
        return "PDF открыт"
    def edit(self, content):
        return "PDF нельзя править"
    def save(self):
        return "PDF сохранён"

class SpreadsheetDocument(Document):
    def __init__(self):
        self.content = []
    def open(self):
        return "Таблица открыта"
    def edit(self, content):
        self.content.append(content)
        return "Таблица обновлена"
    def save(self):
        return "Таблица сохранена"

# 12 задание: Lesson и подклассы
class Lesson(ABC):
    @abstractmethod
    def start(self):
        pass

class VideoLesson(Lesson):
    def __init__(self, title):
        self.title = title
    def start(self):
        return f"Запуск видео-урока: {self.title}"

class QuizLesson(Lesson):
    def __init__(self, title):
        self.title = title
    def start(self):
        return f"Включена викторина: {self.title}"

class TextLesson(Lesson):
    def __init__(self, title):
        self.title = title
    def start(self):
        return f"Открыт текстовый урок: {self.title}"

# 13 задание: Notifications
class EmailNotification:
    def send(self, message):
        return f"Письмо отправлено: {message}"

class SMSNotification:
    def send(self, message):
        return f"СМС отправлено: {message}"

class PushNotification:
    def send(self, message):
        return f"Push: {message}"

# 14 задание: Shapes
class Square:
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return self.side * 4

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c

# 15 задание: Employees (Manager, Developer, Designer)
class Manager:
    def work(self):
        return "Менеджер организует задачи"

class Developer:
    def work(self):
        return "Разработчик пишет и тестит код"

class Designer:
    def work(self):
        return "Дизайнер рисует интерфейсы"

# 16 задание: Spells (Fire, Ice, Healing)
class FireSpell:
    def cast(self, target):
        return f"{target}: горение — наносит урон огнём"

class IceSpell:
    def cast(self, target):
        return f"{target}: лед — замедляет и замораживает"

class HealingSpell:
    def cast(self, target):
        return f"{target}: лечит — возвращает здоровье"

# Демонстрация использования всех классов (значения изменены)
if __name__ == "__main__":
    # Account
    a = Account("AC9876", 500, "2468")
    print(a.deposit(150, "2468"))
    print(a.withdraw(75, "2468"))
    print(a.get_balance("2468"))

    # Product
    p = Product(199.99)
    print(p.set_discount(15))
    print(p.final_price())

    # Course
    c = Course("Intro to Py", 3)
    print(c.add_student("Лена"))
    print(c.add_student("Олег"))
    print(c.add_student("Майкл"))
    print(c.add_student("Антон"))  # должно вернуть, что мест нет
    print(c.get_students())

    # SmartWatch
    s = SmartWatch(65)
    print(s.use(45))   # уменьшится на 4.5%
    print(s.charge(25))
    print(s.get_battery())

    # Transport
    b = Bus(50, 40)
    t = Train(100, 150)
    ap = Airplane(900, 220)
    print(b.travel_time(150))
    print(t.travel_time(300))
    print(ap.travel_time(1800))

    # Orders
    d1 = DineInOrder([12.5, 7.5, 20])
    t1 = TakeAwayOrder([6, 4])
    del1 = DeliveryOrder([9.99, 14.01])
    print(d1.calculate_total())
    print(t1.calculate_total())
    print(del1.calculate_total())

    # Characters
    w = Warrior("Коля", 110, 18)
    m = Mage("Аня", 70, 25)
    ar = Archer("Рома", 85, 14)
    print(w.attack())
    print(m.attack())
    print(ar.attack())

    # Media files
    af = AudioFile("Трек", "4:05")
    vf = VideoFile("Клип", "2:30")
    pod = Podcast("Беседа", "27:10")
    print(af.play())
    print(vf.play())
    print(pod.play())

    # Payments
    cc = CreditCardPayment()
    cr = CryptoPayment()
    bt = BankTransfer()
    print(cc.process_payment(120))
    print(cr.process_payment(35))
    print(bt.process_payment(45))

    # Animals
    animals = [Lion(), Elephant(), Snake()]
    for an in animals:
        print(an.eat())
        print(an.sleep())

    # Documents
    wd = WordDocument()
    print(wd.open())
    print(wd.edit("пример текста"))
    print(wd.save())
    pd = PdfDocument()
    print(pd.open())
    print(pd.edit("abc"))
    print(pd.save())
    sd = SpreadsheetDocument()
    print(sd.open())
    print(sd.edit("B2=5"))
    print(sd.save())

    # Lessons
    lessons = [VideoLesson("Урок 1"), QuizLesson("Тест 1"), TextLesson("Чтение")]
    for les in lessons:
        print(les.start())

    # Notifications
    notifications = [EmailNotification(), SMSNotification(), PushNotification()]
    for n in notifications:
        print(n.send("Всем привет"))

    # Shapes
    shapes = [Square(5), Circle(2.5), Triangle(4,5,6)]
    for sh in shapes:
        print(sh.perimeter())

    # Employees
    staff = [Manager(), Developer(), Designer()]
    for person in staff:
        print(person.work())

    # Spells
    spells = [FireSpell(), IceSpell(), HealingSpell()]
    for sp in spells:
        print(sp.cast("Монстр"))
        