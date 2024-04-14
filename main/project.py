import logging
import time

import schedule
from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler
from telegram.ext import filters
import time_mini
import words1

application = Application.builder().token('7148131509:AAEN3LjmdH0RlhkSRW3wKfks6qaHb2S1tsI').build()

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


async def hello(update, context):
    await update.message.reply_text(
        'Привет! Я бот-помощник, который может обучить вас новым словам в английском языке!\n'
        'Для продолжения напишите /start\n'
        'Если есть вопросы, нажмите /help')


async def start(update, context):
    global hope_executed
    global hope_executed1
    global hope_executed2
    reply_keyboard = [['Времена'], ['Слова'], ['Тесты по временам']]
    markup = ReplyKeyboardMarkup(reply_keyboard)
    await update.message.reply_text(
        'Выберите, что хотите изучить',
        reply_markup=markup)
    hope_executed = False
    hope_executed1 = False
    hope_executed2 = False


async def help_command(update, context):
    await update.message.reply_text('По всем вопросам: @alex11qqq')


def main():
    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help_command)

    time_handler_1 = MessageHandler(filters.Regex('^(Времена)$'), time_mini.time1)
    time_handler = MessageHandler(filters.Regex('^(Слова)$'), words1.words)
    time_handler_2 = MessageHandler(filters.Regex('^(Тесты по временам)$'), time_mini.test_next1)

    test_next = CommandHandler('next', time_mini.check_tense_1)

    result_time_test = MessageHandler(filters.TEXT, time_mini.check_tense_present_simple)

    result_time = MessageHandler(filters.TEXT, time_mini.result)

    schedule_test = CommandHandler('hop', words1.start_scheduler)

    application.add_handler(start_handler, group=1)
    application.add_handler(help_handler, group=1)

    application.add_handler(time_handler_1, group=2)
    application.add_handler(time_handler, group=2)
    application.add_handler(time_handler_2, group=2)
    application.add_handler(result_time, group=2)

    application.add_handler(test_next, group=3)
    application.add_handler(result_time_test, group=3)

    application.add_handler(schedule_test)

    schedule.every(10).seconds.do(words1.send_message)

    # Запускаем приложение.
    application.run_polling()

    while True:
        schedule.run_pending()
        time.sleep(1)


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
