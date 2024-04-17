import logging

from telegram import ReplyKeyboardMarkup
from telegram.ext import Application, MessageHandler, CommandHandler
from telegram.ext import filters
import time_mini
import words1
import test_time

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
    time_handler_2 = MessageHandler(filters.Regex('^(Тесты по временам)$'), test_time.test_next1)

    test_next = CommandHandler('next', test_time.check_tense_1)
    test_next_1 = CommandHandler('next1', test_time.check_tense_2)
    test_next_2 = CommandHandler('next2', test_time.check_tense_3)
    test_next_3 = CommandHandler('next3', test_time.check_tense_4)
    test_next_4 = CommandHandler('next4', test_time.check_tense_5)
    test_next_5 = CommandHandler('next5', test_time.check_tense_6)
    test_next_6 = CommandHandler('next6', test_time.check_tense_7)
    test_next_7 = CommandHandler('next7', test_time.check_tense_8)
    test_next_8 = CommandHandler('next8', test_time.check_tense_9)
    test_next_9 = CommandHandler('next9', test_time.check_tense_10)
    test_next_10 = CommandHandler('next10', test_time.check_tense_11)
    test_next_11 = CommandHandler('next11', test_time.check_tense_12)

    result_time_test = MessageHandler(filters.TEXT, test_time.check_tense_present_simple)
    result_time_test_1 = MessageHandler(filters.TEXT, test_time.check_tense_past_simple)
    result_time_test_2 = MessageHandler(filters.TEXT, test_time.check_tense_past_perfect_continuous)
    result_time_test_3 = MessageHandler(filters.TEXT, test_time.check_tense_future_simple)
    result_time_test_4 = MessageHandler(filters.TEXT, test_time.check_tense_past_continuous)
    result_time_test_5 = MessageHandler(filters.TEXT, test_time.check_tense_past_perfect)
    result_time_test_6 = MessageHandler(filters.TEXT, test_time.check_tense_future_perfect)
    result_time_test_7 = MessageHandler(filters.TEXT, test_time.check_tense_future_perfect_continuous)
    result_time_test_8 = MessageHandler(filters.TEXT, test_time.check_tense_present_perfect_continuous)
    result_time_test_9 = MessageHandler(filters.TEXT, test_time.check_tense_present_perfect)
    result_time_test_10 = MessageHandler(filters.TEXT, test_time.check_tense_future_continuous)
    result_time_test_11 = MessageHandler(filters.TEXT, test_time.check_tense_present_continuous)

    result_time = MessageHandler(filters.TEXT, time_mini.result)

    application.add_handler(start_handler, group=1)
    application.add_handler(help_handler, group=1)

    application.add_handler(time_handler_1, group=2)
    application.add_handler(time_handler, group=2)
    application.add_handler(time_handler_2, group=2)
    application.add_handler(result_time, group=2)

    application.add_handler(test_next, group=5)
    application.add_handler(result_time_test, group=5)

    application.add_handler(test_next_1, group=6)
    application.add_handler(result_time_test_1, group=6)

    application.add_handler(test_next_2, group=7)
    application.add_handler(result_time_test_2, group=7)

    application.add_handler(test_next_3, group=8)
    application.add_handler(result_time_test_3, group=8)

    application.add_handler(test_next_4, group=9)
    application.add_handler(result_time_test_4, group=9)

    application.add_handler(test_next_5, group=10)
    application.add_handler(result_time_test_5, group=10)

    application.add_handler(test_next_6, group=11)
    application.add_handler(result_time_test_6, group=11)

    application.add_handler(test_next_7, group=12)
    application.add_handler(result_time_test_7, group=12)

    application.add_handler(test_next_8, group=13)
    application.add_handler(result_time_test_8, group=13)

    application.add_handler(test_next_9, group=14)
    application.add_handler(result_time_test_9, group=14)

    application.add_handler(test_next_10, group=15)
    application.add_handler(result_time_test_10, group=15)

    application.add_handler(test_next_11, group=16)
    application.add_handler(result_time_test_11, group=16)

    # application.add_handler(CommandHandler('timeee', words1.set_timer))

    application.run_polling()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
