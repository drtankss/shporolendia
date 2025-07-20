import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Замените на ваш токен бота
BOT_TOKEN = "8119239168:AAG9dAm1rgDX9wBU4L-F6KXJyHe-C3SNsn4"

class ShporolandiaBot:
    def __init__(self):
        # Данные о канале
        self.channel_info = """
🏟️ **Добро пожаловать в Шпороландию!**

Здесь вы найдете:
• Последние новости о клубе
• Анализ матчей и тактики
• Трансферные слухи и подтверждения
• Интервью с игроками
• История клуба и легендарные моменты

**COYS!** (Come On You Spurs!) 🤍💙

Присоединяйтесь к нашему сообществу преданных фанатов Шпор!
        """
        
        # Последние матчи (примерные данные)
        self.recent_matches = [
            {
                "date": "15.07.2025",
                "opponent": "Арсенал",
                "result": "2-1",
                "competition": "Дружеский матч",
                "scorers": "Сон Хын Мин, Мэдисон"
            },
            {
                "date": "12.07.2025", 
                "opponent": "Ливерпуль",
                "result": "1-3",
                "competition": "Дружеский матч",
                "scorers": "Кулушевски"
            },
            {
                "date": "08.07.2025",
                "opponent": "Манчестер Юнайтед", 
                "result": "2-0",
                "competition": "Дружеский матч",
                "scorers": "Ришарлисон, Сон Хын Мин"
            }
        ]
        
        # Расписание матчей
        self.upcoming_matches = [
            {
                "date": "25.07.2025",
                "time": "20:00",
                "opponent": "Челси",
                "competition": "Дружеский матч",
                "venue": "Уэмбли"
            },
            {
                "date": "17.08.2025",
                "time": "17:30", 
                "opponent": "Лестер Сити",
                "competition": "Премьер-лига",
                "venue": "Тоттенхэм Хотспур Стэдиум"
            },
            {
                "date": "24.08.2025",
                "time": "15:00",
                "opponent": "Эвертон",
                "competition": "Премьер-лига", 
                "venue": "Гудисон Парк"
            }
        ]
        
        # Социальные сети
        self.social_media = {
            "telegram": "@tottenham_news_channel",
            "tiktok": "@tottenham_official",
            "admin": "@admin_username",
            "owner": "@owner_username"
        }

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Стартовое сообщение с главным меню"""
        keyboard = [
            [InlineKeyboardButton("🏟️ Про канал", callback_data='channel_info')],
            [InlineKeyboardButton("⚽ Последние матчи", callback_data='recent_matches')],
            [InlineKeyboardButton("📅 Расписание матчей", callback_data='upcoming_matches')],
            [InlineKeyboardButton("📱 Соц. сети", callback_data='social_media')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_text = """
🤍💙 **Добро пожаловать в Шпороландию!** 

Выберите интересующий вас раздел:
        """
        
        await update.message.reply_text(
            welcome_text, 
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def button_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Обработчик нажатий на кнопки"""
        query = update.callback_query
        await query.answer()
        
        if query.data == 'channel_info':
            await self.show_channel_info(query)
        elif query.data == 'recent_matches':
            await self.show_recent_matches(query)
        elif query.data == 'upcoming_matches':
            await self.show_upcoming_matches(query)
        elif query.data == 'social_media':
            await self.show_social_media(query)
        elif query.data == 'back_to_menu':
            await self.show_main_menu(query)

    async def show_channel_info(self, query):
        """Показать информацию о канале"""
        keyboard = [[InlineKeyboardButton("🔙 Назад в меню", callback_data='back_to_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            self.channel_info,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def show_recent_matches(self, query):
        """Показать последние матчи"""
        text = "⚽ **ПОСЛЕДНИЕ МАТЧИ ТОТТЕНХЭМА**\n\n"
        
        for match in self.recent_matches:
            text += f"📅 {match['date']}\n"
            text += f"🆚 Тоттенхэм {match['result']} {match['opponent']}\n"
            text += f"🏆 {match['competition']}\n"
            text += f"⚽ Голы: {match['scorers']}\n\n"
        
        keyboard = [[InlineKeyboardButton("🔙 Назад в меню", callback_data='back_to_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def show_upcoming_matches(self, query):
        """Показать расписание матчей"""
        text = "📅 **РАСПИСАНИЕ МАТЧЕЙ ТОТТЕНХЭМА**\n\n"
        
        for match in self.upcoming_matches:
            text += f"📅 {match['date']} в {match['time']}\n"
            text += f"🆚 Тоттенхэм vs {match['opponent']}\n"
            text += f"🏆 {match['competition']}\n"
            text += f"🏟️ {match['venue']}\n\n"
        
        keyboard = [[InlineKeyboardButton("🔙 Назад в меню", callback_data='back_to_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def show_social_media(self, query):
        """Показать социальные сети"""
        text = f"""
📱 **НАШИ СОЦИАЛЬНЫЕ СЕТИ**

📢 **Telegram канал:** {self.social_media['telegram']}
🎵 **TikTok:** {self.social_media['tiktok']}

👑 **Владелец:** {self.social_media['owner']}
⚙️ **Администратор:** {self.social_media['admin']}

Подписывайтесь на все наши платформы, чтобы не пропустить важные новости о Тоттенхэме! 🤍💙
        """
        
        keyboard = [[InlineKeyboardButton("🔙 Назад в меню", callback_data='back_to_menu')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def show_main_menu(self, query):
        """Показать главное меню"""
        keyboard = [
            [InlineKeyboardButton("🏟️ Про канал", callback_data='channel_info')],
            [InlineKeyboardButton("⚽ Последние матчи", callback_data='recent_matches')],
            [InlineKeyboardButton("📅 Расписание матчей", callback_data='upcoming_matches')],
            [InlineKeyboardButton("📱 Соц. сети", callback_data='social_media')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        welcome_text = """
🤍💙 **Добро пожаловать в Шпороландию!** 

Выберите интересующий вас раздел:
        """
        
        await query.edit_message_text(
            welcome_text,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

def main():
    """Запуск бота"""
    # Создаем экземпляр бота
    bot = ShporolandiaBot()
    
    # Создаем приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    application.add_handler(CommandHandler("start", bot.start))
    application.add_handler(CallbackQueryHandler(bot.button_handler))
    
    # Запускаем бота
    print("🤍💙 Шпороландия запущена! COYS!")
    application.run_polling()

if __name__ == '__main__':
    main()
