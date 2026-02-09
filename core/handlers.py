import asyncio
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.quiz import Quiz
from core.roulette import RussianRouletteGame

class BotHandlers:
    def __init__(self, bot):
        self.router = Router()
        self.bot = bot
        self.quiz = Quiz()
        self.user_data = {}
        self.roulette_games = {}  # хранит игру и состояние
        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_quiz, Command("quiz"))
        self.router.message.register(self.start_roulette, Command("roulette"))
        self.router.message.register(self.shoot_roulette, Command("shoot"))
        self.router.message.register(self.stop_roulette, Command("stop"))
        self.router.callback_query.register(self.handle_answer)

    # --- Команды викторины ---
    async def start_command(self, message: types.Message):
        await message.answer("Привет 👋\nНапиши /quiz чтобы начать викторину 🎯 или напиши /roulette чтобы начать игру")

    async def start_quiz(self, message: types.Message):
        user_id = message.from_user.id
        self.user_data[user_id] = {"score": 0, "q_index": 0}
        await self.send_question(message.chat.id, user_id)

    async def send_question(self, chat_id, user_id):
        data = self.user_data[user_id]
        question_data = self.quiz.get_question(data["q_index"])
        if not question_data:
            await self.finish_quiz(chat_id, user_id)
            return

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=opt, callback_data=opt)]
                             for opt in question_data["options"]]
        )
        await self.bot.send_message(chat_id, question_data["question"], reply_markup=keyboard)

    async def handle_answer(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data = self.user_data.get(user_id)
        if not data:
            await callback.answer("Сначала начни викторину через /quiz")
            return

        question_data = self.quiz.get_question(data["q_index"])
        if callback.data == question_data["correct"]:
            data["score"] += 1
        data["q_index"] += 1
        await callback.answer("Ответ принят!")
        await self.send_question(callback.message.chat.id, user_id)

    async def finish_quiz(self, chat_id, user_id):
        score = self.user_data[user_id]["score"]
        total = self.quiz.total_questions()
        await self.bot.send_message(chat_id, f"🏁 Викторина окончена!\nТвой результат: {score} из {total}")
        del self.user_data[user_id]

    # --- Рулетка ---
    async def start_roulette(self, message: types.Message):
        player = message.from_user.id
        game = RussianRouletteGame()

        # сохраняем игру
        self.roulette_games["game"] = {
            "game": game,
            "players": [player, "player2"],
            "current": 0,
            "timer_task": None
        }

        await message.answer(f"Игра началась!\nПервый ход за {player}\nНажми /shoot чтобы стрелять!")

        # запускаем таймер первого игрока
        await self.start_timer(message)

    async def start_timer(self, message: types.Message):
        """Запуск таймера 5 сек для текущего игрока"""
        game_data = self.roulette_games.get("game")
        if not game_data:
            return

        current_player = game_data["players"][game_data["current"]]

        # отменяем предыдущий таймер, если есть
        if game_data.get("timer_task"):
            game_data["timer_task"].cancel()

        # создаём новую задачу
        async def timeout():
            await asyncio.sleep(5)
            # игрок не успел — проиграл
            await message.answer(f"{current_player} не успел стрелять за 5 секунд 💥 проиграл!")
            del self.roulette_games["game"]

        game_data["timer_task"] = asyncio.create_task(timeout())

    async def shoot_roulette(self, message: types.Message):
        game_data = self.roulette_games.get("game")
        if not game_data:
            await message.answer("Сначала запусти игру через /roulette")
            return

        result = game_data["game"].shoot()
        current_player = game_data["players"][game_data["current"]]

        # если был таймер — отменяем
        if game_data.get("timer_task"):
            game_data["timer_task"].cancel()
            game_data["timer_task"] = None

        if result == 'click':
            await message.answer(f'{current_player} стреляет — пусто! 🎯')
            # меняем игрока
            game_data["current"] = 1 - game_data["current"]
            next_player = game_data["players"][game_data["current"]]
            await message.answer(f"Ход за {next_player}!")
            # запускаем таймер следующего игрока
            await self.start_timer(message)

        elif result == 'boom':
            await message.answer(f'{current_player} стреляет — 💥 проиграл! Игра окончена!')
            del self.roulette_games["game"]

    async def stop_roulette(self, message: types.Message):
        game_data = self.roulette_games.get("game")
        if not game_data:
            await message.answer("Игра не запущена!")
            return

        # отменяем таймер
        if game_data.get("timer_task"):
            game_data["timer_task"].cancel()

        score = game_data["game"].stop()
        await message.answer(f"Ты остановил игру принудительно! Ваши очки - {score}")
        del self.roulette_games["game"]
