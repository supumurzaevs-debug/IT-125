from abc import ABC, abstractmethod

#1
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass

class CreditCardPayment:
    def pay(self, amount):
        print (f"Произошла Оплата {amount} сом с кредитной карты выполнена.")

    def refund(self, amount):
        print (f"Произошел Возврат {amount} сом с кредитной карты выполнен.")

class CryptoPayment:
    def pay(self, amount):
        print (f"Произошла Оплата {amount} сом с крипто кошелька выполнена")

    def refund(self, amount):
        print (f"Произошел Возврат {amount} сом с крипто кошелька выполнен.")

payments = [ CreditCardPayment(), CryptoPayment()]

print("Выполнение оплат")
for p in payments:
    p.pay(1500)

print("Выполнение возратов")
for p in payments:
    p.refund(500)


#2
class courses(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def get_materials(self):
        pass
    @abstractmethod
    def end(self):
        pass
    
class PythonCourse:
    def __str__(self):
        return "Python"
    
    def start(self):
        print (f"Вы Успешно начали курс {self}")

    def get_materials(self):
        print (f"Вы Получили учебный материал {self}")

    def end (self):
        print (f"Вы Успешно прошли курс {self}")

class MathCourse:
     def __str__(self):
        return "Math"
     
     def start(self):
        print (f"Вы Успешно начали курс {self}")

     def get_materials(self):
        print (f"Вы Получили учебный материал {self}")

     def end (self):
        print (f"Вы Успешно прошли курс {self}")

lessons = [ PythonCourse(), MathCourse()]

print("Начало обучения")
for l in lessons:
    l.start()

print("Получение учебных материалов")
for l in lessons:
    l.get_materials()

print("Завершение обучения")
for l in lessons:
    l.end()


#3
class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass
    @abstractmethod
    def deliver(self):
        pass

class AirDelivery:
    def calculate_cost(self, distance):
        return distance * 10.5
    def deliver(self):
        print("Доставка самолётом выполнена.")

class GroundDelivery:
    def calculate_cost(self, distance):
        return distance * 3.2
    def deliver(self):
        print("Доставка грузовиком выполнена.")

class SeaDelivery:
    def calculate_cost(self, distance):
        return distance * 5.8
    def deliver(self):
        print("Доставка морем выполнена.")

deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]

print("Доставка товаров")
for d in deliveries:
    print(f"{d.__class__.__name__} стоимость: {d.calculate_cost(1200)}")
    d.deliver()


#4
class BankAccount:
    def __init__(self, owner, pin, balance=0):
        self.__owner = owner
        self.__pin = pin
        self.__balance = balance

    def deposit(self, amount, pin):
        if pin != self.__pin:
            print("Неверный PIN")
            return
        if amount <= 0:
            print("Сумма должна быть положительной")
            return
        self.__balance += amount
        print(f"Баланс после пополнения: {self.__balance}")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Неверный PIN")
            return
        if amount > self.__balance:
            print("Недостаточно средств")
            return
        self.__balance -= amount
        print(f"Баланс после снятия: {self.__balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("Старый PIN неверен")
            return
        self.__pin = new_pin
        print("PIN успешно изменён")

account = BankAccount("Иван", 1234, 1000)
account.deposit(500, 1234)
account.withdraw(200, 1234)
account.change_pin(1234, 4321)


#5
class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "Бесплатный"

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            print("Вход выполнен")
            return True
        else:
            print("Неверный логин или пароль")
            return False

    def upgrade_to_premium(self):
        self._status = "Премиум"
        print("Статус обновлён")

    def get_info(self):
        return f"Email: {self.__email}, Статус: {self._status}"

user = UserProfile("test@mail.com", "qwerty")
if user.login("test@mail.com", "qwerty"):
    user.upgrade_to_premium()
print(user.get_info())


#6
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0

    def set_discount(self, discount, is_admin=False):
        if not is_admin:
            print("Нет прав для установки скидки")
            return
        self.__discount = discount

    def get_price(self):
        return self.price * (1 - self.__discount / 100)

product = Product("Ноутбук", 100000)
product.set_discount(10, is_admin=True)
print(f"Цена со скидкой: {product.get_price()}")


#7
class TextFile:
    def open(self):
        print("Открыт текстовый файл")

class ImageFile:
    def open(self):
        print("Открыт графический файл")

class AudioFile:
    def open(self):
        print("Открыт аудиофайл")

files = [TextFile(), ImageFile(), AudioFile()]

print("Открытие файлов")
for f in files:
    f.open()


#8
class Car:
    def move(self, distance):
        speed = 80
        print(f"Машина проедет {distance} км за {distance/speed:.2f} часов")

class Truck:
    def move(self, distance):
        speed = 60
        print(f"Грузовик проедет {distance} км за {distance/speed:.2f} часов")

class Bicycle:
    def move(self, distance):
        speed = 20
        print(f"Велосипед проедет {distance} км за {distance/speed:.2f} часов")

transports = [Car(), Truck(), Bicycle()]

print("Симуляция транспорта")
for t in transports:
    t.move(120)

#9
class Student:
    def access_portal(self):
        print("Студент: просмотр расписания")

class Teacher:
    def access_portal(self):
        print("Преподаватель: выставление оценок")

class Administrator:
    def access_portal(self):
        print("Администратор: управление пользователями")

users = [Student(), Teacher(), Administrator()]

print("Доступ к порталу")
for u in users:
    u.access_portal()