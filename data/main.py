import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN
from database import Database
from models import Student


class Registration(StatesGroup):
    last_name = State()
    first_name = State()
    middle_name = State()
    birth_date = State()
    phone = State()
    email = State()
    group_name = State()
    major = State()
    course = State()
    study_form = State()


class RegistrationBot:
    def __init__(self):
        self.bot = Bot(token=BOT_TOKEN)
        self.dp = Dispatcher(storage=MemoryStorage())
        self.db = Database()
        self.student = Student()
        self.register_handlers()

    def register_handlers(self):
        self.dp.message.register(self.start, CommandStart())
        self.dp.message.register(self.get_last_name, Registration.last_name)
        self.dp.message.register(self.get_first_name, Registration.first_name)
        self.dp.message.register(self.get_middle_name, Registration.middle_name)
        self.dp.message.register(self.get_birth_date, Registration.birth_date)
        self.dp.message.register(self.get_phone, Registration.phone)
        self.dp.message.register(self.get_email, Registration.email)
        self.dp.message.register(self.get_group_name, Registration.group_name)
        self.dp.message.register(self.get_major, Registration.major)
        self.dp.message.register(self.get_course, Registration.course)
        self.dp.message.register(self.get_study_form, Registration.study_form)

    async def start(self, message: Message, state: FSMContext):
        if self.db.student_exists(message.from_user.id):
            await message.answer("Вы уже зарегистрированы!")
            return

        await message.answer("Введите вашу фамилию:")
        await state.set_state(Registration.last_name)

    async def get_last_name(self, message: Message, state: FSMContext):
        self.student.set_field("last_name", message.text)
        await message.answer("Введите имя:")
        await state.set_state(Registration.first_name)

    async def get_first_name(self, message: Message, state: FSMContext):
        self.student.set_field("first_name", message.text)
        await message.answer("Введите отчество:")
        await state.set_state(Registration.middle_name)

    async def get_middle_name(self, message: Message, state: FSMContext):
        self.student.set_field("middle_name", message.text)
        await message.answer("Введите дату рождения:")
        await state.set_state(Registration.birth_date)

    async def get_birth_date(self, message: Message, state: FSMContext):
        self.student.set_field("birth_date", message.text)
        await message.answer("Введите номер телефона:")
        await state.set_state(Registration.phone)

    async def get_phone(self, message: Message, state: FSMContext):
        self.student.set_field("phone", message.text)
        await message.answer("Введите email:")
        await state.set_state(Registration.email)

    async def get_email(self, message: Message, state: FSMContext):
        self.student.set_field("email", message.text)
        await message.answer("Введите группу:")
        await state.set_state(Registration.group_name)

    async def get_group_name(self, message: Message, state: FSMContext):
        self.student.set_field("group_name", message.text)
        await message.answer("Введите направление подготовки:")
        await state.set_state(Registration.major)

    async def get_major(self, message: Message, state: FSMContext):
        self.student.set_field("major", message.text)
        await message.answer("Введите курс:")
        await state.set_state(Registration.course)

    async def get_course(self, message: Message, state: FSMContext):
        self.student.set_field("course", message.text)
        await message.answer("Введите форму обучения:")
        await state.set_state(Registration.study_form)

    async def get_study_form(self, message: Message, state: FSMContext):
        self.student.set_field("study_form", message.text)

        data_tuple = self.student.get_data_tuple(message.from_user.id)
        self.db.add_student(data_tuple)

        await message.answer("Регистрация успешно завершена!")
        await state.clear()

    async def run(self):
        await self.dp.start_polling(self.bot)


if __name__ == "__main__":
    bot = RegistrationBot()
    asyncio.run(bot.run())
